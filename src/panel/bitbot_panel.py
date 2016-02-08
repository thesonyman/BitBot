# Main control panel module

import time
import subprocess
import sys
sys.path.insert(0, '/Users/Zack/Code/BitBot/src')

from tkinter import *
from api.catch import *

currency = 'USD'

root = Tk()
root.geometry("500x500")

v = StringVar()
w = Label(root, textvariable=v)
w.pack()

# Here is the magic : recursion to automate update
def get_str():
    v.set("Last Bitcoin price : " + str(get_last_price(currency)))
    root.after(1000, get_str)

get_str()

root.mainloop()

