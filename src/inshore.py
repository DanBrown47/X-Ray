import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost')) #TODO : move the localhost to env,
channel = connection.channel()

im_res_queue = 'image_result_queue' #TODO : move this to env
txt_res_queue = 'text_result_queue' #TODO : move this to env
channel.queue_declare(queue=txt_res_queue)
channel.queue_declare(queue=im_res_queue)

def callback(ch, method, properties, body):
    # Callback function to process the received message
    print(f"Received message from {method.routing_key}: {body}")

def consume_from_queue():
    channel.basic_consume(queue=txt_res_queue, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


