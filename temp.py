import numpy as np
from risk_factor import helper
hba1c_level,blood_glucose_level = 7.5,220
risk = helper([float(hba1c_level),int(blood_glucose_level)])
print(risk)