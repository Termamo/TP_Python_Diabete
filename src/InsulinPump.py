class InsulinPump:
    def __init__(self, basal_rates, insulin_to_carb_ratio, insulin_sensitivity_factor):
        self.basal_rates = basal_rates
        self.insulin_to_carb_ratio = insulin_to_carb_ratio
        self.insulin_sensitivity_factor = insulin_sensitivity_factor
        self.bolus = 0
        self.bolus_delivered = 0


    def deliver_basal(self, hour):
        """Administre l'insuline basale pour l'heure donnée."""
        return self.basal_rates[hour]
    def administer_bolus(self):
        self.bolus_delivered = self.bolus

    def calculate_correction_bolus(self, current_glucose, target_glucose):
        """Calcule le bolus de correction pour ramener la glycémie à la cible."""
        return (current_glucose - target_glucose) / self.insulin_sensitivity_factor    