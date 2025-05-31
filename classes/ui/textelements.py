# Importing necessary libraries
import streamlit as st

class TextElement:
    def __init__(self, text: str):
        st.markdown(text)