# tela do app
# rodar com: py -m streamlit run app.py
import streamlit as st

from chat_contexto import historico_para_envio, novo_historico
from llm_memoria import perguntar
from prompts import NOME_ASSISTENTE

st.set_page_config(page_title=NOME_ASSISTENTE)
st.title(NOME_ASSISTENTE)
st.caption("Pergunta sobre horários, cardápio, preços e delivery.")

if "historico" not in st.session_state:
    st.session_state.historico = novo_historico()

with st.sidebar:
    st.header("Opçôes")
    if st.button("Limpar e conversa"):
        st.session_state.historico = novo_historico()
        st.rerun()
    if st.button("Recarregar contexto.txt"):
        st.session_state.historico = novo_historico()
        st.rerun()

for mensagem in st.session_state.historico:
    if mensagem["role"] == "system":
        continue
    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])

pergunta = st.chat_input("Digite sua pergunta...")

if pergunta:
    st.session_state.historico.append({"role": "user", "content": pergunta})
    with st.chat_message("user"):
        st.markdown(pergunta)

    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            resposta = perguntar(historico_para_envio(st.session_state.historico))
        st.markdown(resposta)

st.session_state.historico.append({"role": "assistant", "content": pergunta})