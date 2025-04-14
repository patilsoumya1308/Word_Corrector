import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="Spell Corrector", page_icon="📝", layout="centered")

# Custom CSS styling
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
        }
        .stTextInput input {
            background-color: purple;
            color: white;
            height: 50px;
            font-size: 20px;
            text-align: center;
        }
        .stButton>button {
            background-color: purple;
            color: white;
            font-size: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Main content
st.markdown("<div class='main'>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;color:black;'>Words Corrector</h2>", unsafe_allow_html=True)

text_input = st.text_input("Enter Wrong Words...", "")

if st.button("Check Words"):
    if text_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        blob = TextBlob(text_input)
        corrected_text = str(blob.correct())
        if corrected_text != text_input:
            st.markdown("""
                <div style='background: purple; padding: 1rem; border-radius: 4px; color: white;'>
                    <h3>Wrong Words:</h3>
                    <p>{}</p>
                    <h3>Corrected Words:</h3>
                    <p>{}</p>
                </div>
            """.format(text_input, corrected_text), unsafe_allow_html=True)
        else:
            st.success("No corrections needed!")
st.markdown("</div>", unsafe_allow_html=True)
