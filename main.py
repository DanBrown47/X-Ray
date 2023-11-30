import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.title("NSFW | Main Page")


st.sidebar.success("v0.1.0 Alpha")


st.markdown(
    """
    # NSFW Classifier Demo

    This is a NSFW (Not Safe For Work) classifier built with machine learning models by Danwnad, Sivadas, and Mamtha for the Miniproject at CUSAT.

    **👈 Select a website from the sidebar** to check if it is offensive or not.

    ### How it works
    - The models analyze the content of a given website to determine if it contains offensive material.
    - Results will indicate whether the website is safe or potentially NSFW.

    ### Note
    This demo is for educational purposes and may not be perfect. Use it responsibly.

    ### See more projects
    - Discover other projects by visiting [Danwnad's GitHub](https://github.com/danbrown47/)
    """
)



# TODO : Add a button to force scan the URL