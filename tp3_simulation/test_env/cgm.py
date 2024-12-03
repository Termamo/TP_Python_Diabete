
import pika
import json

class CGM:
    def __init__(self):
        self.current_glucose = None

    def publish_glucose(self, glucose_level, queue_name="glucose_data"):
        self.current_glucose = glucose_level
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue=queue_name)

        message = {"glucose_level": glucose_level}
        channel.basic_publish(exchange='', routing_key=queue_name, body=json.dumps(message))
        print(f"Published glucose level: {glucose_level}")
        connection.close()


print("cgm terminée")