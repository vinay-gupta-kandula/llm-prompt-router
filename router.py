from classifier import classify_intent
from prompts import EXPERT_PROMPTS


def route_and_respond(user_message: str):
    """
    Routes the user's message to the correct expert persona
    based on the detected intent.
    """

    # Step 1: classify the user message
    classification = classify_intent(user_message)
    intent = classification["intent"]

    # Step 2: handle unclear requests
    if intent == "unclear":
        clarification_msg = (
            "I couldn't clearly understand your request. "
            "Are you asking about programming, data analysis, writing help, "
            "or career advice?"
        )
        return classification, clarification_msg

    # Step 3: get the appropriate expert prompt
    expert_prompt = EXPERT_PROMPTS.get(intent)

    # Step 4: generate a simple expert-style response
    if intent == "code":
        response_text = (
            f"{expert_prompt}\n\n"
            "Example approach:\n"
            "In Python, you can sort a list using the built-in sorted() function:\n\n"
            "sorted_list = sorted(my_list)"
        )

    elif intent == "data":
        response_text = (
            f"{expert_prompt}\n\n"
            "Example calculation:\n"
            "Average = (12 + 45 + 67) / 3 = 41.33"
        )

    elif intent == "writing":
        response_text = (
            f"{expert_prompt}\n\n"
            "Suggestion:\n"
            "Check sentence clarity and remove unnecessary filler words. "
            "Breaking long sentences into shorter ones can also improve readability."
        )

    elif intent == "career":
        response_text = (
            f"{expert_prompt}\n\n"
            "Interview preparation tips:\n"
            "- Research the company and role\n"
            "- Practice common interview questions\n"
            "- Prepare examples of your past work or projects"
        )

    else:
        response_text = "Sorry, I couldn't generate a suitable response."

    return classification, response_text