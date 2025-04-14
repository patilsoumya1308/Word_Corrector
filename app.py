import streamlit as st
from textblob import TextBlob
import nltk

# Download necessary NLTK corpora
nltk.download('brown')
nltk.download('punkt')

# Page config
st.set_page_config(page_title="Words Corrector", page_icon="📝", layout="centered")

# Styling (similar to your HTML/CSS)
st.markdown("""
    <style>
    body {
        background: rgb(230, 85, 230);
    }
    .main {
        background-color: plum;
        padding: 2rem;
        border-radius: 8px;
        max-width: 600px;
        margin: auto;
        color: black;
        font-family: Arial, sans-serif;
    }
    .stTextInput input {
        background: purple;
        color: white;
        font-size: 20px;
        height: 50px;
        text-align: center;
    }
    .stButton>button {
        background-color: purple;
        color: white;
        font-size: 20px;
        padding: 12px;
        border-radius: 4px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main"><h2 style="text-align:center;">Words Corrector</h2>', unsafe_allow_html=True)

user_input = st.text_input("Enter Wrong Words...")

if st.button("Check Words"):
    if user_input.strip():
        words = user_input.split()
        corrected_words = [str(TextBlob(word).correct()) for word in words]
        corrected = " ".join(corrected_words)

        st.markdown('<div class="results">', unsafe_allow_html=True)
        st.subheader("Wrong Words :")
        st.write(words)
        st.subheader("Corrected Words :")
        st.write(corrected)
        st.markdown('</div></div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter some text.")
