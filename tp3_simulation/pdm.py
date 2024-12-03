
class PDM:
    def __init__(self, pump, target_glucose):
        self.pump = pump
        self.target_glucose = target_glucose

    def calculate_bolus(self, carbs):
        return carbs / self.pump.insulin_to_carb_ratio

    def send_bolus_to_pump(self, bolus):
        self.pump.bolus = bolus
        self.pump.administer_bolus()

print("pdm terminée")