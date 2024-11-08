import numpy as np
import pandas as pd
from pykrige.ok import OrdinaryKriging
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Membaca dataset
data = pd.read_csv('data_training.csv')

# Menampilkan beberapa baris pertama untuk melihat struktur data
print(data.head())

# Menyimpan fitur dan target
X = data[['latitute', 'longitude']]  # Lokasi
y = data[['COD2023', 'COD2024', 'BOD2023', 'BOD2024']]  # Kualitas air

scaler = StandardScaler()
y_scaled = scaler.fit_transform(y)

def fit_kriging_model(X, y, parameter):
    OK = OrdinaryKriging(
        X['longitude'], X['latitute'], y[parameter],
        variogram_model='spherical', verbose=True, enable_plotting=False
    )
    return OK

# Membuat model Kriging untuk setiap parameter
kriging_models = {}
parameters = ['COD2023', 'COD2024', 'BOD2023', 'BOD2024']

for param in parameters:
    kriging_models[param] = fit_kriging_model(X, data, param)

print(data.dtypes)

def predict_quality(latitute, longitude):
    predicted_values = {}
    for param in parameters:
        z, ss = kriging_models[param].execute('points', [longitude], [latitute])
        predicted_values[param] = z[0]  # Ambil nilai prediksi

    # Mengembalikan nilai yang diprediksi
    return predicted_values

# Contoh penggunaan
latitute_input = -6.1751
longitude_input = 106.8650

predicted_quality = predict_quality(latitute_input, longitude_input)
print(predicted_quality)

def fit_kriging_model(X, y, parameter):
    OK = OrdinaryKriging(
        X['longitude'], X['latitute'], y[parameter],
        variogram_model='spherical', verbose=True, enable_plotting=False
    )
    return OK

# Membuat model Kriging untuk setiap parameter
kriging_models = {}
parameters = ['COD2023', 'COD2024', 'BOD2023', 'BOD2024']

for param in parameters:
    kriging_models[param] = fit_kriging_model(data[['latitute', 'longitude']], data, param)

def predict_quality(latitute, longitude):
    predicted_values = {}
    for param in parameters:
        # Eksekusi model Kriging
        z, ss = kriging_models[param].execute('points', [longitude], [latitute])
        predicted_values[param] = z[0]

    return predicted_values

# Contoh penggunaan
latitute_input = -6.1751
longitude_input = 106.8650

predicted_quality = predict_quality(latitute_input, longitude_input)
print(predicted_quality)

latitute_input = -7.942
longitude_input = 110.371

predicted_quality = predict_quality(latitute_input, longitude_input)
print(predicted_quality)
