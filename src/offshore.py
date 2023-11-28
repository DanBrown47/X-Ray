import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost')) #TODO : move the localhost to env,
channel = connection.channel()

# Declare a queue
queue_name_txt = 'text_queue' #TODO : move this to env
channel.queue_declare(queue=queue_name_txt)

queue_name = 'image_queue' #TODO : move this to env
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