1. Uma função input() sempre devolve uma string. Alternativa C.
2. O motivo da API key ficar sempre no .env é principalmente por segurança. Se a chave da API ficar em um arquivo .py, e ir, por exemplo, para um repositório do GitHUB, a chave vai correr o risco de ser invadida por terceiros.
3. Alternativa B. Lista de dicionários.
4. 
total = 0
while True:
 n = int(input("Número (0 para sair): "))
 if n == 0:
    break
 total += n
print(f"Soma: {total}")

5.
a.
Acontece por que não tinha nada feito para guardar as mensagens enviadas. assim, mesmo a ana falando seu nome, quando ela mandava outra mensagem a IA não conseguia buscar as mensagens que já foram enviadas anterioremente.

b. 
Essa linha define a função que recebe uma lista de mensagens e retorna uma string
def perguntar(mensagens: list) -> str:

Essa linha envia o histórico para a IA, permitindo que ela considere as mensagens anteriores
"messages": mensagens

6. B. Pega o primeiro item da lista choices

7. 
def carregar_contexto(caminho: str = "contexto.txt") -> str:
    try:
        with open(caminho, encoding="utf-8") as arquivo:
            texto = arquivo.read().strip()
    except FileNotFoundError:
        print(f"Aviso: arquivo '{caminho}' não encontrado. Seguindo sem contexto.")
        return ""

8. 
a.
import streamlit as st

if "historico" not in st.session_state:
    st.session_state.historico = []

pergunta = st.chat_input("Digite...")

if pergunta:
    st.session_state.historico.append({"role": "user", "content": pergunta})

b. Se usa st.session_state para manter o histórico de mensagens mesmo quando o streamlit executa novamente o código. Se usar apenas historico = [], a lista vai ser reiniciada a cada execução, perdendo as mensagens anteriores