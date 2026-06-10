import streamlit as st

st.set_page_config(
    page_title="English-French Translator",
    page_icon="🌎",
    layout="wide"
)

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

st.title("🌎 English → French Translator")

text = st.text_area(
    "Enter English Text",
    height=150
)

if st.button("Translate"):

    translated_text = translations.get(
        text.lower().strip(),
        "Translation not found in training data"
    )

    st.success(translated_text)
