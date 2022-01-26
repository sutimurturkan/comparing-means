import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import scipy.stats as st
from scipy.stats import ttest_ind, ttest_ind_from_stats

# Read the csv file
if os.path.exists("Georgiapeaches.csv"): 
  georgia = pd.read_csv("Georgiapeaches.csv")
if os.path.exists("Yangshanpeaches.csv"):
  yangshan = pd.read_csv("Yangshanpeaches.csv")

# Prepare data
x = georgia['Yield per investment (in kilograms per Martian dollar)'].to_numpy()
y = yangshan['Yield per investment (in kilograms per Martian dollar)'].to_numpy()

mean_x = np.mean(x)
mean_y = np.mean(y)

sdx = np.std(x)
sdy = np.std(y)

n1 = x.size
n2 = y.size

#this is a helper variable to make the calculation cleaner
i = (np.square(sdx) / n1) + (np.square(sdy) / n2)

#calculating the test statistic

z = (mean_x - mean_y) / np.sqrt(i)
print (z)

# 90%
ci_x1 = st.t.interval(0.90, n1-1, loc=mean_x, scale=st.sem(x))
ci_y1 = st.t.interval(0.90, n2-1, loc=mean_y, scale=st.sem(y))
print ("The 90% confidence interval for Georgian peaches:", ci_x1)
print ("The 90% confidence interval for Yangshan peaches:", ci_y1)

# 95%
ci_x2 = st.t.interval(0.95, n1-1, loc=mean_x, scale=st.sem(x))
ci_y2 = st.t.interval(0.95, n2-1, loc=mean_y, scale=st.sem(y))
print ("The 95% confidence interval for Georgian peaches:", ci_x2)
print ("The 95% confidence interval for Yangshan peaches:", ci_y2)

# 99%
ci_x3 = st.t.interval(0.99, n1-1, loc=mean_x, scale=st.sem(x))
ci_y3 = st.t.interval(0.99, n2-1, loc=mean_y, scale=st.sem(y))
print ("The 99% confidence interval for Georgian peaches:", ci_x3)
print ("The 99% confidence interval for Yangshan peaches:", ci_y3)
