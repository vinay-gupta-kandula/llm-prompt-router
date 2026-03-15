from classifier import classify_intent
from prompts import SYSTEM_PROMPTS


def route_and_respond(message: str):

    intent_data = classify_intent(message)

    intent = intent_data["intent"]

    if intent == "unclear":
        return intent_data, (
            "I'm not sure what you're asking. "
            "Are you looking for help with coding, data analysis, writing improvement, "
            "or career advice?"
        )

    system_prompt = SYSTEM_PROMPTS.get(intent)

    # Generate simple response using expert persona
    if intent == "code":
        response = f"{system_prompt}\n\nExample solution:\nUse Python's built-in sorted() function:\n\nsorted_list = sorted(your_list)"

    elif intent == "data":
        response = f"{system_prompt}\n\nTo calculate the average:\n(12 + 45 + 67) / 3 = 41.33"

    elif intent == "writing":
        response = f"{system_prompt}\n\nYour sentence may contain clarity or tone issues. Review sentence structure and remove filler words."

    elif intent == "career":
        response = f"{system_prompt}\n\nFor interview preparation: research the company, practice common questions, and prepare examples of your past work."

    else:
        response = "I couldn't generate a response."

    return intent_data, response