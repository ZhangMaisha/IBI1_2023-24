import matplotlib.pyplot as plt  
  
# Activities and corresponding average time spent per day  
activities = {'Sleeping': 8,'Classes': 6,'Studying': 3.5,'TV': 2,'Music': 1,'other':3.5}  
  
#Plot pie charts
labels = activities.keys()  
sizes = activities.values()  
colors = ['#66b3ff','#99cc99','#ffcc99','#ff9999','#cc99cc','#6699cc'] 
plt.figure(figsize=(10, 7))  
plt.pie(sizes, labels=labels, colors=colors, startangle=90)  
plt.axis('equal')  # Make sure the pie chart is round  
plt.title('Average Daily Activities of a University Student')  
plt.show()  
  
# Suppose we want to calculate the average time spent per day on the activity "Sleeping".  
activity_name = 'Sleeping'  
average_hours_per_activity = activities[activity_name]  
  
print(f"The average number of hours spent on {activity_name} is: {average_hours_per_activity} hours")