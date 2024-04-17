# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
N = 10000 # total population
S = N-1 # number of initially susceptible individuals
I = 1 # initial number of infected persons
R = 0 # Number of initial rehabbers
beta = 0.3 # Rate of disease transmission
gamma = 0.05 # recovery rate
# Create a array to record the status at each time point
S_history = [S]
I_history = [I]
R_history = [R]
# Iterate over each time point
for t in range(1000):
    # To calculate the proportion of current infected persons in the total population
    infected_fraction = I / N
    # Calculate the probability of infection for each susceptible person
    infection_probability = beta * infected_fraction
    # Randomly select susceptible individuals to become infected
    new_infected = np.random.choice([0, 1], size=S, p=[1 - infection_probability, infection_probability]) 
    S-= new_infected.sum()
    I+= new_infected.sum()
    # Randomly select infected people to become survivors
    new_recovered = np.random.choice([0, 1], size=I, p=[1 - gamma, gamma])  
    I-= new_recovered.sum()
    R+= new_recovered.sum()
    # Record the status at the current time point
    S_history.append(S)
    I_history.append(I)
    R_history.append(R)
#Set the size and resolution of the plot
plt.figure(figsize=(6, 4), dpi=150)
# Plot the number of susceptible individuals over time
plt.plot(range(len(S_history)), S_history, label='Susceptible')
# Plot the number of infected people over time
plt.plot(range(len(I_history)), I_history, label='Infected')
# Plot the number of recovered people over time
plt.plot(range(len(R_history)), R_history, label='Recovered')
# Set the X-axis label
plt.xlabel('Time')
# Set the Y-axis label
plt.ylabel('Number of people')
# Set the title of the figure
plt.title('SIR Model')
# Show the legend
plt.legend()
# Show the figure
plt.show()