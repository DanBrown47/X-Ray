import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_USER = os.getenv("DB_USER")
RABBITMQ_ENDPOINT = os.getenv("RABBITMQ_ENDPOINT")
RABBITMQ_PORT = os.getenv("RABBITMQ_PORT")
RABBITMQ_TEXT_QUEUE = os.getenv("RABBITMQ_TEXT_QUEUE")
RABBITMQ_TEXT_SCORE = os.getenv("RABBITMQ_TEXT_SCORE")
RABBITMQ_IMAGE_QUEUE = os.getenv("RABBITMQ_IMAGE_QUEUE")
RABBITMQ_IMAGE_SCORE = os.getenv("RABBITMQ_IMAGE_SCORE")

