import streamlit as st



st.title("NSFW | Main Page")

title = st.text_input('URL Link to Scan', 'https://wattlecorp.com')
# Add URL Checker python module or regex

st.button("Reset", type="primary")
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')


