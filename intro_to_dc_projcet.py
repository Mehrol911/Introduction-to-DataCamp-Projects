#1. This is a Jupyter notebook!

# I'm a code cell, click me, then run me!
256 * 60 * 24 # Children × minutes × hours

#2. Put any code in code cells
def greet(first_name, last_name):
    greeting = 'My name is ' + last_name + ', ' + first_name + ' ' + last_name + '!'
    return greeting

# Replace with your first and last name.
# That is, unless your name is already James Bond.
greet('Bazarov', 'Mehrol')

#3. Jupyter notebooks ♡ data
# Importing the pandas module
import pandas as pd

# Reading in the global temperature data
global_temp = pd.read_csv('datasets/global_temperature.csv')

# Take a look at the first datapoints
# ... YOUR CODE FOR TASK 3 ...

#4. Jupyter notebooks ♡ plots
# Setting up inline plotting using jupyter notebook "magic"
%matplotlib inline

import matplotlib.pyplot as plt

# Plotting global temperature in degrees celsius by year
plt.plot(global_temp['year'], global_temp['degrees_celsius'])

# Adding some nice labels 
plt.xlabel('Year') 
plt.ylabel('Degrees_celsius') 

#5. Jupyter notebooks ♡ a lot more
# Making a map using the folium module
import folium
phone_map = folium.Map()

# Top three smart phone companies by market share in 2016
companies = [
    {'loc': [37.4970,  127.0266], 'label': 'Samsung: 20.5%'},
    {'loc': [37.3318, -122.0311], 'label': 'Apple: 14.4%'},
    {'loc': [22.5431,  114.0579], 'label': 'Huawei: 8.9%'}] 

# Adding markers to the map
for company in companies:
    marker = folium.Marker(location=company['loc'], popup=company['label'])
    marker.add_to(phone_map)

# The last object in the cell always gets shown in the notebook
phone_map

#6. Goodbye for now!
# Are you ready to get started with  DataCamp projects?
I_am_ready = True

# Ps. 
# Feel free to try out any other stuff in this notebook. 
# It's all yours!
