# Given data  
uk_cities = ["Edinburgh", "Glasgow", "Stirling", "London"]  
uk_populations = [0.56, 0.62, 0.04, 9.7]  
china_cities = ["Haining", "Hangzhou", "Shanghai", "Beijing"]  
china_populations = [0.58, 8.4, 29.9, 22.2]  
  
# Sort the UK and China populations    
uk_sorted_indices = sorted(range(len(uk_cities)), key=lambda k: uk_populations[k])  
uk_sorted_cities = [uk_cities[i] for i in uk_sorted_indices]  
uk_sorted_pops = [uk_populations[i] for i in uk_sorted_indices]  
  
china_sorted_indices = sorted(range(len(china_cities)), key=lambda k: china_populations[k])  
china_sorted_cities = [china_cities[i] for i in china_sorted_indices]  
china_sorted_pops = [china_populations[i] for i in china_sorted_indices]  
import matplotlib.pyplot as plt  
# Create bar plot for UK cities  
plt.figure(figsize=(10, 5))  
plt.bar(uk_cities, uk_sorted_pops)  
plt.title("UK City Populations (millions)")  
plt.xlabel("Cities")  
plt.ylabel("Population")  
plt.tight_layout()  #Make sure that all elements are clearly displayed and that there is no overlap.
plt.show()  
  
# Create bar plot for China cities  
plt.figure(figsize=(10, 5))  
plt.bar(china_cities, china_sorted_pops)  
plt.title("China City Populations (millions)")  
plt.xlabel("Cities")  
plt.ylabel("Population")  
plt.tight_layout()  
plt.show()