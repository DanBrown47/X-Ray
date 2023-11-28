import streamlit as st
from src.models import get_from_db_all_values
# Add a button to the app

result = get_from_db_all_values()
st.dataframe(result)

# Add a button to the app
if st.button("Re-scan"):
    st.write("Re-scanning...")
    
