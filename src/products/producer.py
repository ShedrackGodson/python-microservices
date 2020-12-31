import pika, json

params = pika.URLParameters("amqps://ygfxrvwk:pRe_uyBY9BgrDQMbVyYJpn8qOosuVLHx@llama.rmq.cloudamqp.com/ygfxrvwk")

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
