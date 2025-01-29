import streamlit as st

def show_fragments():

    """
    Streamlit Fragments
    ===================

    Streamlit Fragments allow you to update only the fragment part of the page.
    you cannot return any date from a fragment
    
    """
    st.title('Fragments')
    st.write('This is a fragment example')

    @st.fragment()
    def toggle_and_text() -> None:
        cols = st.columns(2)
        cols[0].toggle('Toggle')
        cols[1].text_area('Enter Text')

    @st.fragment()
    def filter_and_file() -> None:
        new_cols = st.columns(5)
        new_cols[0].checkbox('filter')
        new_cols[1].file_uploader('upload_image')
        new_cols[2].selectbox('choose option', ['option 1', 'option 2, option 3'])
        new_cols[3].slider('slect value', 0, 100, 50)
        new_cols[4].text_input('enter text')

    toggle_and_text()
    cols = st.columns(2)
    cols[0].selectbox('Select', [1,2,3], None)
    cols[1].button('Update')
    filter_and_file()
