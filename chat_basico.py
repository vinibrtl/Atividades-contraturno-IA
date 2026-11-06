# chat_basico.py — chatbot no terminal (Groq)
from llm import perguntar

COMANDOS = "Comandos: 'ajuda' mostra esta mensagem, 'sair' encerra o chat"


def main() -> None:
    print("Chat com Groq — digite 'ajuda' ou 'sair'\n")
    total_perguntas = 0

    while True:
        pergunta = input("você> ").strip()
        comando = pergunta.lower()

        if comando == "sair":
            print(f"Até logo! Você fez {total_perguntas} pergunta(s).")
            break

        if comando == "ajuda":
            print(COMANDOS)
            continue

        if not pergunta:
            continue

        resposta = perguntar(pergunta)
        total_perguntas += 1
        print("ia>", resposta)
        print()


if __name__ == "__main__":
    main()
