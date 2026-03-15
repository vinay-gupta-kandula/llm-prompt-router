def classify_intent(user_message: str):
    """
    Basic keyword-based intent classifier.
    Determines the user's request category.
    """

    text = user_message.lower()

    coding_keywords = ["python", "code", "bug", "function", "program", "algorithm"]
    data_keywords = ["average", "data", "statistics", "numbers", "dataset"]
    writing_keywords = ["paragraph", "writing", "grammar", "sentence", "essay"]
    career_keywords = ["career", "job", "interview", "resume", "cv"]

    if any(keyword in text for keyword in coding_keywords):
        return {"intent": "code", "confidence": 0.88}

    elif any(keyword in text for keyword in data_keywords):
        return {"intent": "data", "confidence": 0.87}

    elif any(keyword in text for keyword in writing_keywords):
        return {"intent": "writing", "confidence": 0.86}

    elif any(keyword in text for keyword in career_keywords):
        return {"intent": "career", "confidence": 0.85}

    else:
        return {"intent": "unclear", "confidence": 0.55}