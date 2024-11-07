import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pykrige.ok import OrdinaryKriging

datatraining = pd.read_csv('data_training.csv')
datatraining

# Extract the necessary columns
latitude = datatraining['latitute'].values
longitude = datatraining['longitude'].values
value = datatraining['COD2024'].values

datatesting = pd.read_csv('data_testing.csv')
datatesting

# Extract the necessary columns
gridy = datatesting['latitute'].values
gridx= datatesting['longitude'].values

"""**Prediksi dengan Ordinary Kriging**"""

# Perform Ordinary Kriging using the spherical variogram model
OK = OrdinaryKriging(longitude,
                     latitute,
                     value,
                     variogram_model='spherical',
                     coordinates_type='geographic',
                     verbose=True,
                     enable_plotting=True)

# Hasil interpolasi Kriging untuk 10 data testing
z_interp, ss = OK.execute('points', gridx, gridy)
pd.DataFrame(z_interp)
