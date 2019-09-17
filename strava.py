#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 13:24:06 2019

Strava API.

@author: ryan.nanson
"""

import requests as r
import matplotlib.pyplot as plt

url = 'https://www.strava.com/api/v3'

athletePath = '/athletes/{id}'
activityPath = '/activities/{id}'

header = {'Authorization': 'Bearer access_token'}

athleteData = r.get(url + athletePath, headers=header).json()
statsData = r.get(url + athletePath + '/stats', headers=header).json()
print(f"Hello {athleteData['firstname']} {athleteData['lastname']},")
print(f"In total you have run {statsData['all_run_totals']['count']} times covering {statsData['all_run_totals']['distance']}m")
print(f"In total you have rode {statsData['all_ride_totals']['count']} times covering {statsData['all_run_totals']['distance']}m")
      
runs = statsData['all_run_totals']
rides = statsData['all_ride_totals']
      
#runs = {'count': 148, 'distance': 1001410, 'moving_time': 335878, 'elapsed_time': 363712, 'elevation_gain': 7461}
#rides = {'count': 51, 'distance': 1465410, 'moving_time': 440598, 'elapsed_time': 632332, 'elevation_gain': 15512}

plt.style.use('ggplot')

x = ['Runs', 'Rides']
count = [runs['count'], rides['count']]
distance = [runs['distance']/1600, rides['distance']/1600]
moving_time = [runs['moving_time']/3600, rides['moving_time']/3600]

x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, count, color='green')
plt.xlabel("Activity type")
plt.ylabel("Number of occurences")
plt.title("Number of type of activity")

plt.xticks(x_pos, x)
plt.show()

plt.bar(x_pos, distance, color='blue')
plt.xlabel("Activity type")
plt.ylabel("Miles")
plt.title("Miles of activity")

plt.xticks(x_pos, x)
plt.show()

plt.bar(x_pos, moving_time, color='red')
plt.xlabel("Activity type")
plt.ylabel("Miles")
plt.title("Hours of activity")

plt.xticks(x_pos, x)
plt.show()
