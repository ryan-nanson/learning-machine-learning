#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 13:24:06 2019

Strava Data Mining.

@author: ryan.nanson
"""

import requests as r

url = 'https://www.strava.com/api/v3'

athletePath = '/athletes/{athlete_id}'
activityPath = '/activities/{activity_id}'

header = {'Authorization': 'Bearer access_token'}

athleteData = r.get(url + athletePath, headers=header).json()
print(athleteData)

statsData = r.get(url + athletePath + '/stats', headers=header).json()
print(statsData)

activityData  = r.get(url + activityPath, headers=header).json()
print(activityData)
