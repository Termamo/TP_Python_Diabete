# src/simulator.py

class Simulator:
    def __init__(self, patient, pump, cgm, controller, pdm, duration):
        self.patient = patient
        self.pump = pump
        self.cgm = cgm
        self.controller = controller
        self.pdm = pdm
        self.duration = duration  # Durée de la simulation en heures
        self.log = []
    
    def run_simulation(self):
        """Exécute la simulation sur la durée spécifiée."""
        for hour in range(self.duration):
            # Administrer l'insuline basale
            basal_dose = self.pump.deliver_basal(hour % 24)
            self.patient.administer_insulin(basal_dose)
            
            # Mesurer la glycémie et ajuster si nécessaire
            correction_dose = self.controller.adjust_basal_rate(self.patient)
            if correction_dose > 0:
                self.patient.administer_insulin(correction_dose)
            
            # Enregistrer l'état de la simulation
            self.log_data(hour)
    
    def log_data(self, hour):
        """Enregistre les données de la simulation."""
        glucose = self.patient.glucose_level
        self.log.append(f"Heure {hour}: Glycémie = {glucose} mg/dL")
