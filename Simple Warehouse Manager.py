import sqlite3
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("simple Warehouse Manager")
root.geometry("300x250")

def init_db():
    conn = sqlite3.connect("warehouse.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS inventory
                      (id INTEGER PRIMARY KEY, item TEXT, quantity INTEGER)''')
    conn.commit()
    conn.close()
def add_item():
    item = entry_item.get()
    quantity = entry_quantity.get()
    
    conn = sqlite3.connect("warehouse.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO inventory (item, quantity) VALUES (?, ?)", (item, int(quantity)))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", f"Item '{item}' with quantity {quantity} added!")
    entry_item.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
init_db()
def check_stock():
    conn = sqlite3.connect("warehouse.db")
    cursor = conn.cursor()
    cursor.execute(" SELECT * FROM inventory where item=?", (entry_item.get(),))
    results = cursor.fetchall()
    conn.close()
    
    if not results:
        messagebox.showinfo("Info", "Inventory is empty!")
        return
    stock_list = "\n".join([f"Item: {row[1]} | Quantity: {row[2]}" for row in results])
    messagebox.showinfo("Current Stock", stock_list)

def show_all():
    conn = sqlite3.connect("warehouse.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory")
    rows = cursor.fetchall()
    conn.close()
    print("Current Database Content:", rows)
    

tk.Label(root, text="Enter Item Name:").pack()
entry_item = tk.Entry(root)
entry_item.pack(pady=5)
tk.Label(root, text="Enter Item Quantity:").pack()
entry_quantity = tk.Entry(root)
entry_quantity.pack(pady=5)

    
tk.Button(root, text="add to inventory", command=add_item).pack(pady=10)
tk.Button(root, text="check stock", command=check_stock).pack(pady=10)
tk.Button(root, text="Show All Items", command=show_all).pack(pady=10)
root.mainloop()