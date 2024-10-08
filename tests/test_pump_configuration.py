import unittest
import sys
import os

# Ajoutez le chemin du répertoire parent au sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.InsulinPump import InsulinPump

class TestPumpConfiguration(unittest.TestCase):
    def test_pump_configuration(self):
        # Configuration de la pompe avec des paramètres spécifiques
        pump = InsulinPump(
            basal_rates=[0.8, 0.6, 0.5, 0.7, 1.0, 1.2, 0.9], 
            insulin_to_carb_ratio=10, 
            insulin_sensitivity_factor=50
        )
        
        # Vérification des taux basaux
        self.assertEqual(pump.basal_rates[0], 0.8)
        self.assertEqual(pump.basal_rates[5], 1.2)
        
        # Vérification du ratio insuline/glucides
        self.assertEqual(pump.insulin_to_carb_ratio, 10)
        
        # Vérification du facteur de sensibilité à l'insuline
        self.assertEqual(pump.insulin_sensitivity_factor, 50)

if __name__ == '__main__':
    unittest.main()