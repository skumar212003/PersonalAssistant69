import openai

# Replace 'Your-OpenAI-API-key-here' with your actual API key
openai.api_key = 'Your-OpenAI-API-key-here'

def get_gpt_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Update this to the correct engine name for GPT-4
            prompt=prompt,
            max_tokens=150
        )
        message = response['choices'][0]['text'].strip()
        return message
    except Exception as e:
        return str(e)

def main():
    print("Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        prompt = f"User: {user_input}\nAI:"
        response = get_gpt_response(prompt)
        print(f"AI: {response}")

if __name__ == "__main__":
    main()
