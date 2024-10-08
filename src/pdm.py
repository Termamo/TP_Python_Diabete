# src/pdm.py

class PDM:
    def __init__(self, pump, target_glucose):
        self.pump = pump
        self.target_glucose = target_glucose
        self.history = []

    def apply_new_config(self, config):
        if 'basal_rates' in config:
            self.pump.basal_rates = config['basal_rates']
            self.history.append("Taux basaux configurés avec succès")
        if 'insulin_to_carb_ratio' in config:
            self.pump.insulin_to_carb_ratio = config['insulin_to_carb_ratio']
            self.history.append("Ratio insuline/glucides configuré avec succès")