import sqlite3
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Shop Application")
root.geometry("300x250")

tk.Label(root, text="Enter Product Name:").pack()
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

tk.Label(root, text="Enter Product Price:").pack()
entry_price = tk.Entry(root)
entry_price.pack(pady=5)
    
def save_data():
    print("Saving data...")
    name = entry_name.get()
    price = entry_price.get()
    print(f"Product Name: {name}, Product Price: {price}")
    try:
        conn = sqlite3.connect("shop.db")
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS products
                      (id INTEGER PRIMARY KEY, name TEXT, price REAL)''')
        cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, float(price)))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", f"Product '{name}' with price ${price} saved!")
        entry_name.delete(0, tk.END)  # کادر نام رو پاک کن
        entry_price.delete(0, tk.END) # کادر قیمت رو پاک کن
    except:
        messagebox.showerror("Error", "Failed to save product data.")
    
btn = tk.Button(root, text="saved Products", command=save_data)
btn.pack(pady=20)
root.mainloop()
    
    