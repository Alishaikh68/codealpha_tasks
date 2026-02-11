def get_response(user_input):
    user_input = user_input.lower().strip()

    # Greetings
    if user_input in ["hi", "hello", "hey", "hii"]:
        return "Hello! How can I help you today?"

    # How are you
    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking 😊"

    # Name related
    elif "your name" in user_input:
        return "I am a simple rule-based chatbot created in Python."

    # Help related
    elif "help" in user_input:
        return "Sure! You can ask me about my name, status, or say hello."

    # Thanks
    elif "thank" in user_input:
        return "You're welcome! Happy to help."

    # Exit commands
    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a nice day 👋"

    # Unknown input
    else:
        return "Sorry, I didn't understand that. Please try something else."


def chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("🤖 Chatbot:", response)

        if user_input.lower() in ["bye", "exit", "quit"]:
            break


# Run chatbot
chatbot()
