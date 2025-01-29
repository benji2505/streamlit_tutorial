import streamlit as st


def show_adv_widgets():
    st.title('Advanced Widgets')
    st.write('This is an advanced widget example')

    st.button('OK')
    st.button('OK', key='btn2') #st usually derives key from widget name, if same name you have to specify key

    # if yoi do not want parameter changed duri ghte session you have to store it in a session_state variable
    if 'slider' not in st.session_state:
        st.session_state.slider = 25

    min_value = st.slider('Set min value', 0, 50, 25)
    st.session_state.slider = st.slider('Slider', min_value, 100, st.session_state.slider)

    # if a widget is removed from rendering its session_state is removed and the value gets lost
    if 'checkbox' not in st.session_state:
        st.session_state.checkbox = False

    if 'user_input' not in st.session_state:
        st.session_state.user_input = ''

    def toggle_input():
        st.session_state.checkbox = not st.session_state.checkbox

    st.checkbox('Show Input Field', value=st.session_state.checkbox, on_change=toggle_input)

    if st.session_state.checkbox:
        user_input = st.text_input('Enter something', value= st.session_state.user_input)
        st.session_state.user_input = user_input
    else:
        user_input = st.session_state.get('user_input', '')

    st.write(f'User Input: {user_input}')