# Exercise 6
# Add a label above the convertor to inform the user what
# currency they are converting from/to
# Query an API to get the actual exchange rate.

# Extension: Can you query the currency API you have previously
# used to get the actual exchange rate and use this in your calculations?

# Further Extensions:
# - Try to add a row for GBP to BTC.
# - Try to add an additional Entry to each row such that conversions can be made both ways.

import tkinter as tk

def gbp_to_usd():
    gbp = gbp_entry.get()
    usd = float(gbp) * 1.5
    usd_label["text"] = f"${round(usd, ß2)}"


window = tk.Tk()
window.title("Currency Converter")
window.resizable(width=False, height=False)

# Here we create a frame.
# Instead of putting our widgets in the window, we'll put them in this frame. 
frame = tk.Frame(window)

gbp_label = tk.Label(frame, text="£")
gbp_entry = tk.Entry(frame, width=20)
button_convertor = tk.Button(frame, text="£ \N{RIGHTWARDS BLACK ARROW} $", command=gbp_to_usd)
usd_label = tk.Label(frame, text="$")

# padx and pady refer to padding on the x and y axis.
frame.grid(row=0, column=0, padx=15, pady=15)

gbp_label.grid(row=0, column=0)
gbp_entry.grid(row=0, column=1, sticky="e")
button_convertor.grid(row=0, column=2)
usd_label.grid(row=0, column=3, sticky="w")

window.mainloop()