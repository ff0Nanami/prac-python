# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 09:12:41 2023

@author: gy22zh2
"""

def get_max_distance(agent):
    max_distance = 0
    for i in range(len(agent)):
        a = agent[i]
        for j in range(len(agent)):
            b = agent[j]
            if i < j:                
                dx = a.x - b.x
                dy = a.y - b.y
                distance = ((dx*dx)+(dy*dy))**0.5
                max_distance = max(distance, max_distance)
    return max_distance

def get_distance(x1,y1,x2,y2):
    dx = x1 - x2
    dy = y1 - y2
    distance = ((dx*dx)+(dy*dy))**0.5
    return distance