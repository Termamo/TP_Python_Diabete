# src/pdm.py

class PDM:
    def __init__(self, pump, target_glucose):
        self.pump = pump
        self.target_glucose = target_glucose
        self.history = []

    def set_meal(self, carbs):
        """Programmer un bolus pour un repas."""
        bolus = self.pump.calculate_meal_bolus(carbs)
        self.history.append(f"Bolus alimentaire: {bolus} U pour {carbs} g de glucides")
        return bolus

    def set_correction(self, current_glucose):
        """Programmer un bolus de correction."""
        bolus = self.pump.calculate_correction_bolus(current_glucose, self.target_glucose)
        self.history.append(f"Bolus de correction: {bolus} U")
        return bolus
