import conway
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def read_pattern_from_file(file_path):
    with open(file_path, 'r') as file:
        pattern = file.read()
    return pattern

N = 64

# Create the game of life object
life = conway.GameOfLife(N)
pattern_file = 'gosper.txt'  # Provide the path to your pattern file
pattern = read_pattern_from_file(pattern_file)
life.insertFromPlainText(pattern)  # Insert pattern from file
cells = life.getStates()  # Initial state

# -------------------------------
# Plot cells
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
        print(cellsUpdated)
        img.set_array(cellsUpdated)
    return img,

interval = 300  # ms

# Animate frames with interval between them calling animate function at each frame
ani = animation.FuncAnimation(fig, animate, frames=48, interval=interval, blit=True)

cid = fig.canvas.mpl_connect('key_press_event', on_key)

plt.show()
