import pika
import json
import streamlit as st
from config import RABBITMQ_ENDPOINT, RABBITMQ_TEXT_QUEUE, RABBITMQ_IMAGE_QUEUE
connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_ENDPOINT)) 
channel = connection.channel()

# Declare a queue
queue_name_txt = RABBITMQ_TEXT_QUEUE
channel.queue_declare(queue=queue_name_txt)

queue_name = RABBITMQ_IMAGE_QUEUE
channel.queue_declare(queue=queue_name)

def send_to_queue_text(data):
    try:
        channel.basic_publish(exchange='',
                        routing_key=queue_name_txt,
                        body=data
                        )
        
        print(f" [x] Sent data to {queue_name_txt}")
    except Exception as e:
        print(f"Error sending data to queue: {str(e)}")
        return False

    return True

def send_to_queue_image(data):
    # json_data = json.dumps(data)
    try:
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body=data)
        print(f" [x] Sent data to {queue_name}")
    except Exception as e:
        print(f"Error sending data to queue: {queue_name} error is  {str(e)}")
        return False
    
    return True