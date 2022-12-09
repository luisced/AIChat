import openai
openai.api_key = "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"

margin1, margin2, margin3, margin4, margin5, margin6 = "╔═", "═╗", "╚═", "═╝", "║", "═"


def chat_with_gpt3():
    while True:
        prompt = input(f"You: ")
        if prompt == "exit":
            break
        else:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None
            )
            # remove the enter key from the response
            answer = response['choices'][0]['text'].replace("\n", "")

        print(f"GPT-3: {answer}")


chat_with_gpt3()
