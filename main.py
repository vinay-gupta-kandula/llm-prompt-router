import json
import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import SYSTEM_PROMPTS

# Load environment variables from the .env file
load_dotenv()

# Explicitly fetch the key and handle the error cleanly
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("🛑 ERROR: GEMINI_API_KEY is missing! Make sure you have a .env file with your key.")
    exit(1)

# Initialize Gemini client explicitly with the fetched key
client = genai.Client(api_key=api_key)

# STEP 2: Develop the Classifier Prompt
# Engineered to be short and focused, returning only a JSON object [cite: 92]
CLASSIFIER_PROMPT = """Your task is to classify the user's intent. Based on the user message below, choose one of the following labels: code, data, writing, career, unclear. Respond with a single JSON object containing two keys: 'intent' (the label you chose) and 'confidence' (a float from 0.0 to 1.0, representing your certainty). Do not provide any other text or explanation."""

# STEP 3: Build the Classifier Function
def classify_intent(message: str) -> dict:
    try:
        full_prompt = f"{CLASSIFIER_PROMPT}\n\nUser message: {message}"
        
        # Making the initial LLM call optimized for speed [cite: 69, 71]
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=full_prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json", # Strictly enforce JSON output [cite: 92]
                temperature=0.0
            )
        )
        
        # Parse the JSON response [cite: 95]
        intent_data = json.loads(response.text)
        
        # Ensure the required schema exists, otherwise force fallback
        if "intent" not in intent_data or "confidence" not in intent_data:
            raise ValueError("Missing required keys in LLM JSON response")
            
        return intent_data

    except Exception as e:
        # Gracefully handle malformed or non-JSON responses without crashing [cite: 176, 177]
        print(f"\n[DEBUG] API Error: {e}")
        return {"intent": "unclear", "confidence": 0.0} # Default to unclear [cite: 180]

# STEP 4: Build the Routing Function
def route_and_respond(message: str, intent_data: dict) -> str:
    intent = intent_data.get("intent", "unclear")
    
    # Handle 'unclear' intent without guessing or routing to a default expert [cite: 159]
    if intent == "unclear" or intent not in SYSTEM_PROMPTS:
        # Generate a response that asks the user for clarification [cite: 160]
        return "Are you asking for help with coding, data analysis, writing, or career advice?" 
        
    # Valid intent: select the correct expert system prompt [cite: 156]
    expert_prompt = SYSTEM_PROMPTS[intent]
    
    # Make the second LLM call using the selected expert persona [cite: 157]
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=message,
        config=types.GenerateContentConfig(
            system_instruction=expert_prompt,
            temperature=0.7 
        )
    )
    
    return response.text # Return final generated text as a string [cite: 158]

# STEP 5: Implement Logging
def log_interaction(intent_data: dict, user_message: str, final_response: str):
    log_entry = {
        "intent": intent_data.get("intent", "unclear"),
        "confidence": intent_data.get("confidence", 0.0),
        "user_message": user_message,
        "final_response": final_response
    }
    
    # Append a single JSON object to the file on a new line [cite: 173, 174]
    with open("route_log.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")

if __name__ == "__main__":
    # STEP 6: Test Thoroughly
    test_messages = [
        "how do i sort a list of objects in python?",
        "explain this sql query for me",
        "This paragraph sounds awkward, can you help me fix it?",
        "In preparingshboards inkilleraplany tipetile GPP",
        "what's the average of these numbers: 12, 45, 23, 67, 34",
        "Help me make this better.",
        "I need to write a function that takes a user id and returns their profile, but also i need help with my resume.",
        "hey",
        "Can you write me a poem about clouds?",
        "Rewrite this sentence to be more professional.",
        "I'm not sure what to do with my career.",
        "what is a pivot table",
        "fxi thsi bug pls: for i in range(10) print(i)",
        "How do I structure a cover letter?",
        "My boss says my writing is too verbose."
    ]

    print("Starting tests and generating route_log.jsonl...")
    
    for i, msg in enumerate(test_messages, 1):
        print(f"\n--- Test {i} ---")
        print(f"User: {msg}")
        
        intent_data = classify_intent(msg)
        print(f"Classified Intent: {intent_data}")
        
        final_answer = route_and_respond(msg, intent_data)
        log_interaction(intent_data, msg, final_answer)
        print(f"Response: {final_answer}")
        
        # Optional delay for free-tier testing
        if os.getenv("USE_FREE_TIER_DELAY") == "true" and i < len(test_messages):
            print("Free tier mode active: Pausing for 5 seconds to respect rate limits...")
            time.sleep(5) 
            
    print("\n✅ Testing complete! Check your route_log.jsonl file.")