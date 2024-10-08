import unittest
import sys
import os

# Ajoutez le chemin du répertoire parent au sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.InsulinPump import InsulinPump
from src.pdm import PDM

class TestPDMConfiguration(unittest.TestCase):

    def test_basal_rates_configuration(self):
        # Initialisation de la pompe et du PDM
        pump = InsulinPump(
            basal_rates=[0.0] * 24,  # Taux basaux vides pour commencer
            insulin_to_carb_ratio=10, 
            insulin_sensitivity_factor=50
        )
        pdm = PDM(pump=pump, target_glucose=100)

        # Configuration des taux basaux par heure
        new_basal_rates = [0.8, 0.6, 0.5, 0.7, 1.0, 1.2, 0.9, 0.8] + [0.0] * 16
        print(f"Applying new basal rates: {new_basal_rates}")
        pdm.apply_new_config({"basal_rates": new_basal_rates})

        # Vérification que les taux basaux ont été appliqués
        print(f"Basal rates after configuration: {pump.basal_rates[:8]}")
        self.assertEqual(pump.basal_rates[:8], [0.8, 0.6, 0.5, 0.7, 1.0, 1.2, 0.9, 0.8])

        # Message de succès
        success_message = "Taux basaux configurés avec succès"
        print(f"History after configuration: {pdm.history}")
        self.assertIn(success_message, pdm.history)

    def test_icr_configuration(self):
        # Initialisation de la pompe et du PDM
        pump = InsulinPump(
            basal_rates=[0.8, 0.6, 0.5, 0.7, 1.0, 1.2, 0.9],
            insulin_to_carb_ratio=10, 
            insulin_sensitivity_factor=50
        )
        pdm = PDM(pump=pump, target_glucose=100)

        # Configuration du ratio insuline/glucides
        new_icr = 12
        print(f"Applying new insulin to carb ratio: {new_icr}")
        pdm.apply_new_config({"insulin_to_carb_ratio": new_icr})

        # Vérification que le ratio insuline/glucides a été appliqué
        print(f"Insulin to carb ratio after configuration: {pump.insulin_to_carb_ratio}")
        self.assertEqual(pump.insulin_to_carb_ratio, new_icr)

if __name__ == '__main__':
    unittest.main()