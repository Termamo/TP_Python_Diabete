import unittest
import sys
import os

# Ajoutez le chemin du répertoire parent au sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.InsulinPump import InsulinPump
from src.pdm import PDM

class TestPDMConfiguration(unittest.TestCase):

    def test_bolus_alimentaire(self):
        # Initialisation de la pompe et du PDM
        pump = InsulinPump(
            basal_rates=[0.8, 0.6, 0.5, 0.7, 1.0, 1.2, 0.9],
            insulin_to_carb_ratio=10, 
            insulin_sensitivity_factor=50
        )
        pdm = PDM(pump=pump, target_glucose=100)

        # Scénario : Entrée des glucides par le patient
        glucides = 60
        print(f"Patient entre {glucides} g de glucides")
        pdm.enter_carbs(glucides)

        # Scénario : Calcul du bolus alimentaire
        bolus = pdm.calculate_bolus()
        print(f"Bolus calculé : {bolus} U pour {glucides} g de glucides")
        self.assertEqual(bolus, 6)

        # Scénario : Envoi à la pompe à insuline
        pdm.send_bolus_to_pump(bolus)

        # Scénario : Administration du bolus
        pump.administer_bolus()
        print(f"Bolus administré : {pump.bolus_delivered} U")
        self.assertEqual(pump.bolus_delivered, 6)

        # Scénario : Confirmation au patient
        confirmation_message = pdm.confirm_bolus()
        print(confirmation_message)
        self.assertEqual(confirmation_message, "Bolus alimentaire administré : 6 U pour 60 g de glucides")

        # Scénario : Enregistrement de la dose
        self.assertIn("Bolus alimentaire administré : 6 U pour 60 g de glucides", pdm.history)

if __name__ == '__main__':
    unittest.main()