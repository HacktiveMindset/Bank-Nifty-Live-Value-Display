import tkinter as tk
import requests

root = tk.Tk()
root.title("Bank Nifty Index")

label = tk.Label(root, text="Bank Nifty Index:")
label.pack(pady=10)

value_label = tk.Label(root, text="Loading...")
value_label.pack()


def update_value():
    API_KEY = "X0nZa5RILTxkYN2hKG13_eLRJwqU8amC"
    response = requests.get(f"https://api.polygon.io/v3/trades/O:TSLA210903C00700000?apiKey={API_KEY}")
    print(response.text)

    data = response.json()
    
    value_label.config(text=value)
    root.after(10000, update_value)  # update the value every 10 seconds


update_value()
root.mainloop()
