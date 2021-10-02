# Exercise 5 - Solution 1

import tkinter as tk
from math import sqrt

window = tk.Tk()

window.title('Basic counter')

# Instead of pack, we will configure rows and columns.
# We set weight to 1, this will allow the widgets to grow into extra space.
# This has the desirable effect of expanding widgets if we make our window bigger.

# We will define one row (indexed at 0)
window.rowconfigure(0, minsize=100, weight=1)
# We will define three columns (also indexed at 0)
window.columnconfigure([0, 1, 2, 3, 4], minsize=100, weight=1)

# One row and three columns will cut our window into equal thirds.
# The middle section will contain a label with a text value (our counter).
label = tk.Label(window, text="50")
label.grid(row=0, column=2)


# Here two functions are defined which effect the counter value of the label.
def increase():
    value = float(label["text"])
    label["text"] = f"{value + 1}"


def decrease():
    value = float(label["text"])
    label["text"] = f"{value - 1}"


def calc_sqrt():
    value = float(label["text"])
    value = sqrt(value)
    label["text"] = f"{value}"


def round_value():
    value = float(label["text"])
    value = round(value, 2)
    label["text"] = f"{value}"


# Here two buttons are created which have functions bound to the click event.
# sticky="nsew" simply means the button will grow in all directions if the window is expanded.
btn_sqrt = tk.Button(window, text="sqrt", command=calc_sqrt)
btn_sqrt.grid(row=0, column=0, sticky="nsew")

btn_decrease = tk.Button(window, text="-", command=decrease)
btn_decrease.grid(row=0, column=1, sticky="nsew")

btn_increase = tk.Button(window, text="+", command=increase)
btn_increase.grid(row=0, column=3, sticky="nsew")

btn_round = tk.Button(window, text="round", command=round_value)
btn_round.grid(row=0, column=4, sticky="nsew")

window.mainloop()
