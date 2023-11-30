import streamlit as st
from src.models import get_from_db_all_values, update_db
import pika
import json

from config import RABBITMQ_ENDPOINT, RABBITMQ_TEXT_SCORE, RABBITMQ_IMAGE_SCORE
# Add a button to the app
connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_ENDPOINT)) #TODO : move the localhost to env,
channel = connection.channel()


    

def get_queue_size(queue_name):
    queue_info = channel.queue_declare(queue=queue_name, passive=True)
    queue_size = queue_info.method.message_count
    return queue_size

result = get_from_db_all_values()
st.dataframe(result)

def get_all_messages(queue):
    messages = []
    while True:
        method_frame, header_frame, body = channel.basic_get(queue=queue, auto_ack=False)
        if method_frame:
            messages.append(body.decode('utf-8'))
            # Acknowledge the message to remove it from the queue
            channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        else:
            break
    return messages

def see_txt_callback(ch, method, properties, body):
    print(body)

# Add a button to the app
if st.button("Re-scan"):
    st.write("Updating the SQL DB")
    txt_queue_size = get_queue_size(RABBITMQ_TEXT_SCORE) #TODO : move this to env
    img_queue_size = get_queue_size(RABBITMQ_IMAGE_SCORE) #TODO : move this to env
    st.write(str(txt_queue_size)+" Text(s) are in the queue")
    st.write(str(img_queue_size)+" Image(s) are in the queue")


    txt_messages = get_all_messages(RABBITMQ_TEXT_SCORE)
    for message in txt_messages:
        message = json.loads(message)
        # st.write(type(message))
        # st.write(messages)
        site = message['url']
        score = message['score']
        print(site, score)
        update_db(site, score, "text_value")
    
    img_messages = get_all_messages(RABBITMQ_IMAGE_SCORE)
    for message in img_messages:
        message = json.loads(message)
        site = message['url']
        score = message['score']
        print(site, score)
        update_db(site, score, "image_value")



