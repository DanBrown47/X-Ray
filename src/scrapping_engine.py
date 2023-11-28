import requests
from bs4 import BeautifulSoup
from src.offshore import send_to_queue_text, send_to_queue_image
import re
import json
import base64


# Also covert to Base64
def download_image(url):
    try:
        response = requests.get(url)
        content = response.content  # Assuming the content is in UTF-8 encoding
        # content = base64.b64encode(content)
        return content  # Return the content and no error
    except Exception as e:
        print(f"Error downloading content from {url}: {e}")
        return None

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
            for idx,img_url in enumerate(valid_img_urls):
                image = download_image(img_url)
                image_base64_str = base64.b64encode(image).decode('utf-8')
                print("[+] Found image:", img_url)
                payload = {
                    'site': str(url),
                    'image_count': str(str(idx+1)+'/'+str(image_no)),
                    'image_data': image_base64_str
                }
                payload_bytes = json.dumps(payload).encode('utf-8') # Convert the payload to JSON bytes as Rabbit loves bytes
                print(type(payload_bytes))
                send_to_queue_image(payload_bytes)
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
            
            # JSONify the list of words
            json_data = {str(idx): animal for idx, animal in enumerate(words)}
            json_data['site'] = url
            json_data = json.dumps(json_data)

            send_to_queue_text(json_data)
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
    