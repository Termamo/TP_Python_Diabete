# src/pdm.py

class PDM:
    def __init__(self, pump, target_glucose):
        self.pump = pump
        self.target_glucose = target_glucose
        self.history = []
        self.carbs = 0

    def enter_carbs(self, carbs):
        self.carbs = carbs

    def calculate_bolus(self):
        return self.carbs / self.pump.insulin_to_carb_ratio

    def send_bolus_to_pump(self, bolus):
        self.pump.bolus = bolus

    def confirm_bolus(self):
        message = f"Bolus alimentaire administré : {int(self.pump.bolus_delivered)} U pour {self.carbs} g de glucides"
        self.history.append(message)
        return message
    
