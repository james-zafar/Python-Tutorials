# Exercise 4 - Solution 2


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
