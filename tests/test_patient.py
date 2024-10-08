# tests/test_patient.py

import unittest
from src.Patient import Patient

class TestPatient(unittest.TestCase):
    def test_update_glucose_level(self):
        patient = Patient(initial_glucose=120, insulin_sensitivity=30, carb_sensitivity=5)
        patient.update_glucose_level(2, 50)  # Administrer 2 U d'insuline, consommer 50 g de glucides
        self.assertEqual(patient.glucose_level, 120 - 2 * 30 + 50 * 5)

if __name__ == '__main__':
    unittest.main()
