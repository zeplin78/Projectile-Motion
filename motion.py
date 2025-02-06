import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # Gravity (m/s²)
rho = 1.225  # Air density (kg/m³) (at sea level)
dt = 0.01  # Time step for numerical integration

# Function to calculate projectile motion without air resistance
def projectile_no_air(v0, angle):
    angle_rad = np.radians(angle)

    v0x = v0 * np.cos(angle_rad)
    v0y = v0 * np.sin(angle_rad)

    t_flight = (2 * v0y) / g
    t = np.linspace(0, t_flight, num=100)

    x = v0x * t
    y = v0y * t - 0.5 * g * t**2

    return x, y, t_flight

# Function to calculate projectile motion with air resistance using Euler's method
def projectile_with_air(v0, angle, Cd, mass, A):
    angle_rad = np.radians(angle)

    # Initial velocity components
    vx, vy = v0 * np.cos(angle_rad), v0 * np.sin(angle_rad)

    # Initialize position and time
    x, y = [0], [0]
    t = 0

    while y[-1] >= 0:
        # Speed and drag force
        v = np.sqrt(vx**2 + vy**2)
        F_drag = 0.5 * Cd * rho * A * v**2

        # Acceleration components
        ax = -F_drag * (vx / v) / mass
        ay = -g - (F_drag * (vy / v) / mass)

        # Update velocity using Euler's method
        vx += ax * dt
        vy += ay * dt

        # Update position
        x.append(x[-1] + vx * dt)
        y.append(y[-1] + vy * dt)

        # Update time
        t += dt

    return np.array(x), np.array(y)

# User inputs
v0 = float(input("Enter initial velocity (m/s): "))
angle = float(input("Enter launch angle (degrees): "))
air_resistance = input("Include air resistance? (yes/no): ").strip().lower()

if air_resistance == "yes":
    Cd = float(input("Enter drag coefficient (Cd) (default ~0.47 for a sphere): "))
    mass = float(input("Enter object mass (kg): "))
    A = float(input("Enter cross-sectional area (m²): "))

# Get trajectory data
x_no_air, y_no_air, t_flight = projectile_no_air(v0, angle)

if air_resistance == "yes":
    x_air, y_air = projectile_with_air(v0, angle, Cd, mass, A)

# Plot the projectile motion
plt.figure(figsize=(8, 5))
plt.plot(x_no_air, y_no_air, label="Without Air Resistance", linestyle="dashed", color="blue")
if air_resistance == "yes":
    plt.plot(x_air, y_air, label="With Air Resistance", color="red")
plt.axhline(y=0, color='black', linewidth=1)  # Ground line
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.title(f"Projectile Motion (v0={v0} m/s, angle={angle}°)")
plt.legend()
plt.grid()
plt.show()

# Display results
print(f"Time of Flight (No Air Resistance): {t_flight:.2f} seconds")
if air_resistance == "yes":
    print(f"Range (With Air Resistance): {x_air[-1]:.2f} meters")
    print(f"Range (No Air Resistance): {x_no_air[-1]:.2f} meters")
