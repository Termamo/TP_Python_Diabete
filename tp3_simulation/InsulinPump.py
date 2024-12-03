
class InsulinPump:
    def __init__(self, basal_rates, insulin_to_carb_ratio, insulin_sensitivity_factor):
        self.basal_rates = basal_rates
        self.insulin_to_carb_ratio = insulin_to_carb_ratio
        self.insulin_sensitivity_factor = insulin_sensitivity_factor
        self.bolus = 0

    def deliver_basal(self, hour):
        return self.basal_rates[hour]

    def administer_bolus(self):
        print(f"Bolus administered: {self.bolus} units")

    def calculate_correction_bolus(self, current_glucose, target_glucose):
        return max(0, (current_glucose - target_glucose) / self.insulin_sensitivity_factor)

print("Insulin Pump terminée")