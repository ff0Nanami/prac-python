# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 10:05:47 2023

@author: gy22zh2
"""

import random
import math
import tkinter as tk
import socket
import requests
import bs4
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import operator
import time
import my_modules.agentFramework as af
import my_modules.io as io
import my_modules.geometry as geo
import imageio
import os


#Timing start
start = time.perf_counter()


loopSeed = 5
random.seed(loopSeed)

# Setting environment
(environment , n_rows , n_cols) = io.read_data()
#n_rows = environment.num_rows
#plt.imshow(environment)


# Initialise parameters
n_agents = 10
n_loop = 50
x_min = 0
y_min = 0
x_max = n_cols - 1
y_max = n_rows - 1
sum_store = 0
sum_store_share = 0
global ite
ite = 0
images = []   
# Initiailise agents
r = requests.get('http://agdturner.github.io/resources/abm9/data.html', verify=False)
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)
agent = []
print("agent")
for i in range(n_agents):
    # Create an agent
    y = int(td_ys[i].text) + 99
    x = int(td_xs[i].text) + 99
    agent.append(af.Agent(agent, i, environment, n_rows, n_cols, x, y))
    #print(agent[i].agent[i])
 
    
 
    
 
#function
def plot():
    print("1")
    fig.clear()
    plt.ylim(y_min, y_max)
    plt.xlim(x_min, x_max)
    plt.imshow(environment)
    for i in range(n_agents):
        plt.scatter(agent[i].x, agent[i].y, color='black')
    # Plot the coordinate with the largest x red
    lx = max(agent, key=operator.attrgetter('x'))
    plt.scatter(lx.x, lx.y, color='red')
    # Plot the coordinate with the smallest x blue
    sx = min(agent, key=operator.attrgetter('x'))
    plt.scatter(sx.x, sx.y, color='blue')
    # Plot the coordinate with the largest y yellow
    ly = max(agent, key=operator.attrgetter('y'))
    plt.scatter(ly.x, ly.y, color='yellow')
    # Plot the coordinate with the smallest y green
    sy = min(agent, key=operator.attrgetter('y'))
    plt.scatter(sy.x, sy.y, color='green')
    filename = '../data/output/images/image' + str(ite) + '.png'
    plt.savefig(filename)
    plt.show()
    images.append(imageio.imread(filename))
    return fig       
        
def update(frames):
    print("2")
    # Model loop
    global carry_on
    # Move agents
    print("Move and eat")
    for i in range(n_agents):
        agent[i].move(x_min, y_min, x_max, y_max)
        agent[i].eat()
        #print(agents[i])
    # Share store
    print("Share")
    # Distribute shares
    for i in range(n_agents):
        agent[i].share(neighbourhood = 200)
    # Add store_shares to store and set store_shares back to zero
    for i in range(n_agents):
        #print(agents[i])
        agent[i].store = agent[i].store_shares
        agent[i].store_shares = 0
    #print(agents)
    # Print the maximum distance between all the agents
    print("Maximum distance between all the agents", geo.get_max_distance(agent))

    # Stopping condition
    # Random
    if random.random() < 0.1:
        #if sum_as / n_agents > 80:
        carry_on = False
        print("stopping condition")

    # Plot
    global ite
    plot()
    ite = ite + 1

def gen_function():
    print("3")
    global ite
    ite = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (ite < n_loop) & (carry_on) :
        yield ite # Returns control and waits next call.
        ite = ite + 1
    global data_written
    if data_written == False:
        # Write data
        print("write data")
        #io.write_data('../data/output/out7.txt', environment)
        #imageio.mimsave('../data/output/out7.gif', images, fps=3)
        data_written = True    

def run(canvas):
    animation = anim.FuncAnimation(fig, update, init_func=plot, frames=gen_function, repeat=False)
    animation.new_frame_seq()
    canvas.draw()

def exiting():
    """
    Exit the program.
    """
    root.quit()
    root.destroy()
    #sys.exit(0)
    
#Animate
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
carry_on = True
data_written = False

root = tk.Tk()
root.wm_title("Agent Based Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
menu_0 = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=menu_0)
menu_0.add_command(label="Run model", command=lambda: run(canvas))
menu_0.add_command(label="Write data", command=lambda: output())
menu_0.add_command(label="Exit", command=lambda: exiting())
menu_0.entryconfig("Write data", state="disabled")
# Exit if the window is closed.
root.protocol('WM_DELETE_WINDOW', exiting)
tk.mainloop()

#Timing end

end = time.perf_counter()
print("Time taken to calculate maximum distance", end - start, "seconds")
 

# For storing images
# Loop for move




