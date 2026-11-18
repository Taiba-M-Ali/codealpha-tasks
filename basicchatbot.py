def chatbot_reply(user_input):
    text = user_input.lower().strip()
    text = text.replace("?","").replace("!","").replace("."," ")

    if text in ("hello", "hi", "hey"):
        return "Hi!"
    elif text == "how are you":
        return "I am fine, thanks!"
    elif text in ("bye", "goodbye", "exit"):
        return "Good bye!"
    else:
        return "Sorry,I don't understand that"


def main():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        reply = chatbot_reply(user_input)
        print("Chatbot:", reply)
        if reply == "Good bye!":
            break


main()
