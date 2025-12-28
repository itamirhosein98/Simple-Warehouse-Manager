import sqlite3
import tkinter as tk
from tkinter import messagebox

# 1. Database Initialization
def init_db():
    conn = sqlite3.connect("phonebook.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts
                      (id INTEGER PRIMARY KEY, name TEXT, phone TEXT)''')
    conn.commit()
    conn.close()

# 2. Add Contact Function
def add_contact():
    # Getting text from entry widgets
    name = entry_name.get()
    phone = entry_phone.get()

    if name == "" or phone == "":
        messagebox.showwarning("Error", "Please fill all fields!")
        return
    
    conn = sqlite3.connect("phonebook.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, phone) VALUES (?, ?)", (name, phone))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Success", f"Contact '{name}' saved successfully!")
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

# 3. Show All Contacts Function
def show_all_contacts():
    conn = sqlite3.connect("phonebook.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    results = cursor.fetchall()
    conn.close()
    
    if not results:
        messagebox.showinfo("Info", "Phonebook is empty!")
        return

    # Joining results into a single string for display
    contacts_list = "\n".join([f"Name: {row[1]} | Phone: {row[2]}" for row in results])
    messagebox.showinfo("All Contacts", contacts_list)

# 4. GUI Setup
init_db()
root = tk.Tk()
root.title("Amir's Phonebook")
root.geometry("300x350")

# Input for Name
tk.Label(root, text="Contact Name:").pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack()

# Input for Phone
tk.Label(root, text="Phone Number:").pack(pady=5)
entry_phone = tk.Entry(root)
entry_phone.pack()

# Buttons
btn_save = tk.Button(root, text="Save Contact", command=add_contact, bg="blue", fg="white")
btn_save.pack(pady=20)

btn_show = tk.Button(root, text="Show All", command=show_all_contacts, bg="green", fg="white")
btn_show.pack(pady=10)

root.mainloop()
