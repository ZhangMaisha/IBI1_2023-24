a=5      #the initial density
i=0      #the starting day
while a<=90:  #the number of circle-1 equals to the days I can stay away from the lab
    a=2*a    #doubles the density
    i=i+1    #increase the day number by 1
print("On day",i,"the cell density goes over 90%, which means you have",i-1,"free days")