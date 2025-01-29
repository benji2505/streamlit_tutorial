import streamlit as st


def show_session_value():
    if 'count' not in st.session_state:
        st.session_state.count = 0

    st.write(f'Count: {st.session_state.count}')

    if st.button('Increment Counter'):
        st.session_state.count += 1
        # toggle on and off
        st.rerun()  # rerun the web page, this way you do not have wait for refreshing of webpage

    if st.button('Reset Counter'):
        st.session_state.count = 0
        st.rerun()

    st.write(f'Count: {st.session_state.count}')