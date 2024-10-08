# src/insulin_pump.py

class InsulinPump:
    def __init__(self, basal_rates, insulin_to_carb_ratio, insulin_sensitivity_factor):
        self.basal_rates = basal_rates  # Taux d'insuline basale par heure
        self.insulin_to_carb_ratio = insulin_to_carb_ratio  # Ratio Insuline/Glucides (ICR)
        self.insulin_sensitivity_factor = insulin_sensitivity_factor  # Facteur de sensibilité (ISF)
    
    def deliver_basal(self, hour):
        """Administre l'insuline basale pour l'heure donnée."""
        return self.basal_rates[hour]
    
    def calculate_meal_bolus(self, carbs):
        """Calcule le bolus alimentaire en fonction des glucides consommés."""
        return carbs / self.insulin_to_carb_ratio
    
    def calculate_correction_bolus(self, current_glucose, target_glucose):
        """Calcule le bolus de correction pour une glycémie élevée."""
        return (current_glucose - target_glucose) / self.insulin_sensitivity_factor
