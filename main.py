import openai
openai.api_key = "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"


def chat_with_gpt3():
    while True:
        prompt = input("You: ")
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None
        )

        print("GPT-3: ", response["choices"][0]["text"])


chat_with_gpt3()
# q: how do i create a virtual environment in python?
