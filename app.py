import streamlit as st
def translate(sentence):

    translations = {
        "hello":"bonjour",
        "good morning":"bonjour",
        "good night":"bonne nuit",
        "thank you":"merci",
        "welcome":"bienvenue",
        "how are you":"comment allez vous",
        "i am fine":"je vais bien",
        "what is your name":"quel est votre nom",
        "i am a student":"je suis etudiant",
        "i like coffee":"j aime le cafe"
    }

    return translations.get(
        sentence.lower(),
        "Translation not found"
    )
st.set_page_config(
    page_title="English-French Translator",
    page_icon="🌎"
)

st.markdown(
"""
# 🌎 English → French Translator

Translate English sentences into French using a Transformer Model.
"""
)

col1, col2 = st.columns(2)

with col1:
    text = st.text_area(
        "English Text",
        height=150
    )

with col2:
    st.text_area(
        "French Translation",
        value=st.session_state.get(
            "translation",
            ""
        ),
        height=150
    )

if st.button("Translate"):

    translated_text = translate(text)

    st.session_state["translation"] = translated_text

    st.rerun()