import numpy as np
import matplotlib.pyplot as plt

# Physical constants
h = 6.626e-34   # Planck's constant, J*s
c = 3e8         # Speed of light, m/s
k = 1.381e-23   # Boltzmann constant, J/K

def planck(wavelength, T):
    """Spectral radiance of a blackbody at temperature T (K). 
       Wavelength in meters, output W/sr/m^3
    """
    a = 2.0*h*c**2
    b = h*c / (wavelength*k*T)
    intensity = a / ( (wavelength**5) * (np.exp(b) - 1.0) )
    return intensity

# Wavelength range (100 nm to 3000 nm)
wavelengths = np.linspace(100e-9, 3000e-9, 500)

# Example temperature (e.g. 5800 K, Sun-like)
T = 5800
intensity = planck(wavelengths, T)

# Plot
plt.figure(figsize=(8,5))
plt.plot(wavelengths*1e9, intensity, label=f"{T} K")
plt.xlabel("Wavelength (nm)")
plt.ylabel("Spectral Radiance (W·sr⁻¹·m⁻³)")
plt.title("Blackbody Radiation Curve")
plt.legend()
plt.grid(True)
plt.show()
