from router import route_and_respond
from logger import log_route


def main():
    print("LLM Prompt Router")
    print("Type 'exit' to quit\n")

    while True:
        user_message = input("Enter message: ")

        if user_message.lower() == "exit":
            print("Goodbye!")
            break

        intent_data, response = route_and_respond(user_message)

        intent = intent_data["intent"]
        confidence = intent_data["confidence"]

        print("\nDetected Intent:", intent)
        print("Confidence:", confidence)
        print("\nResponse:\n", response)
        print("\n-----------------------------------\n")

        # Log the request
        log_route(intent, confidence, user_message, response)


if __name__ == "__main__":
    main()