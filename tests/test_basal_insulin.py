import unittest
import sys
import os

# Ajoutez le chemin du répertoire parent au sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.Patient import Patient
from src.InsulinPump import InsulinPump

class TestBasalInsulin(unittest.TestCase):
    def test_basal_insulin(self):
        # Initialiser le patient avec une glycémie initiale
        patient = Patient(initial_glucose=120, insulin_sensitivity=30, carb_sensitivity=5)
        pump = InsulinPump(
            basal_rates=[0.8, 0.6, 0.5, 0.7, 1.0, 1.2, 0.9], 
            insulin_to_carb_ratio=10, 
            insulin_sensitivity_factor=50
        )
        
        # Administrer l'insuline basale à une heure donnée
        insulin_dose = pump.deliver_basal(2)  # Insuline basale à l'heure 2
        patient.administer_insulin(insulin_dose)
        
        # Vérification que la glycémie a été mise à jour correctement
        self.assertEqual(patient.glucose_level, 120 - insulin_dose * 30)

if __name__ == '__main__':
    unittest.main()