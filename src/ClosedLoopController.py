# src/closed_loop_controller.py

class ClosedLoopController:
    def __init__(self, target_glucose, pump, cgm):
        self.target_glucose = target_glucose
        self.pump = pump
        self.cgm = cgm
    
    def adjust_basal_rate(self, patient):
        """Ajuste la délivrance basale en fonction de la glycémie."""
        current_glucose = self.cgm.measure_glucose(patient)
        if current_glucose > self.target_glucose:
            return self.pump.calculate_correction_bolus(current_glucose, self.target_glucose)
        return 0
