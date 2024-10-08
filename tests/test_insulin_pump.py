# tests/test_patient.py

import unittest
import sys
import os

# Ajoute le chemin du dossier src à sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from Patient import Patient
from InsulinPump import InsulinPump
from pdm import PDM

class TestInsulinPump(unittest.TestCase):
    def test_basal_insulin_delivery(self):
        # Configuration des paramètres
        initial_glucose = 120  # Glycémie initiale en mg/dL
        insulin_sensitivity = 30
        carb_sensitivity = 5
        basal_rate = 0.8  # Taux basal programmé
        
        # Initialisation des objets
        patient = Patient(initial_glucose, insulin_sensitivity, carb_sensitivity)
        pump = InsulinPump(basal_rates=[basal_rate] * 24, insulin_to_carb_ratio=15, insulin_sensitivity_factor=insulin_sensitivity)
        pdm = PDM(pump, target_glucose=100)

        # Simuler l'administration de l'insuline basale à l'heure 0
        hour = 0
        basal_dose = pump.deliver_basal(hour)
        patient.administer_insulin(basal_dose)

        # Vérifie que le patient a reçu la bonne dose d'insuline
        self.assertEqual(patient.glucose_level, initial_glucose - basal_dose * insulin_sensitivity)
        
        # Vérifie le message d'administration (si implémenté dans la méthode)
        # Pour cela, il faudrait que tu modifies la méthode d'administration d'insuline
        message = f"Insuline basale administrée : {basal_dose} U"
        print(message)  # Simule l'affichage du message

if __name__ == '__main__':
    unittest.main()
