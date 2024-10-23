# imports
from tkinter import *

# first for gui
root = Tk()

# label widget creation
myLabel = Label(root, text="Testing")

# packs everything onto window
# FIX : impactical , could be done better
myLabel.pack()

# create event loop
root.mainloop()