import re
import streamlit as st
from agents.rag import get_rag_answer
from agents.whisper_stt import record_audio

# Streamlit Page Settings
st.set_page_config(page_title="Finance Assistent", page_icon="📈", layout="centered")
st.markdown(
    """
    <style>
    .stApp {
        background-color: #eef5fa;
        font-family: 'Arial', sans-serif;
    }
    h1, h4 {
        color: #003366;
        text-align: center;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        background-color: #ffffff;
        color: #003366;
        border-radius: 8px;
        padding: 10px;
        border: 1px solid #aaa;
    }
    .stButton>button {
        background-color: #0057b7;
        color: white;
        border-radius: 8px;
        padding: 8px 16px;
        font-size: 16px;
        border: none;
    }
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("<h1>📈 Market Brief Assistant</h1>", unsafe_allow_html=True)
st.markdown("<h4>Get real-time insights from your voice</h4>", unsafe_allow_html=True)
st.write("---")

# Voice Input & Market Response 
if st.button("Record Voice"):
    with st.spinner("Transcribing your voice..."):
        try:
            transcribed_text = record_audio()
            st.success("You said:")
            st.write(transcribed_text)

            with st.spinner("Getting market insights..."):
                result = get_rag_answer(transcribed_text)

                # Extract and clean response
                response = result.get("answer") if isinstance(result, dict) else result
                confidence = result.get("confidence", 1.0) if isinstance(result, dict) else 1.0
                if confidence < 0.65:
                    st.warning("I'm not confident about the answer. Could you please rephrase your question?")
                else:
                    response = re.sub(r"<think>.*?</think>\n\n?", "", response, flags=re.DOTALL)
                    st.success("Market Brief:")
                    st.write(response)

        except Exception as e:
            st.error(f"Error: {str(e)}")

# Footer
st.markdown(
    """
    <hr style='border: 0.5px solid #6c757d;'>
    <div style='text-align: center; color: #003366;'>
      Powered by AI Market Voice Agent
    </div>
    """,
    unsafe_allow_html=True
)