# import sqlite3
# conection = sqlite3.connect('example.db')
# cursor = conection.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS users
#                   (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
# conection.commit()
# conection.close()
# # # print("Database and table created successfully.")
# import sqlite3

# # ۱. اتصال به دیتابیس
# connection = sqlite3.connect("my_data.db")
# cursor = connection.cursor()

# # ۲. ساخت جدول (حتماً این خط باید قبل از INSERT یا SELECT باشد)
# # این خط می‌گوید: اگر جدول وجود ندارد، آن را بساز.
# cursor.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER)")

# # ۳. گرفتن اطلاعات از کاربر و ذخیره
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# cursor.execute("INSERT INTO users VALUES (?, ?)", (name, age))
# connection.commit() # ذخیره تغییرات
# print("User added successfully.")

# # ۴. حالا خواندن اطلاعات (که قبلاً اینجا خطا می‌داد)
# print("--- List of Users ---")
# cursor.execute("SELECT * FROM users")
# results = cursor.fetchall()

# for row in results:
# #     print(f"Name: {row[0]}, Age: {row[1]}")

# # # ۵. بستن اتصال
# # connection.close()
# import sqlite3
# connection = sqlite3.connect("shop.db")
# cursor = connection.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS products
#                   (id INTEGER PRIMARY KEY, name TEXT, price REAL)''')
# products = input("Enter product names and prices (format: name1:price1,name2:price2): ")
# products = dict(item.split(":") for item in products.split(","))
# products = {name: float(price) for name, price in products.items()}

# cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)", products.items())
# connection.commit()
# cursor.execute("SELECT * FROM products")
# results = cursor.fetchall()
# for row in results:
#     print(f"ID: {row[0]}, Name: {row[1]}, Price: ${row[2]:.2f}")
# connection.close()
import tkinter as tk
from tkinter import messagebox

def show_message():
    name = entry.get()
    messagebox.showinfo("خوش‌آمدگویی", f"سلام {name} عزیز! به دنیای برنامه‌های گرافیکی خوش اومدی.")

# ۱. ساخت پنجره اصلی
root = tk.Tk()
root.title("نرم‌افزار من")
root.geometry("300x200")

# ۲. ساخت یک متن راهنما (Label)
label = tk.Label(root, text="نام خود را وارد کنید:")
label.pack(pady=10)

# ۳. ساخت کادر ورودی (Entry)
entry = tk.Entry(root)
entry.pack(pady=5)

# ۴. ساخت دکمه (Button)
button = tk.Button(root, text="کلیک کن!", command=show_message)
button.pack(pady=20)

# ۵. اجرای پنجره
root.mainloop()