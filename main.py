import streamlit as st
from src.scrapping_engine import scrap_image_urls, scrap_word_content
from src.models import save_url_to_db

st.title("NSFW | Main Page")


st.sidebar.success("Select a demo above.")


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

main_url = st.text_input('URL Link to Scan', 'https://wattlecorp.com')
# Add URL Checker python module or regex

if st.button('Scan the URL'):
    # save_url_to_db(main_url)
    # print('URL Saved to DB')
    Image_resp = scrap_image_urls(main_url)
    Text_resp = scrap_word_content(main_url) # Text is in the offshore, Its working
    st.write(Image_resp)
    st.write(Text_resp)


else:
    st.write('Click to scan')

# TODO : Add a button to force scan the URL