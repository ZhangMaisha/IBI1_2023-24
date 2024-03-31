import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/Users/zhangmaisha/Desktop/IBI/IBI1_2023-24/IBI1_2023-24/Practical7")
os.getcwd()
os.listdir()
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
# showing the fourth column (the DALYs) from every 10th row, starting from the first row, for the first 100 rows (inclusive).
print(dalys_data.iloc[0:110:10,3])
# use a Boolean to show DALYs for all rows corresponding to Afghanistan.
Afghanistan = []
for i in range(0,dalys_data.shape[0]):
    if dalys_data.iloc[i,0] == 'Afghanistan':
        Afghanistan.append(True)
    else:
        Afghanistan.append(False)
print(dalys_data.loc[Afghanistan,"DALYs"])
# careate chian_data
China = []
for i in range(0,dalys_data.shape[0]):
    if dalys_data.iloc[i,0] == 'Afghanistan':
        China.append(True)
    else:
        China.append(False)
china_data = dalys_data.iloc[China, :]
# compute the mean DALYs in China
mean_china_DALYs = np.mean(dalys_data.loc[China, 'DALYs'])
print('the mean DALYs in China:',mean_china_DALYs) # The DALYs in China in 2019 was less than the mean.
# create a plot showing the DALYS over time in China.
plt.figure()
plt.plot(china_data.Year, china_data.DALYs, 'b+')
plt.xticks(china_data.Year,rotation=-90)
plt.title('DALYS over time in China')
plt.show()
plt.clf()
# Plot a boxplot of DALYs across countries in 2019.
DALYs_2019 = []
for i in range(0,dalys_data.shape[0]):
    if dalys_data.iloc[i,2] == 2019:
        DALYs_2019.append(True)
    else:
        DALYs_2019.append(False)
data_2019 = dalys_data.iloc[DALYs_2019,:]
labels =['DALYs across countries in 2019']
plt.boxplot(data_2019.DALYs, labels = labels)
plt.show()
plt.clf()