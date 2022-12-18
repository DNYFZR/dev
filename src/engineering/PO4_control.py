# Phosphate Control - Chemical Dosing
import numpy as np

class PhosphateController:
    def __init__(self, flowrates: np.array, solids_mgl: np.array, max_limit: float,
                p_in_mgl: np.array, p_out_mgl: np.array,p_target_mgl: float, ) -> None:
        
        self.flow = flowrates
        self.solids = solids_mgl
        
        self.p_in = p_in_mgl
        self.p_out = p_out_mgl

        self.target = p_target_mgl
        self.limit = max_limit


    def control(self):
        pass