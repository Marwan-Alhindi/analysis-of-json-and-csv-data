"""
    Made By: Marwan Alhindi
    Created On: 27 July 2022
    From: Python Crash Course
    This file purpose is similar to a previous file that has been created but with different location/city. The way you handled errors here is different than how you handled it in the other file though. You used try-except statement here.

    The Data Visualization project starts in Chapter 15, in which you'll learn to generate data and create a series of functional and beautiful visualizations of that data using Matplotlib and Plotly. Chapter 16 teaches you to access data from online sources and feed it into a visualization package to create plots of weather data and a map of global earthquake activity. Finally, Chapter 17 shows you how to write a program to automatically download and visualize data. Learning to make visualizations allows you to explore the field of data mining, which is a highly sought-after skill in the world today.
"""
import csv
import matplotlib.pyplot as plt
from datetime import datetime

#reading file and extracting certain data
filename= 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    #reading all data
    reader= csv.reader(f)
    headers= next(reader)

    #extracting certain values
    high_temp,low_temp,dates= [],[],[]
    for row in reader:
        try:
            int(row[5])
            int(row[6])
        except ValueError:
            print('Ops. a missing value!')
        else:
            high_temp.append(int(row[5]))
            low_temp.append(int(row[6]))
            formated_date= datetime.strptime(row[2],'%Y-%m-%d')
            dates.append(formated_date)

# #getting index and column header
# for index,column_header in enumerate(headers):
#     print(index,column_header)

fig,ax= plt.subplots()
ax.plot(dates,high_temp,c= 'red',label= 'High temp')
ax.plot(dates,low_temp,c= 'blue',label= 'low temp')
ax.set_title('Temperature in Valley')
ax.set_xlabel('Days')
ax.set_ylabel('Temperature')
plt.fill_between(dates, high_temp, low_temp, facecolor='orange', alpha=0.4)
ax.legend()
plt.show()