import tkinter as tk
from tkinter import ttk, messagebox
import requests

# Function to fetch exchange rates
def get_exchange_rate():
    api_url = "https://api.exchangerate-api.com/v4/latest/USD"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()["rates"]
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch exchange rates: {e}")
        return None

# Conversion function
def convert_currency():
    try:
        usd_amount = float(entry_amount.get())
        selected_currency = combo_currency.get()
        rate = exchange_rates[selected_currency]
        converted_amount = usd_amount * rate
        label_result.config(text=f"{usd_amount} USD = {converted_amount:.2f} {selected_currency}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")
    except KeyError:
        messagebox.showerror("Error", "Please select a valid currency.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Fetch exchange rates at startup
exchange_rates = get_exchange_rate()

if exchange_rates:
    # GUI Setup
    app = tk.Tk()
    app.title("USD Currency Converter")
    app.geometry("400x300")

    # Input section
    tk.Label(app, text="Amount in USD:", font=("Arial", 12)).pack(pady=10)
    entry_amount = tk.Entry(app, font=("Arial", 12), justify="center")
    entry_amount.pack(pady=5)

    # Currency selection
    tk.Label(app, text="Select Currency:", font=("Arial", 12)).pack(pady=10)
    combo_currency = ttk.Combobox(app, values=list(exchange_rates.keys()), font=("Arial", 12))
    combo_currency.pack(pady=5)

    # Convert button
    btn_convert = tk.Button(app, text="Convert", command=convert_currency, font=("Arial", 12))
    btn_convert.pack(pady=20)

    # Result section
    label_result = tk.Label(app, text="", font=("Arial", 14, "bold"))
    label_result.pack(pady=10)

    # Run the app
    app.mainloop()
