import numpy as np
import matplotlib.pyplot as plt

# Number of points
n = 200
NPM = 76

# Generate random x values between 0 and 4π
np.random.seed(NPM)
x = np.random.uniform(0, 4*np.pi, n)

# Original function
y_true = 4 * np.sin(2*x + 0.2)

# Add Gaussian noise
noise = np.random.normal(0, 0.4, n) # mean=0, std=0.5
y_noisy = y_true + noise

# Plot
plt.scatter(x, y_noisy, label="Noisy Data", color="red", alpha=0.6)
plt.plot(np.sort(x), 4*np.sin(4*np.sort(x) + 0.2), label="True Function", color="blue")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

# TUGAS: Temukan kembali fungsi asli dengan interpolasi dari titik-titik data acak (y_noisy)

import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial
from scipy.interpolate import CubicSpline
from scipy.interpolate import UnivariateSpline

n = 200
NPM = 76
np.random.seed(NPM)
x = np.random.uniform(0, 4 * np.pi, n) # titik acak antara 0 s/d 4π
y_true = 4 * np.sin(2*x + 0.2) # fungsi asli sinus
noise = np.random.normal(0, 0.4, n) # gangguan acak
y_noisy = y_true + noise # data asli + noise

# mengurutkan data agar hasil spline lebih halus
sort_idx = np.argsort(x)
x_sorted = x[sort_idx]
y_sorted = y_noisy[sort_idx]

## Cubic Spline Interpolation dari Data Noisy
# membuat cubic spline dari data yang sudah diurutkan
cs = CubicSpline(x_sorted, y_sorted)
# membuat titik x baru dengan 1000 titik yg terdistribusi merata antara 0 dan 4π
# titik-titik ini digunakan untuk evaluasi spline agar kurva yg digambar lebih halus
x_new = np.linspace(0, 4*np.pi, 1000)
# menghitung nilai y pada setiap titik x_new menggunakan fungsi spline
y_cubic = cs(x_new)

# visualisasi hasil cubic spline interpolation
plt.figure(figsize=(10,6))
plt.scatter(x, y_noisy, label="Noisy Data", color="red", alpha=0.4, s=20)
plt.plot(np.sort(x), 4*np.sin(2*np.sort(x) + 0.2), label="True Function", color="blue", linewidth=2)
plt.plot(x_new, y_cubic, label="Cubic Spline Interpolation", color="purple", linestyle="--", linewidth=2)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Cubic Spline Interpolation")
plt.show()

## Smoothing Spline
spline_smooth = UnivariateSpline(x_sorted, y_sorted, s=30)
x_new = np.linspace(0, 4*np.pi, 1000)
y_smooth = spline_smooth(x_new)

# visualisai hasil smoothing spline
plt.figure(figsize=(10,6))
plt.scatter(x, y_noisy, label="Noisy Data", color="red", alpha=0.4, s=30)
plt.plot(np.sort(x), 4*np.sin(2*np.sort(x) + 0.2), label="True Function", color="blue", linewidth=2)
plt.plot(x_new, y_smooth, label="Smoothing Spline", color="green", linestyle="--", linewidth=2)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Smoothing Spline")
plt.show()
