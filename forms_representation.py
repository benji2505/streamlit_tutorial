import streamlit as st


def show_forms():
    with st.form(key='sample form'):
        st.title('Streamlit Forms')

        st.subheader('Form Input')
        name = st.text_input('Enter your name')
        st.write(f'Hello, {name}!')

        st.subheader('Date and Time Inputs')
        dob = st.date_input('Enter your date of birth')
        time = st.time_input('Choose a preferred time')

        st.subheader('Selectors')
        choice = st.radio('Select an option', ['Option 1', 'Option 2', 'Option 3'])
        gender = st.selectbox('Select your gender', ['Male', 'Female', 'Perverted'])
        slider_value = st.select_slider('Select a range', [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

        st.subheader('Toggles and Checkboxes')
        notifications = st.checkbox('Enable notifications')
        toggle_value = st.checkbox('dark mode?', value=True)

        st.subheader('submit button')
        submit_button = st.form_submit_button(label="Submit")  # only works withing defined form and reads form values
