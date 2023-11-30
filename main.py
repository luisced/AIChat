import openai

"""
Webs de interés:
- Módulo OpenAI: https://github.com/openai/openai-python
- Documentación API ChatGPT: https://platform.openai.com/docs/api-reference/chat
"""

def main():

    openai.api_key = ""

    print("💬 ChatGPT API en Python")
    print("Comandos disponibles:")
    print("  exit - Salir de la aplicación")
    print("  new - Crear una nueva conversación")

    # Initial conversation context
    conversation_history = []

    while True:

        user_input = input("\n¿Sobre qué quieres hablar? ")

        if user_input.lower() == "exit":
            if confirm_exit():
                break
            continue

        if user_input.lower() == "new":
            print("🆕 Nueva conversación creada")
            conversation_history = []
            continue

        conversation_history.append(user_input)
        response = generate_response(conversation_history)
        print("> " + response)
        conversation_history.append(response)


def confirm_exit() -> bool:
    exit_confirm = input("✋ ¿Estás seguro? (y/n): ")
    if exit_confirm.lower() == 'y':
        print("👋 ¡Hasta luego!")
        return True
    return False


def generate_response(history: list) -> str:
    prompt = "\n".join(history)
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # or another model name
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print("Error al generar la respuesta:", e)
        return "Hubo un error."


if __name__ == "__main__":
    main()
