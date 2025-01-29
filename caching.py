import streamlit as st
import time


def show_caching() -> None:
    """
    Caching in Streamlit
    ====================

    Streamlit provides different types of caching. Caching allows you to store
    the results of expensive computations so that they can be reused instead
    of recomputed.

    The most common use case is to cache function results.
    """

    st.title('Caching')
    st.write('This is a caching example')

    @st.cache_data(ttl=60)  # cache data for 60 seconds
    def get_data():  # for immutable data only. for mutable data use @st.cache_resource
        time.sleep(1)  # simulate expensive computation
        return {'data': 'This is cached data!'}

    st.write('Fetching data...')
    data = get_data()
    st.write(data)

    file_path = 'static/data_dump.txt'

    @st.cache_resource
    def get_file_handler():  # for mutable data. if one user saves file, it will affect all users
        file = open(file_path, 'a+')
        return file

    file_handler = get_file_handler()

    if st.button('write to file'):
        file_handler.write('New line of text!\n')
        file_handler.flush()
        st.success('wrote new line to the file!')

    if st.button('read from file'):
        file_handler.seek(0)
        content = file_handler.read()
        st.text(content)

    st.button('close file', on_click=file_handler.close)




