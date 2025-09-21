import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 500)
dx = x[1] - x[0]

f = np.sin(x) + 0.5*np.sin(2*x) + (1/3)*np.sin(3*x) + (1/4)*np.sin(4*x) + (1/5)*np.sin(5*x)

# (a) Hitung turunan f(x)
f_prime = np.gradient(f, dx)
print(f_prime[:5])

# (b) Hitung integral kumulatif f(x)
F = np.cumsum(f)*dx
print(F[:5])

# (c) Hitung secara terpisah bagian integral di atas dan di bawah y=0
F_pos = np.cumsum(np.where(f>0, f, 0)) * dx
F_neg = np.cumsum(np.where(f<0, 1, 0)) * dx
print(F_pos[:5])
print(F_neg[:5])

plt.figure(figsize=(12,8))

# Plot fungsi asli dengan area positif/negatif
plt.subplot(3,1,1)
plt.plot(x, f, label="f(x)", linewidth=2)
plt.fill_between(x, f, 0, where=f>=0, color="skyblue", alpha=0.5, label="Area +")
plt.fill_between(x, f, 0, where=f<0, color="salmon", alpha=0.5, label="Area -")
plt.axhline(0, color='black', linestyle='--', alpha=0.7)
plt.title("Fungsi f(x)")
plt.legend()

# Plot turunan f(x)
plt.subplot(3,1,2)
plt.plot(x, f_prime, color="orange", label="f'(x)")
plt.axhline(0, color='black', linestyle='--', alpha=0.7)
plt.title("Turunan f(x) (f'(x))")
plt.legend()

# Plot integral F(x)
plt.subplot(3,1,3)
plt.plot(x, F, color="green", label="F(x)")
plt.fill_between(x, F_pos, 0, color="lightgreen", alpha=0.3, label="Integral +")
plt.fill_between(x, F_neg, 0, color="pink", alpha=0.3, label="Integral -")
plt.axhline(0, color='black', linestyle='--', alpha=0.7)
plt.title("Integral f(x)")
plt.legend()

plt.tight_layout()
plt.show()
