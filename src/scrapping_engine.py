import requests
from bs4 import BeautifulSoup
import re


#link, media, resources
def download_image(url):
    pass    


def put_to_queue(url, data, type):
    if type == 'text':
        pass
    else:
        pass

def scrap_image_urls(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:

            soup = BeautifulSoup(response.text, "html.parser")

            img_tags = soup.find_all('img', src=True)
            img_urls = [img['src'] for img in img_tags]
            
            # Filter out absolute and relative image URLs
            valid_img_urls = [img_url for img_url in img_urls if img_url.startswith("http") or img_url.startswith("www.") ]
            
            #  TODO or img_url.startswith("/")/ Integrate this later 
            image_no = len(valid_img_urls)
            # Display the list of image URLs
            for img_url in valid_img_urls:
                print(img_url)
        
            return_msg = f"Found {image_no} images in the webpage | Moving to the queue"

        else:
            print("Failed to retrieve the webpage. Status code:", response.status_code)
            return_msg = "Failed to retrieve the webpage. "
    except Exception as e:
        print("An error occurred:", str(e))
        return_msg = "Failed to retrieve the webpage. {}".format(str(e))


    return return_msg



def scrap_word_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Find all text content within the HTML document
            text_content = soup.get_text()
            
            # Split the text into words using whitespace as the delimiter
            words = re.findall(r'\b\w+\b', text_content)
            # Send as a single request for all the words
            
            # Display the list of words
            for idx, word in enumerate(words):
                print(idx, word)
            return_msg = f"Found {len(words)} words in the webpage | Moving to the queue"
        else:
            print("Failed to retrieve the webpage. Status code:", response.status_code)
            return_msg = "Failed to retrieve the webpage. "
    except Exception as e:
        print("An error occurred:", str(e))
        return_msg = "Failed to retrieve the webpage. {}".format(str(e))
    
    return return_msg


if __name__ == "__main__":
    no_img = scrap_image_urls("https://wattlecorp.com/")
    no_content = scrap_word_content("https://en.wikipedia.org/wiki/The_Last_King_of_Scotland_(film)")
    