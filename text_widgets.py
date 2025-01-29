import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def show_text_widgets():
    st.title('Hello, World!')
    st.header('this is our header')
    st.subheader('this is our subheader')
    st.markdown('this is our _markdown_')  # double underscore for italics
    st.caption('this is our caption')
    st.divider()

    code_example = """
    def greet(name):
        print('hello', name)
    """
    st.code(code_example, language='python')

    pressed = st.button('Press me')
    print(pressed)