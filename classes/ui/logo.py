# Importing necessary libraries
import streamlit as st 

class Logo:
    def __init__(self, imagePath: str):
        st.logo(imagePath)
        self.imagePath = imagePath