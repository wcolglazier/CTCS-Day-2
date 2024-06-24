import random


def get_response(user_input):
    user_input = user_input.lower()

    greetings = ["hello", "hi", "hey", "greetings"]
    farewells = ["bye", "goodbye", "see you", "later"]
    how_are_you = ["how are you", "how's it going", "how are you doing"]

    if user_input in greetings:
        return random.choice(
            ["Hi there! How can I help you today?", "Hello! What can I do for you?", "Hey! How's it going?"])
    elif user_input in how_are_you:
        return random.choice(
            ["I'm just a bot, but I'm doing great! How about you?", "I'm here to assist you! How are you?",
             "Doing well, thanks! What about you?"])
    elif user_input in farewells:
        return random.choice(["Goodbye! Have a great day!", "See you later!", "Take care!"])
    elif "weather" in user_input:
        return "I can't provide live weather updates, but you can check online for the latest forecast."
    elif "name" in user_input:
        return "I'm your friendly chatbot! What's your name?"
    elif "help" in user_input:
        return "I'm here to help! You can ask me about the weather, how I'm doing, or say hello."
    else:
        return random.choice(
            ["Sorry, I don't understand that. Can you rephrase?", "I'm not sure how to respond to that.",
             "Could you clarify what you mean?"])


def chat():
    print("Welcome to the chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye", "exit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")


chat()
