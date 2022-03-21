#!/usr/bin/env python
# coding: utf-8

# In[10]:


# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sp
# import the csv file to python
data = pd.read_csv(r"C:\E_Drive\01.MSC_Fintech_Neoma\02.Python for Finance\2nd_GroupProject\VWAGY.csv")


# In[25]:


print(' ')
print('Corporation: Volkswagen')
print('Ticker: VWAGY')
print(' ')
print('Event Nature : Dieselgate')
print('Event Date : 09/20/2015')

print('==========================================================')

# Divide the volume by 1M so that when we plot the stock price and the volume in a single graph, it looks better 
data['Volume_reduced']=data['Volume']/1000000

# show graphically the evolution of the stock price over time and show the volume on the same graph using the secondary axis
price = data['Adj Close']
volume = data['Volume_reduced'] 

plt.title('Evolution of the stock price and the volume over time')

plt.plot(price,'g-',label="Stock Price")
plt.plot(volume,'r--',label="Volume(M)")
plt.legend()
plt.show()

# stock returns
ret=data['Adj Close'].pct_change()
#print(ret)

print(' ')
print('============')
print('Summary')
print('============')
print(' ')

print('Control Window')
print('------------------------')

# Define the control window
Control_window=data['Adj Close'][0:114]

# Compute the average returns 
RetControl=ret[0:114]
avRetControl=RetControl.mean()
print('Average stock return over the control window:',avRetControl*100,'%')

# Compute the volatility 

VolRetControl=RetControl.std()
print('Volatility over the control window:',VolRetControl)

print(' ')
print('Event Window')
print('------------------------')

# Define the event window
Event_window=data['Adj Close'][120:125]

# Compute the average returns 
RetEvent=ret[120:125]
avRetEvent=RetEvent.mean()
print('Average stock return over the event window:',avRetEvent*100,'%')

# Compute the volatility 

VolRetEvent=RetEvent.std()
print('Volatility over the event window:',VolRetEvent)

print(' ')
print(' ')

# Compute the abnormal returns of event window
AR_Event=RetEvent-avRetControl

# Compute the cumulative abnormal returns over the event window
CAR_using_cumsum=AR_Event.cumsum()
CAR=CAR_using_cumsum.iloc[-1]
print('The cumulative abnormal returns over the event window:',CAR)

# Standard deviation of the abnormal returns over the control window
AR_Control=RetControl-avRetControl
sigmaAR=AR_Control.std()
#print(sigmaAR)

# Test statistics
Stat=CAR/(sigmaAR*6**0.5)
print('Test statistics:',Stat)

print(' ')

#Compute the Z critical value for 95% confidence
z95_critical=sp.norm.ppf(0.95)

#Declaring Null and Alternate Hypothesis
H_Null = "the CAR of the event window is equals to 0."
H_Alt = "the CAR of the event window is not equals to 0."

#Checking the absolute value of Test statistic with Z critical value
if (np.absolute(Stat) > z95_critical ) :
    print("We will REJECT the Null Hypothesis which is ",H_Null)
else :
    print("We CANNOT REJECT the Null Hypothesis which is ",H_Null)

# Are the CAR of the event window significantly different from 0?
print('\nIs the CAR of the event window significantly different from 0?')
print(' ')
print('Answer: Yes. The CAR of the event window is significantly different from 0.','\nThe absolute Test Statistic value is 6.82767066419204,','\nwhich is greater than the Z-value i.e. 1.65 at 95% confidence.','\nHence we can reject the Null Hypothesis which is the CAR of the event window is equals to 0. ')


# In[ ]:





# In[ ]:




