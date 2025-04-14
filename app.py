import streamlit as st
from textblob import TextBlob

st.title("Spell Checker using TextBlob")

# Input list of words
words_input = st.text_input("Enter words separated by commas", "Machne, Learnin")

# Process input
if words_input:
    words = [word.strip() for word in words_input.split(",")]
    corrected_words = [TextBlob(word).correct() for word in words]

    st.write("### Wrong Words:")
    st.write(words)

    st.write("### Corrected Words:")
    st.write([str(word) for word in corrected_words])
