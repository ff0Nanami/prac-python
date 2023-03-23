# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 11:40:39 2023

@author: gy22zh2
"""
import random
import my_modules.geometry as geo

class Agent():
    def __init__(self, agents, i, environment, n_rows, n_cols, x = None, y = None):
        self.agents = agents
        self.i = i
        self.environment = environment
        if x == None:
            tnc = int(n_cols / 3)
            self.x = random.randint(tnc - 1, (2 * tnc) - 1)
        else:
            self.x = x
        if y == None:
            tnr = int(n_rows / 3)
            self.y = random.randint(tnr - 1, (2 * tnr) - 1)
        else:
            self.y = y
        self.store = random.randint(0, 99)
        self.store_shares = 0
        
    
    def __str__(self):
        return self.__class__.__name__ + "(x=" + str(self.x) +" , y=" + str(self.y) + ")"
    
    def __repr__(self):
        return str(self)
    def move(self, x_min, y_min, x_max, y_max):
        # Change x and y randomly
        rn = random.random()
        if rn < 0.5:
            self.x = self.x + 1
        else:
            self.x = self.x - 1
        rn = random.random()
        if rn < 0.5:
            self.y = self.y + 1
        else:
            self.y = self.y - 1
        
        #limited move
        if self.x < x_min:
            self.x = x_min
        if self.y < y_min:
            self.y = y_min
        if self.x > x_max:
            self.x = x_max
        if self.y > y_max:
            self.y = y_max   
            
    def eat(self):
        if self.environment[self.y][self.x] >= 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            if self.store_shares > 100:
                recover = self.store_shares / 2
                self.environment[self.y][self.x] += recover
                self.store_shares = 0
            
    def share(self,neighbourhood):
        neighbours = []
        for a in self.agents:
            distance = geo.get_distance(a.x,a.y,self.x,self.y)
            if distance < neighbourhood:
                neighbours.append(a.i)
            n_neighbours = len(neighbours)
            shares = self.store / n_neighbours
            for i in neighbours:
                self.agents[i].store_shares += shares
