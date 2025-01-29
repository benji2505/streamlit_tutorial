import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def show_chart_representation():
    st.title('Streamlit Chart Representation')
    st.subheader('Line Chart')
    df = pd.DataFrame(np.random.randn(10, 4), columns=['a', 'b', 'c', 'd'])
    st.line_chart(df)

    st.subheader('Area Chart')
    df = pd.DataFrame(np.random.randn(10, 4), columns=['a', 'b', 'c', 'd'])
    st.area_chart(df)

    st.subheader('Bar Chart')
    df = pd.DataFrame(np.random.randn(10, 4), columns=['a', 'b', 'c', 'd'])
    st.bar_chart(df)

    st.subheader('Scatter Chart')
    scatter_data = pd.DataFrame({
        'x': np.random.randn(100),
        'y': np.random.randn(100)
    })
    st.scatter_chart(scatter_data)

    st.subheader('Map Chart')
    latitude = 41.5855
    longitude = -70.9408
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [latitude, longitude],
        columns=['lat', 'lon']
    )
    st.map(map_data)

    st.subheader('Pyplot Chart')
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [1, 4, 9, 16], label='A')
    ax.plot([2, 3, 4, 5], [1, 2, 4, 8], label='B')
    ax.plot([3, 4, 5, 6], [1, 3, 6, 9], label='C')
    ax.legend()
    st.pyplot(fig)