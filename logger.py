import json


def log_route(intent, confidence, user_message, final_response):
    """
    Logs routing decisions and responses to route_log.jsonl
    """

    log_entry = {
        "intent": intent,
        "confidence": confidence,
        "user_message": user_message,
        "final_response": final_response
    }

    with open("route_log.jsonl", "a") as log_file:
        json.dump(log_entry, log_file)
        log_file.write("\n")