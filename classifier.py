def classify_intent(message: str):
    """
    Simple rule-based intent classifier
    """

    message_lower = message.lower()

    if any(word in message_lower for word in ["python", "code", "bug", "function", "program"]):
        return {"intent": "code", "confidence": 0.9}

    elif any(word in message_lower for word in ["average", "data", "statistics", "numbers"]):
        return {"intent": "data", "confidence": 0.9}

    elif any(word in message_lower for word in ["paragraph", "writing", "grammar", "sentence"]):
        return {"intent": "writing", "confidence": 0.9}

    elif any(word in message_lower for word in ["career", "job", "interview", "resume"]):
        return {"intent": "career", "confidence": 0.9}

    else:
        return {"intent": "unclear", "confidence": 0.5}