# src/cgm.py

class CGM:
    def __init__(self, measurement_interval):
        self.measurement_interval = measurement_interval  # Intervalle de mesure (en minutes)
        self.current_glucose = None  # Dernière valeur mesurée
    
    def measure_glucose(self, patient):
        """Mesure la glycémie actuelle du patient."""
        self.current_glucose = patient.glucose_level
        return self.current_glucose
