import matplotlib.pyplot as plt
import random
import math

# initial variables
radius = 1
total_trials = int(input("Enter the number of trials for Pi approximation: "))
in_circle = 0
inst_approx = []

# Set up the plot
plt.figure(figsize=(7,7))

# Generate points within the circle and outside the circle using a uniform random distribution
for i in range(1, total_trials + 1):
    x = random.uniform(-radius, radius)
    y = random.uniform(-radius, radius)

    if (x**2 + y**2) <= radius**2:
        in_circle += 1
        plt.scatter(x, y, color='red', s=5) # Point inside the circle 
    else:
        plt.scatter(x, y, color='green', s=5)  # Point outside the circle
    
    # store the instantaneous approximation of Pi
    inst_approx.append((in_circle / i) * 4)

# Calculate the approximation of Pi 
print(f"Approximation of Pi after {total_trials} trials is: {(in_circle / total_trials) * 4}")

# Calculate the confidence level in percentage and the margin of error by comparing the approximated Pi with the actual value of Pi
print(f'Accuracy level: {inst_approx[-1] * 100 / math.pi}%')
print(f'Margin of error: {(math.pi - inst_approx[-1]) / math.pi}%')

# Plot the Monte Carlo simulation results
plt.title("Monte Carlo Simulation for Pi Approximation")
plt.legend([f'Dots inside the circle: {in_circle} to a total number of trials: {total_trials }'], loc='upper right')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()