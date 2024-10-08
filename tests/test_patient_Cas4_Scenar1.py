# tests/test_patient.py

import unittest
import sys
import os

# Ajoute le chemin du dossier src à sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from Patient import Patient
from InsulinPump import InsulinPump
from cgm import CGM
from ClosedLoopController import ClosedLoopController

class TestInsulinPump(unittest.TestCase):
    def test_corrective_bolus_delivery(self):
        # Configuration des paramètres
        current_glucose = 250  # Glycémie mesurée en mg/dL
        target_glucose = 100  # Glycémie cible en mg/dL
        insulin_sensitivity_factor = 40  # ISF en mg/dL par unité
        
        # Initialisation des objets
        patient = Patient(initial_glucose=current_glucose, insulin_sensitivity=insulin_sensitivity_factor, carb_sensitivity=5)
        pump = InsulinPump(basal_rates=[0.0] * 24, insulin_to_carb_ratio=15, insulin_sensitivity_factor=insulin_sensitivity_factor)
        cgm = CGM(measurement_interval=5)  # Capteur mesurant toutes les 5 minutes
        controller = ClosedLoopController(target_glucose, pump, cgm)

        # Calculer le bolus de correction
        correction_bolus = pump.calculate_correction_bolus(current_glucose, target_glucose)
        patient.administer_insulin(correction_bolus)

        # Vérifie que la dose de correction est correcte
        self.assertAlmostEqual(correction_bolus, 3.75, places=2)  # Vérifie que le bolus de correction est bien de 3.75 U
        
        # Vérifie le message d'administration
        message = f"Bolus de correction administré : {correction_bolus} U"
        print(message)  # Simule l'affichage du message

if __name__ == '__main__':
    unittest.main()
