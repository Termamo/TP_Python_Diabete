
import json
import pika

class CalculationsPlatform:
    def __init__(self, target_glucose, high_threshold, low_threshold, insulin_sensitivity_factor):
        self.target_glucose = target_glucose
        self.high_threshold = high_threshold
        self.low_threshold = low_threshold
        self.insulin_sensitivity_factor = insulin_sensitivity_factor

    def calculate_correction_bolus(self, current_glucose):
        return max(0, (current_glucose - self.target_glucose) / self.insulin_sensitivity_factor)

    def analyze_data(self, glucose_level):
        if glucose_level > self.high_threshold:
            return "ALERT_HIGH", f"Glucose élevé ({glucose_level} mg/dL)"
        elif glucose_level < self.low_threshold:
            return "ALERT_LOW", f"Glucose bas ({glucose_level} mg/dL)"
        else:
            bolus = self.calculate_correction_bolus(glucose_level)
            return "NORMAL", f"Bolus calculé : {bolus} unités"

    def consume_glucose_data(self, queue_name="glucose_data"):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue=queue_name)

        def callback(ch, method, properties, body):
            data = json.loads(body)
            glucose_level = data.get("glucose_level")
            status, message = self.analyze_data(glucose_level)
            print(f"Status: {status}, Message: {message}")

        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        print(f"Waiting for messages on queue: {queue_name}")
        channel.start_consuming()

print("Calculs terminée")