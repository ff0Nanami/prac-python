# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 09:30:16 2023

@author: gy22zh2
"""

import csv
import matplotlib.pyplot as plt
import matplotlib.animation as anmi

def read_data():
    # Read input data
    f = open('../data/input/in.txt', newline='')
    data = []
    num_rows = 0   
    for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
        row = []
        num_cols = 0
        for value in line:
            row.append(value)
            num_cols = num_cols + 1
            #print(value)
        data.append(row)
        num_rows = num_rows + 1
    f.close()
    return (data,num_rows,num_cols)




    