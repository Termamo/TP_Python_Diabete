class InsulinPump:
    def __init__(self, basal_rates, insulin_to_carb_ratio, insulin_sensitivity_factor):
        self.basal_rates = basal_rates
        self.insulin_to_carb_ratio = insulin_to_carb_ratio
        self.insulin_sensitivity_factor = insulin_sensitivity_factor
        self.bolus = 0
        self.bolus_delivered = 0

    def administer_bolus(self):
        self.bolus_delivered = self.bolus