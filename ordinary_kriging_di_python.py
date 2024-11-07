import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pykrige.ok import OrdinaryKriging

datatraining = pd.read_csv('https://drive.google.com/file/d/1q5mNLxlUX1vmIri2JM9jXzBQxHOR5Gv2/view?usp=sharing')
datatraining

# Extract the necessary columns
latitude = datatraining['Latitute'].values
longitude = datatraining['Longtitute'].values
value = datatraining['COD 2024'].values

datatesting = pd.read_excel('https://docs.google.com/spreadsheets/d/1zfQoGmkmHhDqnGVIIRgK7Tu4muQBcM5Z/edit?usp=sharing&ouid=118433922064170523803&rtpof=true&sd=true')
datatesting

# Extract the necessary columns
gridy = datatesting['Latitute'].values
gridx= datatesting['Longtitute'].values

"""**Prediksi dengan Ordinary Kriging**"""

# Perform Ordinary Kriging using the spherical variogram model
OK = OrdinaryKriging(longitude,
                     latitude,
                     value,
                     variogram_model='spherical',
                     coordinates_type='geographic',
                     verbose=True,
                     enable_plotting=True)

# Hasil interpolasi Kriging untuk 10 data testing
z_interp, ss = OK.execute('points', gridx, gridy)
pd.DataFrame(z_interp)
