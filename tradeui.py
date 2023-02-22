import tkinter as tk
from tkinter import ttk
import ccxt

def execute_trade():
    exchange = ccxt.binance({
        'rateLimit': 3000,
        'enableRateLimit': True,
        'apiKey': api_key_entry.get(),
        'secret': api_secret_entry.get()
    })
    symbol = trading_pair_entry.get()
    amount = float(amount_entry.get())
    price = float(price_entry.get())
    order = exchange.create_order(symbol, 'limit', trade_type.get(), amount, price)
    result_label.configure(text=f"Order ID: {order['id']}\nOrder Status: {order['status']}")

root = tk.Tk()
root.title("Trading Bot")

api_key_label = ttk.Label(root, text="API Key:")
api_key_label.grid(column=0, row=0)
api_key_entry = ttk.Entry(root)
api_key_entry.grid(column=1, row=0)

api_secret_label = ttk.Label(root, text="API Secret:")
api_secret_label.grid(column=0, row=1)
api_secret_entry = ttk.Entry(root, show="*")
api_secret_entry.grid(column=1, row=1)

trading_pair_label = ttk.Label(root, text="Trading Pair (e.g BTC/USDT):")
trading_pair_label.grid(column=0, row=2)
trading_pair_entry = ttk.Entry(root)
trading_pair_entry.grid(column=1, row=2)

amount_label = ttk.Label(root, text="Amount:")
amount_label.grid(column=0, row=3)
amount_entry = ttk.Entry(root)
amount_entry.grid(column=1, row=3)

price_label = ttk.Label(root, text="Price:")
price_label.grid(column=0, row=4)
price_entry = ttk.Entry(root)
price_entry.grid(column=1, row=4)

trade_type = tk.StringVar(value="buy")
buy_radio = ttk.Radiobutton(root, text='Buy', variable=trade_type, value='buy')
buy_radio.grid(column=0, row=5)
sell_radio = ttk.Radiobutton(root, text='Sell', variable=trade_type, value='sell')
sell_radio.grid(column=1, row=5)

execute_button = ttk.Button(root, text="Execute Trade", command=execute_trade)
execute_button.grid(column=0, row=6)

result_label = ttk.Label(root, text="")
result_label.grid(column=0, row=7, columnspan=2)

root.mainloop()
