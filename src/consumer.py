import pika
from dotenv import load_dotenv
import os

load_dotenv('.env')

params = pika.URLParameters(os.getenv('AMQP_URL'))

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print("Received in admin")
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print("Started consuming")

channel.start_consuming()

channel.close()
