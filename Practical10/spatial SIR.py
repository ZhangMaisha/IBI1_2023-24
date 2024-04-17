# import necessary libraries
import numpy as np
import matplotlib . pyplot as plt
# make array of all susceptible population
population = np.zeros((100,100))
outbreak = np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]] = 1
# plot a heat map
plt.figure(figsize = (6, 4), dpi = 150)
plt.subplot(2, 2, 1)
plt.imshow(population, cmap = 'viridis', interpolation = 'nearest')
# define the basic variables of the model
beta = 0.3
gamma = 0.05
# time course
for j in range(1, 101):
   # find infected points
    infectedIndex = np.where(population==1)
    # loop through all infected points
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        # infect each neighbour with probability beta
      # infect all 8 neighbours (this is a bit finicky, is there a better way?):
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                # don't infect yourself! (Is this strictly necessary?)
                if (xNeighbour,yNeighbour) != (x,y):
                    # make sure I don't fall off an edge
                   if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        # only infect neighbours that are not already infected!
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
        # recover
        RecoveredIndex = np.where(population == 1)  
    for k in range(len(RecoveredIndex[0])):  
        x = RecoveredIndex[0][k]  
        y = RecoveredIndex[1][k]  
        population[x, y] = sum(np.random.choice([1, 2], 1, p = [1 - gamma, gamma]))
    # plot subplots   
    if j == 10:
        plt.subplot(2, 2, 2)
        plt.imshow(population, cmap = 'viridis', interpolation = 'nearest')
    if j == 50:
        plt.subplot(2, 2, 3)
        plt.imshow(population, cmap = 'viridis', interpolation = 'nearest')
    if j == 100:
        plt.subplot(2, 2, 4)
        plt.imshow(population, cmap = 'viridis', interpolation = 'nearest')
plt.show()
plt.clf()