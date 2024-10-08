# src/main.py

from src.Patient import Patient
from src.InsulinPump import InsulinPump
from src.cgm import CGM
from src.ClosedLoopController import ClosedLoopController
from src.pdm import PDM
from src.Simulator import Simulator

def main():
    # Initialisation des paramètres
    initial_glucose = 150  # Glycémie initiale en mg/dL
    insulin_sensitivity = 30  # Sensibilité à l'insuline (ISF)
    carb_sensitivity = 5  # Sensibilité aux glucides (SCF)
    
    basal_rates = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # Taux d'insuline basale
    insulin_to_carb_ratio = 15  # Ratio Insuline/Glucides
    target_glucose = 100  # Glycémie cible en mg/dL
    
    # Création des objets
    patient = Patient(initial_glucose, insulin_sensitivity, carb_sensitivity)
    pump = InsulinPump(basal_rates, insulin_to_carb_ratio, insulin_sensitivity)
    cgm = CGM(measurement_interval=5)  # Mesure toutes les 5 minutes
    controller = ClosedLoopController(target_glucose, pump, cgm)
    pdm = PDM(pump, target_glucose)
    
    # Durée de la simulation (en heures)
    duration = 24  # Simuler sur 24 heures

    # Création et exécution de la simulation
    simulator = Simulator(patient, pump, cgm, controller, pdm, duration)
    simulator.run_simulation()
    
    # Affichage des résultats de la simulation
    for log_entry in simulator.log:
        print(log_entry)

if __name__ == "__main__":
    main()
