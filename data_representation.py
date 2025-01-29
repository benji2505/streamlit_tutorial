import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def show_data_representation():
    st.title('Streamlit Data Representation')
    st.subheader('Dataframe')
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 32, 37, 45],
        'Occupation': ['Engineer', 'Doctor', 'Artist', 'Cook']
    })
    st.dataframe(df)

    st.subheader('Data Editor')
    editable_df = st.data_editor(df)
    st.subheader('Static Table')
    st.table(df)

    st.subheader('Metrics')
    st.metric(label='total Rows', value=df.shape[0])
    st.metric(label='total Columns', value=df.shape[1])
    st.metric(label='average age', value=round(df['Age'].mean(), 1), delta=df['Age'].mean())

    st.subheader('JSON and Dictionaries')
    sample_dict = {
        'name': 'Alice',
        'age': 25,
        'skills': ['Python', 'Data Science', 'Machine Learning']
    }
    st.json(sample_dict)

    st.write('Dictionary View', sample_dict)