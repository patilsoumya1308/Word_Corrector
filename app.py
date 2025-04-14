import streamlit as st
from textblob import TextBlob

# Custom CSS to mimic your style
st.markdown("""
    <style>
    body {
        background: rgb(230, 85, 230);
    }
    .main {
        background-color: plum;
        border-radius: 10px;
        padding: 2rem;
        max-width: 600px;
        margin: auto;
        color: black;
    }
    .stTextInput>div>div>input {
        background-color: purple;
        color: white;
        text-align: center;
        height: 50px;
        font-size: 20px;
    }
    .stTextInput>div>div>input::placeholder {
        color: white;
        opacity: 1;
    }
    .stButton>button {
        background-color: purple;
        color: white;
        font-size: 20px;
        border-radius: 4px;
        width: 100%;
        padding: 12px;
    }
    .results {
        margin-top: 1.5rem;
        padding: 1rem;
        background: purple;
        border-radius: 4px;
        color: white;
    }
    .results p {
        background: rgba(255, 255, 255, 0.05);
        padding: 10px;
        border-radius: 4px;
    }
    </style>
""", unsafe_allow_html=True)

# Container for layout
with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;'>Words Corrector</h2>", unsafe_allow_html=True)

    text_input = st.text_input("Enter Wrong Words...", placeholder="Enter Wrong Words...")

    if st.button("Check Words"):
        if text_input:
            blob = TextBlob(text_input)
            corrected = str(blob.correct())
            wrong_words = ", ".join([word for word in text_input.split() if word not in corrected.split()])

            st.markdown('<div class="results">', unsafe_allow_html=True)
            st.markdown("<h3>Wrong Words :</h3>", unsafe_allow_html=True)
            st.markdown(f"<p>{wrong_words}</p>", unsafe_allow_html=True)
            st.markdown("<h3>Corrected Words :</h3>", unsafe_allow_html=True)
            st.markdown(f"<p>{corrected}</p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
