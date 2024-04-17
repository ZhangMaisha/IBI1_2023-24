# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
#Set the size and resolution of the plot
plt.figure(figsize=(6, 4), dpi=150)
N=10000 # total population
beta=0.3 # Rate of disease transmission
gamma=0.05 # recovery rate
vaccination_rates=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9,1.0]  
# Create a normalized object to map vaccination_rates to[0, 1]
norm = plt.Normalize(min(vaccination_rates), max(vaccination_rates))  
for vaccination_rate in vaccination_rates:  
    if vaccination_rate == 1.0:  
        # 直接绘制没有感染者的曲线  
        I_history = [0] * 1000  
        plt.plot(range(len(I_history)), I_history, label='100%', color = cm.viridis(norm(vaccination_rate)))  
        continue  
   # Initialize
    S = N - int(N * vaccination_rate) - 1  
    I = 1   
    R = 0  
    V = int(N * vaccination_rate)  
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
  # Plot the number of infected people over time
    plt.plot(range(len(I_history)), I_history, label=f'{vaccination_rate*100:.0f}%',color = cm.viridis(norm(vaccination_rate)))
# Set the X-axis label
plt.xlabel('time')
# Set the Y-axis label
plt.ylabel('number of people')
# Set the title of the figure
plt.title('SIR Model with different vaccination rates')
# Show the legend
plt.legend()
# Show the figure
plt.show()