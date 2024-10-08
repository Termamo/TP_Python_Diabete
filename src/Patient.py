# src/patient.py

class Patient:
    def __init__(self, initial_glucose, insulin_sensitivity, carb_sensitivity):
        self.glucose_level = initial_glucose  # Glycémie actuelle
        self.insulin_sensitivity = insulin_sensitivity  # Sensibilité à l'insuline (ISF)
        self.carb_sensitivity = carb_sensitivity  # Sensibilité aux glucides (SCF)
    
    def update_glucose_level(self, insulin_dose, carbs):
        """Met à jour la glycémie en fonction de l'insuline et des glucides consommés."""
        self.glucose_level -= insulin_dose * self.insulin_sensitivity
        self.glucose_level += carbs * self.carb_sensitivity
    
    def add_carbs(self, carbs):
        """Ajoute des glucides et met à jour la glycémie."""
        self.update_glucose_level(0, carbs)
    
    def administer_insulin(self, insulin_dose):
        """Administre une dose d'insuline et met à jour la glycémie."""
        self.update_glucose_level(insulin_dose, 0)
