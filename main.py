import openai

openai.api_key = "sk-proj-3cYksoPkHvjzvGgH9XkhT3BlbkFJ9ZDSCpILOIkG6dU4lKBO"
I7VZqjaKfJDwe3zHMbXGT3BlbkFJYKjZ5jlgs7EUtaPdfKqk
gvDVj1HD1YmEdcTGDh38T3BlbkFJdVa6kckJq4lOdfESfVOj

def bot(user_input, messages):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )
    message = response.choices[0].message['content']
    messages.append({"role": "assistant", "content": message})
    return message, messages


if __name__ == '__main__':
    messages = [
        {"role": "system", "content": """



        """}
    ]

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("Session ended.")
            break

        response, messages = bot(user_input, messages)
        print("Assistant:", response)
