"""
    Made By: Marwan Alhindi
    Created On: 25 July 2022
    From: Python Crash Course
    The purpose of this file is to import and analyse online data that has the format of CSV and JSON. CSV is the most common format type for data that's used.

    The Data Visualization project starts in Chapter 15, in which you'll learn to generate data and create a series of functional and beautiful visualizations of that data using Matplotlib and Plotly. Chapter 16 teaches you to access data from online sources and feed it into a visualization package to create plots of weather data and a map of global earthquake activity. Finally, Chapter 17 shows you how to write a program to automatically download and visualize data. Learning to make visualizations allows you to explore the field of data mining, which is a highly sought-after skill in the world today.
"""
import csv
import matplotlib.pyplot as plt
from datetime import datetime

#opening and extracing max temeprature values
filename= 'data/sitka_weather_2018_full.csv'
with open(filename) as f:
    reader= csv.reader(f)
    header= next(reader)

#reading data and error checking
    high_temp,low_temp,dates= [],[],[]
    for row in reader:
        if row[8]:
            each_temp_high= row[8].strip()
            each_temp_low= row[9].strip()
            high_temp.append(int(each_temp_high))
            low_temp.append(int(each_temp_low))
            each_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(each_date)
        else:
            print('No value')

# getting the index of each header
# for index, column_header in enumerate(header):
#      print(index, column_header)

# plotting
plt.style.use('classic')

fig,ax= plt.subplots()
plot_1= ax.plot(dates,high_temp,c= 'red',label= 'High temperature')
plot_2= ax.plot(dates,low_temp,c= 'blue',label= 'Low temperature')

ax.set_title('Temperature in Stika',fontsize= 15)
ax.set_xlabel('Day',fontsize= 15)
fig.autofmt_xdate()
ax.set_ylabel('Temperature',fontsize= 15)
ax.legend()
plt.fill_between(dates, high_temp, low_temp, facecolor='orange', alpha=0.4)
plt.show()