# Exercise 6 - Solution 1

import tkinter as tk

import requests


def get_exchange_rate(currency: str) -> float:
    data = requests.get('https://open.er-api.com/v6/latest/GBP')
    if data.status_code != 200:
        raise TypeError(
            f'Failed to retrieve data from the server. Server responded with {data.status_code}, {data.reason}')
    exchange_rate = data.json()['rates'].get(currency.upper(), 0.)
    return exchange_rate


def gbp_to_usd():
    gbp = gbp_entry.get()
    usd = float(gbp) * get_exchange_rate('USD')
    usd_label["text"] = f"${round(usd, 2)}"


def gbp_to_btc():
    gbp = gbp_entry2.get()
    print(gbp, 'hello', type(gbp))
    btc = float(gbp) * get_exchange_rate('BTC')
    btc_label["text"] = f"BTC {round(btc, 6)}"


window = tk.Tk()
window.title("Currency Converter")
window.resizable(width=False, height=False)

# Here we create a frame.
# Instead of putting our widgets in the window, we'll put them in this frame. 
frame = tk.Frame(window)

gbp_usd_label = tk.Label(frame, text="GBP to USD")
gbp_label = tk.Label(frame, text="£")
gbp_entry = tk.Entry(frame, width=20)
button_convertor = tk.Button(frame, text="£ \N{RIGHTWARDS BLACK ARROW} $", command=gbp_to_usd)
usd_label = tk.Label(frame, text="$")

# padx and pady refer to padding on the x and y axis.
frame.grid(row=0, column=0, padx=15, pady=15)

gbp_usd_label.grid(row=0, column=0)
gbp_label.grid(row=1, column=0)
gbp_entry.grid(row=1, column=1, sticky="e")
button_convertor.grid(row=1, column=2)
usd_label.grid(row=1, column=3, sticky="w")

# Next two blocks simply repeat what's already been done for GBP and BTC.
gbp_btc_label = tk.Label(frame, text="GBP to BTC")
gbp_label2 = tk.Label(frame, text="£")
gbp_entry2 = tk.Entry(frame, width=20)
btc_btn_convertor = tk.Button(frame, text="£ \N{RIGHTWARDS BLACK ARROW} BTC", command=gbp_to_btc)
btc_label = tk.Label(frame, text="BTC")

gbp_btc_label.grid(row=2, column=0)
gbp_label2.grid(row=3, column=0)
gbp_entry2.grid(row=3, column=1, sticky="e")
btc_btn_convertor.grid(row=3, column=2)
btc_label.grid(row=3, column=3, sticky="w")

window.mainloop()
