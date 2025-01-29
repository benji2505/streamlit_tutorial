import streamlit as st
from datetime import datetime

def show_sample_form():
    st.title('User Information Form')

    form_value = {
        'name': '',
        'email': '',
        'dob': '',
        'gender': '',
        'location': ''
    }
    mindate = datetime(1940, 1, 1)
    maxdate = datetime.now()

    with st.form(key='sample_form'):
        form_value['name'] = st.text_input('Enter your name')
        form_value['email'] = st.text_input('Enter your email')
        form_value['dob'] = st.date_input('Enter your dob', max_value=maxdate, min_value=mindate)
        form_value['gender'] = st.selectbox('Select your gender', ['Male', 'Female', 'Perversed'])
        form_value['location'] = st.text_input('Enter your location')

        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            if not all(form_value.values()):
                st.warning('Please fill in all the fields')
            else:
                st.balloons()
                st.success('Form submitted successfully')
                for key, value in form_value.items():
                    st.write(f'{key}: {value}')

