# -*- coding: utf-8 -*-
"""
Game of life script with animated evolution

Created on Tue Jan 15 12:37:52 2019

@author: shakes
"""
import conway
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def get_file(filepath: str) -> str:
    """
    Reads the contents of a file from the specified file path.

    Args:
        filepath (str): The path to the file to be read.

    Returns:
        str: The contents of the file as a string.

    Raises:
        FileNotFoundError: If the specified file does not exist or the path is invalid.
        PermissionError: If the user does not have permission to read the file.
        Exception: If any other error occurs while reading the file.
    """
    with open(filepath, "r") as text_file:
        return text_file.read()

N = 200

#create the game of life object
life = conway.GameOfLife(N, finite=False, fastMode=False)

gosperglidergun = get_file("rle/gosperglidergun.rle")

p46_gliderless_LWSS_gun = get_file("rle/p46_gliderless_LWSS_gun.rle")

twogun = get_file("rle/twogun.rle")

inverter = get_file("rle/inverter.rle")



#life.randomLargePattern()
life.insertFromRLE(p46_gliderless_LWSS_gun, 40)

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
        plt.gcf().canvas.mpl_disconnect(cid)  # Disconnect the key press event handler

def animate(i):
    """perform animation step"""
    global life
    
    if not pause:
        life.evolve()
        cellsUpdated = life.getStates()
        img.set_array(cellsUpdated)
    return img,

interval = 2 #ms

#animate frames with interval between them calling animate function at each frame
ani = animation.FuncAnimation(fig, animate, frames=48, interval=interval, blit=True)

cid = fig.canvas.mpl_connect('key_press_event', on_key)

plt.show()
