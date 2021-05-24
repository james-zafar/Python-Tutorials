# Exercise 1
# In this exercises we will add some properties to our window. We
# will also add some frame widgets.

# The blocks produced by the code below are not arranged in the
# structure of a pyramid. Try to rectify this.

# Extension Exercise: Make the pyramid blocks random shades of red.
# Use six layers instead of three.


import random
import tkinter as tk


# This function will produce a random shade of green.
# Colours are often expressed using the RGB color model.
# This function will produce a string with only a G (green) value.
def random_red() -> str:
    red_hex = random.choice(['a', 'b', 'c', 'd', 'e', 'f'])
    return f'#{red_hex}00'


window = tk.Tk()

# Here we add a title to our window.
window.title('Red pyramid')

# Here we set a resolution.
window.geometry('500x500')

for i in range(1, 7):
    obj = tk.Frame(window, width=(i * 75), height=75, bg=random_red())
    obj.pack()

window.mainloop()
