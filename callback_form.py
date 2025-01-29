import streamlit as st


def callback_form():
    if 'step' not in st.session_state:
        st.session_state.step = 1

    if 'info' not in st.session_state:
        st.session_state.info = {}

    def go_to_step2(name):  # call-back function executed before anything else gets executed
        st.session_state.info['name'] = name
        st.session_state.step = 2

    def go_to_step1():
        st.session_state.step = 1
        

    if st.session_state.step == 1:
        st.header('Part 1: Information')

        name = st.text_input('Enter your name', value=st.session_state.info.get('name', ''))

        st.button('Next', on_click=go_to_step2, args=(name,))


    elif st.session_state.step == 2:
        st.header('Part 2: Review')

        st.subheader('Please review:')
        st.write(f'**Name**: {st.session_state.info.get("name", "")}')

        if st.button('Submit'):
            st.success('Thank you!')
            st.balloons()
            st.session_state.info = {}
            st.session_state.step = 1

        st.button('Previous', on_click=go_to_step1)

