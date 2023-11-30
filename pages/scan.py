import streamlit as st
from src.scrapping_engine import scrap_image_urls, scrap_word_content
from src.models import save_url_to_db

main_url = st.text_input('URL Link to Scan', 'https://wattlecorp.com')
# Add URL Checker python module or regex

if st.button('Scan the URL'):
    save_url_to_db(main_url)
    # print('URL Saved to DB')
    # Image_resp = scrap_image_urls(main_url)
    Text_resp = scrap_word_content(main_url) # Text is in the offshore, Its working
    # st.write(Image_resp)
    st.write(Text_resp)


else:
    st.write('Click to scan')
