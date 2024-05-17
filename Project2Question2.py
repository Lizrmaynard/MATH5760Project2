#!/usr/bin/env python
# coding: utf-8

# # Question 2, Project 2:

# In[60]:


import csv
import pandas as pd
import pandas_datareader as pdr
from pandas import DataFrame
from math import log, sqrt, pi, exp
from datetime import datetime, date
from scipy import stats
import numpy as np
from scipy.sparse import csc_matrix
from scipy.stats import bernoulli
from scipy.optimize import fsolve
from scipy.stats import norm
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
plt.style.use('ggplot')
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Import Desired Data

# We also display the data to check and ensure we have what we want. We do this for both VIX and SPY.

# In[41]:


SPY = pd.read_csv("SPY4.csv")
SPY


# In[42]:


VIX = pd.read_csv("VIX.csv", index_col = 'Date')
VIX


# ### Isolate Desired Variable For Calculations

# We pull out the column data we wish to do our calculations on. This being the Adj Close of SPY.

# In[43]:


SPYc = pd.DataFrame(SPY['Adj Close'])
SPYc


# ### Calculation Of Rolling Average & Plot

# We now calculate the percentage change of the Adj Close of SPY, using the log method from Project 1. Next, we follow the given equation in question 2, where we now find the square root of the rolling average (using .std() for the inner sum), multiplying by 252/29, then finally multiplying it all by 100. We then plot the result of that rolling window.

# In[44]:


SPYc['Change'] = np.log(SPYc['Adj Close'] / SPYc['Adj Close'].shift())
SPYc['Volatility'] = np.sqrt(SPYc.Change.rolling(30).std().shift()*(252/29))*100
SPYc['Volatility'].plot(figsize=(10,5),linewidth=3,color='firebrick')


# ### Plotting VIX Data

# We plot the VIX data to compare it to the rolling average. We note that the Y-axis have a similar scale, indicating we are on the right track and can continue our analysis.

# In[45]:


VIX['Adj Close'].plot(figsize=(15,10),linewidth=3,color='darkgreen')


# ### Plotting Both VIX and Moving Average Volatility Together

# We plot VIX and the moving average together to get an easier comparison and visual as to what exactly is going on with both sets of data.

# In[46]:


fig,ax = plt.subplots(figsize=(15,10))
ax.plot(SPYc['Volatility'], color="firebrick",linewidth=3)
ax.set_xlabel("Date",fontsize=12)
ax.set_ylabel("Volatility",color="firebrick",fontsize=14)
ax2=ax.twinx()
ax2.plot(VIX["Adj Close"],color="darkgreen",linewidth=3)
ax2.set_ylabel("VIX Adj Close",color="darkgreen",fontsize=14)
plt.show()


# In[59]:


SPYc['Date'] = SPY['Date']
SPYc['Change'] = np.log(SPYc['Adj Close'] / SPYc['Adj Close'].shift())
SPYc['Volatility'] = np.sqrt(SPYc.Change.rolling(30).std().shift()*(252/29))*100
SPYc = SPYc[["Date", "Adj Close", "Change","Volatility"]] 
SPYc


# In[48]:


VIXcomp = pd.DataFrame(VIX['Adj Close'])
VIXcomp


# ### Comment on the relations and differences between these two time series ( ̄σi,vi).

# The series are on a similar scale to one another, with the VIX data ranging from about 15-29 and the moving average ranging from about 20-28. The discrepancy between the two (since they are on a similar scale but don't line up a whole lot) can be explained by noting that in that timeframe, the market was in a state of upheaval due to the omicron variant of COVID-19, changing the moving average volatility while the VIX data follows what the expected volatility will be.
