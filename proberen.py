import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
outer_data = pd.read_csv('humerus-177-outer.csv', skiprows=6).to_numpy()
inner_data = pd.read_csv('humerus-177-inner.csv', skiprows=6).to_numpy()

# Extract the coordinates
x_outer, y_outer = outer_data[:, 0], outer_data[:, 1]
x_inner, y_inner = inner_data[:, 0], inner_data[:, 1]

# Plot the outer and inner profiles
plt.figure(figsize=(8, 8))
plt.plot(x_outer, y_outer, label='Outer Profile')
plt.plot(x_inner, y_inner, label='Inner Profile')
plt.xlabel('x (mm)')
plt.ylabel('y (mm)')
plt.legend()
plt.title('Humerus Outer and Inner Profiles')
plt.grid(True)
plt.axis('equal')
plt.show()

# Function to estimate the polar moment of inertia
def polar_moment_inertia(r_func, theta_range):

    Ipol = 0

    for theta in theta_range:

        r = r_func(theta)

        Ipol += r**3 * (theta_range[1] - theta_range[0])  # Integral approximation

    return Ipol

# Estimate the parameters R, a, and b
# These values should be obtained through an iterative process of fitting, here we assume initial guesses
R_outer = 15  # Example guess in mm
a_outer = 0.2  # Example guess
R_inner = 5  # Example guess in mm
a_inner = 0.1  # Example guess

# Define the radius functions
def r_outer(theta):
    return R_outer * (1 + a_outer * np.cos(3 * theta))

def r_inner(theta):
    return R_inner * (1 + a_inner * np.cos(3 * theta))
# Calculate the polar moment of inertia for outer and inner profiles
theta_range = np.linspace(0, 2 * np.pi, 1000)
Ipol_outer = polar_moment_inertia(r_outer, theta_range)
Ipol_inner = polar_moment_inertia(r_inner, theta_range)

# Polar moment of inertia for the hollow humerus
Ipol_hollow = Ipol_outer - Ipol_inner

print(f"Estimated Polar Moment of Inertia for the Hollow Humerus: {Ipol_hollow:.2f} mm^4")
# Calculate the ratio of the triangular and circular profile
# Assuming the circular profile is equivalent in area to the triangular one
R_circular = 15  # Equivalent radius for the circular profile in mm
Ipol_circular = np.pi * (R_circular ** 4) / 2
ratio = Ipol_hollow / Ipol_circular
