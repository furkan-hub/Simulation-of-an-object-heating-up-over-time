import time
import os
import matplotlib.pyplot as plt

# Simulation time (seconds)
simulation_time = 600  # For example, 10 minutes

# Time step (seconds)
dt = 1  # Update every 1 second

# Initial temperature (Celsius degrees)
initial_temperature = 25

# Mass of the object (kg)
mass = 10

# Heat capacity (Joules / (kg * Celsius degree))
heat_capacity = 100

# Heat source power (Watt)
heat_source_power = 50

# Data organization for plotting
time_data = []  # An empty list to store time data
temperature_data = []  # An empty list to store temperature data

# Create a plot
fig, ax = plt.subplots()
line, = ax.plot(time_data, temperature_data)

# Function to update the graph
def update_graph(time, temperature):
    time_data.append(time)
    temperature_data.append(temperature)

    # Update graph data
    line.set_xdata(time_data)
    line.set_ydata(temperature_data)

    # Update graph limits
    ax.relim()
    ax.autoscale_view()

    # Update the graph window
    plt.draw()
    plt.pause(0.01)

# Set initial values
current_temperature = initial_temperature
time_elapsed = 0

# Simulation loop
while time_elapsed < simulation_time:
    # Calculate friction force (just an example value, can be changed as needed)
    friction_force = 0.1 * current_temperature

    # Calculate heat source power
    heat_source_power = heat_source_power - friction_force

    # Calculate heat transfer
    heat_transfer = heat_source_power * dt

    # Calculate temperature change (using Q = mcΔT formula)
    temperature_change = heat_transfer / (mass * heat_capacity)

    # Update temperature
    current_temperature += temperature_change

    # Update the graph
    update_graph(time_elapsed, current_temperature)
    os.system("cls")  # Clear the terminal screen (use "clear" on Linux)
    
    # Print time and temperature
    print("Time: {} seconds".format(time_elapsed))
    print("Temperature: {} degrees Celsius".format(current_temperature))

    # Update time
    time_elapsed += dt

    # Sleep for a while to match real-time speed
    time.sleep(dt)

# Display the graph when the simulation ends
plt.show()
