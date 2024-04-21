# -*- coding: utf-8 -*-
"""
Game of life script with animated evolution

Created on Tue Jan 15 12:37:52 2019

@author: shakes
"""
import conway
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = 64

#create the game of life object
life = conway.GameOfLife(N, finite=False, fastMode=False)

#life.insertFromPlainText('text_files/puffer.txt', 5, 5)

#life.insertFromPlainText('text_files/jaydot.txt', 20, 20)

life.insertFromPlainText('text_files/ants.txt', 5, 5)

cells = life.getStates() #initial state

#-------------------------------
#plot cells
fig = plt.figure()
plt.gray()
img = plt.imshow(cells, animated=True)

pause = True  # Initialize with animation paused

def on_key(event):
    global pause
    if event.key == ' ':
        pause = not pause  # Toggle pause   
        if pause:
            ani.event_source.stop()  # Pause animation
        else:
            ani.event_source.start()  # Unpause animation

def animate(i):
    """perform animation step"""
    global life
    
    if not pause:
        life.evolve()
        cellsUpdated = life.getStates()
        img.set_array(cellsUpdated)
    return img,

interval = 250 #ms

#animate frames with interval between them calling animate function at each frame
ani = animation.FuncAnimation(fig, animate, frames=48, interval=interval, blit=True)

cid = fig.canvas.mpl_connect('key_press_event', on_key)

plt.show()
