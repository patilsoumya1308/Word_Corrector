import streamlit as st
from spellchecker import SpellChecker

# Initialize Streamlit app
st.title("Words Corrector")

# User Input
wrong_words_input = st.text_input("Enter Wrong Words...")

# Button to Check Words
if st.button("Check Words"):
    # Process input
    spell = SpellChecker()
    wrong_words = wrong_words_input.split(',')
    corrected_words = [spell.candidates(word.strip()) for word in wrong_words]
    
    # Displaying results
    st.subheader("Wrong Words :")
    st.write([word.strip() for word in wrong_words])  # Show the wrong words
    st.subheader("Corrected Words :")
    st.write([spell.candidates(word.strip()).pop() for word in wrong_words])  # Show corrected words
