import streamlit as st

def show_layout():
    st.title('Layouts')
    st.write('This is a layout example')

    st.sidebar.title('Sidebar')
    st.sidebar.write('This is a sidebar layout')
    sidebar_input = st.sidebar.text_input('Enter a value')


    tabs = st.tabs(['Tab 1', 'Tab 2', 'Tab 3'])

    with tabs[0]:
        st.write('Tab 1 content')
    with tabs[1]:
        st.write('Tab 2 content')
    with tabs[2]:
        st.write('Tab 3 content')

    with tabs[0]:
        cols = st.columns(4)
        with cols[0]:
            st.write('Column 1')
        with cols[1]:
            st.write('Column 2')
        with cols[2]:
            st.write('Column 3')
        with cols[3]:
            st.write('Column 4')


    with tabs[1]:
        with st.container(border=True):
            st.write('Container 1')
            st.write('you can think of a container as a grouping of elements')
            st.write('container help you manage sections of the page')
        st.write('Hover over this button for a tooltip')
        st.button('Button with tooltip', help='This is a tooltip')

    with tabs[2]:
        placeholder = st.empty()
        placeholder.write('this is an empty container')
        if st.button('update placeholder'):
            placeholder.write('this is updated info inside the placeholder')

        with st.expander('expand for more details'):
            st.write('this is additional information')
            st.write('use the expander to keep your interface cleaner')

        if sidebar_input:
            st.write(f'You entered in the sidebar: {sidebar_input}')
