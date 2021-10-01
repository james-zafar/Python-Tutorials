# Exercise 4
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
def random_green() -> str:
    green_hex = random.choice(['a', 'b', 'c', 'd', 'e', 'f'])
    return f'#0{green_hex}0'


window = tk.Tk()

# Here we add a title to our window.
window.title('Green pyramid')

# Here we set a resolution.
window.geometry('500x500')

# Now we will create our first widgets, three frames of various sizes.
long_frame = tk.Frame(window, width=450, height=150, bg=random_green())
medium_frame = tk.Frame(window, width=300, height=150, bg=random_green())
narrow_frame = tk.Frame(window, width=150, height=150, bg=random_green())

# The pack method is used to add them to their parent widget (window)
long_frame.pack()
medium_frame.pack()
narrow_frame.pack()

window.mainloop()
