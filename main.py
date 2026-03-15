from router import route_and_respond
from logger import log_route


def run_router():
    print("AI Intent Router System")
    print("Type 'exit' anytime to stop the program.\n")

    while True:
        user_input = input("Your message: ")

        if user_input.lower() == "exit":
            print("Session ended. Goodbye!")
            break

        # process the message
        result, reply = route_and_respond(user_input)

        detected_intent = result["intent"]
        confidence_score = result["confidence"]

        print("\nDetected Intent:", detected_intent)
        print("Confidence Score:", confidence_score)
        print("\nGenerated Response:\n", reply)
        print("\n--------------------------------------\n")

        # store the interaction in log file
        log_route(detected_intent, confidence_score, user_input, reply)


if __name__ == "__main__":
    run_router()