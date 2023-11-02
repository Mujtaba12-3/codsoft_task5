import tkinter as tk
from tkinter import messagebox

# Function to add a contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if name and phone:
        contact_list.append((name, phone, email, address))
        clear_entries()
        update_contact_list()
    else:
        messagebox.showerror("Error", "Name and phone are required.")

# Function to clear input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Function to update the contact list
def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contact_list:
        contact_listbox.insert(tk.END, contact[0] + " - " + contact[1])

# Function to search for a contact
def search_contact():
    search_query = search_entry.get()
    contact_listbox.delete(0, tk.END)
    for contact in contact_list:
        if search_query in contact[0] or search_query in contact[1]:
            contact_listbox.insert(tk.END, contact[0] + " - " + contact[1])

# Function to update a contact
def update_selected_contact():
    selected_contact = contact_listbox.curselection()
    if selected_contact:
        index = int(selected_contact[0])
        name, phone, email, address = contact_list[index]
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        name_entry.insert(0, name)
        phone_entry.insert(0, phone)
        email_entry.insert(0, email)
        address_entry.insert(0, address)

# Function to delete a contact
def delete_selected_contact():
    selected_contact = contact_listbox.curselection()
    if selected_contact:
        index = int(selected_contact[0])
        contact_list.pop(index)
        clear_entries()
        update_contact_list()

# Create the main application window
app = tk.Tk()
app.title("Contact Management System")

# Create input fields for contact details
name_label = tk.Label(app, text="Name:")
name_entry = tk.Entry(app)
phone_label = tk.Label(app, text="Phone:")
phone_entry = tk.Entry(app)
email_label = tk.Label(app, text="Email:")
email_entry = tk.Entry(app)
address_label = tk.Label(app, text="Address:")
address_entry = tk.Entry(app)

name_label.grid(row=0, column=0, padx=10, pady=5, sticky="E")
name_entry.grid(row=0, column=1, padx=10, pady=5)
phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="E")
phone_entry.grid(row=1, column=1, padx=10, pady=5)
email_label.grid(row=2, column=0, padx=10, pady=5, sticky="E")
email_entry.grid(row=2, column=1, padx=10, pady=5)
address_label.grid(row=3, column=0, padx=10, pady=5, sticky="E")
address_entry.grid(row=3, column=1, padx=10, pady=5)

# Create buttons for actions
add_button = tk.Button(app, text="Add Contact", command=add_contact)
search_label = tk.Label(app, text="Search:")
search_entry = tk.Entry(app)
search_button = tk.Button(app, text="Search", command=search_contact)
update_button = tk.Button(app, text="Update", command=update_selected_contact)
delete_button = tk.Button(app, text="Delete", command=delete_selected_contact)

add_button.grid(row=4, column=1, padx=10, pady=5)
search_label.grid(row=5, column=0, padx=10, pady=5, sticky="E")
search_entry.grid(row=5, column=1, padx=10, pady=5)
search_button.grid(row=5, column=2, padx=10, pady=5)
update_button.grid(row=6, column=0, padx=10, pady=5)
delete_button.grid(row=6, column=1, padx=10, pady=5)

# Create a listbox to display contacts
contact_listbox = tk.Listbox(app, width=40)
contact_listbox.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
contact_listbox.bind('<<ListboxSelect>>', lambda event: update_selected_contact())

# Initialize the contact list
contact_list = []

# Start the Tkinter main loop
app.mainloop()
