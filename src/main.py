from Patient import Patient
from InsulinPump import InsulinPump
from cgm import CGM
from ClosedLoopController import ClosedLoopController
from pdm import PDM
from Simulator import Simulator

# Initialiser les composants
patient = Patient(initial_glucose=120, insulin_sensitivity=30, carb_sensitivity=5)
pump = InsulinPump(basal_rates=[0.8, 0.6, 0.5, 0.7, 1.0, 1.2, 0.9, 0.8, 0.6, 0.5, 0.7, 1.0, 1.2, 0.9, 0.8, 0.6, 0.5, 0.7, 1.0, 1.2, 0.9,0.8, 0.6, 0.5], insulin_to_carb_ratio=10, insulin_sensitivity_factor=50)
cgm = CGM(measurement_interval=5)
controller = ClosedLoopController(target_glucose=100, pump=pump, cgm=cgm)
pdm = PDM(pump=pump, target_glucose=100)

# Configurer la simulation
simulator = Simulator(patient, pump, cgm, controller, pdm, duration=24)

# Lancer la simulation
simulator.run_simulation()

# Afficher les résultats
for log_entry in simulator.log:
    print(log_entry)
