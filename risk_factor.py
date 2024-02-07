import numpy as np

def helper(cols):
  if cols[0]>=6.5 and cols[1]>=200:
    return 9
  elif cols[0]>=6.5 and cols[1]<200 and cols[1]>=140:
    return 8
  elif cols[0]>=6.5 and cols[1]<140:
    return 7
  elif cols[0]<6.5 and cols[0]>=5.7 and cols[1]>=200:
    return 6
  elif cols[0]<6.5 and cols[0]>=5.7 and cols[1]<200 and cols[1]>=140:
    return 5
  elif cols[0]<6.5 and cols[0]>=5.7 and cols[1]<140:
    return 4
  elif cols[0]<5.7 and cols[1]>=200:
    return 3
  elif cols[0]<5.7 and cols[1]<200 and cols[1]>=140:
    return 2
  elif cols[0]<5.7 and cols[1]<140:
    return 1
  else:
    return np.nan