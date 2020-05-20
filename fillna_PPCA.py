import numpy as np
import pandas as pd

from PPCA import *

# preprossing dataset
names = ['Sample_code_number', 'Clump_Thickness', 'Uniformity_of_Cell_Size',
         'Uniformity_of_Cell_Shape', 'Marginal_Adhesion', 'Single_Epithelial_Cell_Size',
         'Bare_Nuclei', 'Bland_Chromatin', 'Normal_Nucleoli', 'Mitoses', 'Class']
origin_data = pd.read_csv("breast-cancer-wisconsin.data", names=names, index_col = False, na_values='?')
#drop columns unnecessary
origin_data.fillna(origin_data.mean(), inplace=True)
origin_data = origin_data.drop(columns = ['Sample_code_number', 'Class'])
# convert to numpy array to generate missing values data
origin_data = origin_data.values
# read missing dataset and define na_values
missing_data = pd.read_csv('breast_cancer50_navalues.csv', na_values = '?')
# fillna by respective mean of each column, and then using to cal RMSE of fillmean and true values
mean_cols = missing_data.mean()
# fillna
missing_data.fillna(mean_cols, inplace = True)
missing_data = missing_data.values # convert to numpy array

# use PPCA predict the missing data values
# using closed form to estimate weight matrix W_ML, dimensionality reduction is 2
W_ML = PPCA(missing_data, 2)[0]
# using EM agorithm to estimate weight matrix W_EM, dimensionality reduction is 2
W_EM = PPCA(missing_data, 2, EM = True)[0]

# The process of Reconstruction data is predictive
data_hat_ML = (W_ML.dot(np.linalg.inv(W_ML.T.dot(W_ML))).dot(W_ML.T).dot(missing_data.T)).T
data_hat_EM = (W_EM.dot(np.linalg.inv(W_EM.T.dot(W_EM))).dot(W_EM.T).dot(missing_data.T)).T


# RMSE calculated between estimates and true, as well as compare how fillna by mean
# get pos of na-values
pos = pd.read_csv('breast_cancer50_pos_navalue.csv', index_col = False)


# calculate RMSE of PPCA and mean fillna
result_ML = []
result_EM = []
result_mean = []
for i in range(0, pos.shape[1]):
  error_ML = []
  error_EM = []
  error_mean = []
  for item in pos.iloc[:, i]:
    error_ML.append((origin_data[item,i] - data_hat_ML[item,i])**2)
    error_EM.append((origin_data[item,i] - data_hat_EM[item,i])**2)
    error_mean.append((origin_data[item,i] - mean_cols[i])**2)
  result_ML.append(round((sum(error_ML)/50)**0.5, 4))
  result_EM.append(round((sum(error_EM)/50)**0.5, 4))
  result_mean.append(round((sum(error_mean)/50)**0.5, 4))

print('RMSE of missing-value predicted and true values by closed form Maximum likelihood :\n {}'.format(result_ML))
print('RMSE of missing-value predicted and true values by Expectation Maximization algorithm:\n {}'.format(result_EM))
print('RMSE of fillna mean and true values: \n {}'.format(result_mean))

## plot RMSE

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 4))
plt.plot(range(1, 10), result_ML, "ro-", label='Closed-form ML')
plt.plot(range(1, 10), result_EM, "yo--", label='EM algorithm')
plt.plot(range(1, 10), result_mean, "bo-", label="Fill mean")

plt.xlabel("ith Feature", fontsize=14)
plt.ylabel("RMSE", fontsize=14)
plt.legend()
plt.show()







