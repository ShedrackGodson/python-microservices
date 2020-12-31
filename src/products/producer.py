import pika

params = pika.URLParameters("amqps://ygfxrvwk:pRe_uyBY9BgrDQMbVyYJpn8qOosuVLHx@llama.rmq.cloudamqp.com/ygfxrvwk")

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='main', body='Hello')
