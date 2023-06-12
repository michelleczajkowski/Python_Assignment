import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import math as math
import statistics as stats
import numpy as numpy
import pandas as pd
import os as os
import seaborn as seaborn

# create vector with all file names of all participants
file_names = ['2023-06-06_14-46-23_e_f_mich.csv', '2023-06-06_20-37-51_d_m_mart.csv', '2023-06-06_20-41-59_d_m_jaap.csv', '2023-06-06_20-51-12_d_f_marieke.csv']
# combine the four participants into one data file with new  col for name
combined_data = pd.DataFrame()
for file_name in file_names:
    participant = file_name[-8:-4]  
    data = pd.read_csv(file_name)
    # Add the participant column 
    data['participant'] = participant
    
    # add to combined data frame
    
    combined_data = pd.concat([combined_data,data], ignore_index=True)

print(combined_data)
combined_data.to_csv('combined_data.csv', index=False)



