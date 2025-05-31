# Importing necessary libraries
import streamlit as st

class Page:
    def __init__(self, name: str, icon: str, pageLayout='centered'):
        st.set_page_config(page_title=name, page_icon=icon, layout=pageLayout)
        self.name = name
        self.icon = icon
        self.pageLayout = pageLayout