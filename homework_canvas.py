import csv
import json
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def clean_data(data):
    return data.strip().replace('"', '')


def convert_to_json():
    input_file = 'SalesJan2009.csv'
    output_file = 'transaction_data.json'
    
    sales_data = []

    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row

        for row in reader:
            transaction_date = clean_data(row[0])
            product = clean_data(row[1])
            price = clean_data(row[2])
            payment_type = clean_data(row[3])
            name = clean_data(row[4])
            city = clean_data(row[5])
            state = clean_data(row[6])
            country = clean_data(row[7])

            transaction_dict = {
                "Transaction_date": transaction_date,
                "Product": product,
                "Price": price,
                "Payment_Type": payment_type,
                "Name": name,
                "City": city,
                "State": state,
                "Country": country
            }

            sales_data.append(transaction_dict)

    with open(output_file, 'w') as json_file:
        json.dump(sales_data, json_file, indent=4)
        
    messagebox.showinfo("Conversion Complete", "CSV file converted to JSON successfully!")


def show_product_table():
    product_window = tk.Toplevel(root)
    product_window.title("Product Table")
    product_window.geometry("800x600")
    product_window.configure(bg='green')

    tree = ttk.Treeview(product_window)
    tree["columns"] = ("Transaction Date", "Product", "Price", "Payment Type", "Name", "City", "State", "Country")
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("Transaction Date", anchor=tk.W)
    tree.column("Product", anchor=tk.W)
    tree.column("Price", anchor=tk.W)
    tree.column("Payment Type", anchor=tk.W)
    tree.column("Name", anchor=tk.W)
    tree.column("City", anchor=tk.W)
    tree.column("State", anchor=tk.W)
    tree.column("Country", anchor=tk.W)

    tree.heading("#0", text="", anchor=tk.W)
    tree.heading("Transaction Date", text="Transaction Date", anchor=tk.W)
    tree.heading("Product", text="Product", anchor=tk.W)
    tree.heading("Price", text="Price", anchor=tk.W)
    tree.heading("Payment Type", text="Payment Type", anchor=tk.W)
    tree.heading("Name", text="Name", anchor=tk.W)
    tree.heading("City", text="City", anchor=tk.W)
    tree.heading("State", text="State", anchor=tk.W)
    tree.heading("Country", text="Country", anchor=tk.W)

    with open('transaction_data.json', 'r') as file:
        sales_data = json.load(file)
        for item in sales_data:
            transaction_date = item["Transaction_date"]
            product = item["Product"]
            price = item["Price"]
            payment_type = item["Payment_Type"]
            name = item["Name"]
            city = item["City"]
            state = item["State"]
            country = item["Country"]
            tree.insert("", "end", values=(transaction_date, product, price, payment_type, name, city, state, country))

    tree.pack(fill=tk.BOTH, expand=True)


def search_person():
    search_name = entry.get()
    with open('transaction_data.json', 'r') as file:
        sales_data = json.load(file)
        for item in sales_data:
            if item["Name"] == search_name:
                messagebox.showinfo("Person Found", f"Name: {item['Name']}\nCity: {item['City']}\nState: {item['State']}\nCountry: {item['Country']}")
                return
    messagebox.showinfo("Person Not Found", f"No person with the name '{search_name}' found.")


def quit_program():
    root.quit()


root = tk.Tk()
root.title("Main Window")
root.geometry("300x250")
root.configure(bg='green')

label = tk.Label(root, text="Welcome to Sales Data Converter", bg='green', fg='white')
label.pack(pady=10)

convert_button = tk.Button(root, text="Convert to JSON", command=convert_to_json, bg='yellow')
convert_button.pack()

show_table_button = tk.Button(root, text="Show Product Table", command=show_product_table, bg='yellow')
show_table_button.pack()

search_label = tk.Label(root, text="Search by Name:", bg='green', fg='white')
search_label.pack()

entry = tk.Entry(root)
entry.pack()

search_button = tk.Button(root, text="Search", command=search_person, bg='yellow')
search_button.pack()

quit_button = tk.Button(root, text="Quit", command=quit_program, bg='yellow')
quit_button.pack()

root.mainloop()
