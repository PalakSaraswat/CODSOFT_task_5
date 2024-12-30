import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

class ContactManager:
    def __init__(self, root):
        self.contacts = {}  # Store contacts as a dictionary
        
        self.bg_image = PhotoImage(file=r"C:\Users\Admin\Desktop\internship\mbg.png")  # Replace with your image path
        self.bg_label = tk.Label(root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)


        # Widgets
        self.label_title = tk.Label( text="Contact Manager", font=("Arial", 16))
        self.label_title.pack(pady=10)

        # Add Contact Section
        self.frame_add = tk.Frame(root)
        self.frame_add.pack(pady=10)

        self.label_name = tk.Label(self.frame_add, text="Name:")
        self.label_name.grid(row=0, column=0, padx=5, pady=5)
        self.entry_name = tk.Entry(self.frame_add)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        self.label_phone = tk.Label(self.frame_add, text="Phone:")
        self.label_phone.grid(row=1, column=0, padx=5, pady=5)
        self.entry_phone = tk.Entry(self.frame_add)
        self.entry_phone.grid(row=1, column=1, padx=5, pady=5)

        self.label_email = tk.Label(self.frame_add, text="Email:")
        self.label_email.grid(row=2, column=0, padx=5, pady=5)
        self.entry_email = tk.Entry(self.frame_add)
        self.entry_email.grid(row=2, column=1, padx=5, pady=5)

        self.label_address = tk.Label(self.frame_add, text="Address:")
        self.label_address.grid(row=3, column=0, padx=5, pady=5)
        self.entry_address = tk.Entry(self.frame_add)
        self.entry_address.grid(row=3, column=1, padx=5, pady=5)

        self.button_add = tk.Button(self.frame_add, text="Add Contact", command=self.add_contact)
        self.button_add.grid(row=4, columnspan=2, pady=10)

        # Contact List Section
        self.frame_list = tk.Frame(root)
        self.frame_list.pack(pady=10)

        self.label_search = tk.Label(self.frame_list, text="Search:")
        self.label_search.grid(row=0, column=0, padx=5, pady=5)
        self.entry_search = tk.Entry(self.frame_list)
        self.entry_search.grid(row=0, column=1, padx=5, pady=5)

        self.button_search = tk.Button(self.frame_list, text="Search", command=self.search_contact)
        self.button_search.grid(row=0, column=2, padx=5, pady=5)

        self.listbox_contacts = tk.Listbox(self.frame_list, width=50, height=10)
        self.listbox_contacts.grid(row=1, column=0, columnspan=3, pady=10)
        self.listbox_contacts.bind("<Double-1>", self.view_contact)

        # Buttons for Update and Delete
        self.button_update = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.button_update.pack(pady=5)

        self.button_delete = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.button_delete.pack(pady=5)

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()

        if name and phone:
            self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}
            self.refresh_contact_list()
            self.clear_fields()
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Name and Phone are required!")

    def refresh_contact_list(self):
        self.listbox_contacts.delete(0, tk.END)
        for name, details in self.contacts.items():
            self.listbox_contacts.insert(tk.END, f"{name} - {details['Phone']}")

    def clear_fields(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)
        

    def search_contact(self):
        search_term = self.entry_search.get()
        self.listbox_contacts.delete(0, tk.END)
        for name, details in self.contacts.items():
            if search_term.lower() in name.lower() or search_term in details["Phone"]:
                self.listbox_contacts.insert(tk.END, f"{name} - {details['Phone']}")

    def view_contact(self, event):
        selected = self.listbox_contacts.get(self.listbox_contacts.curselection())
        name = selected.split(" - ")[0]
        details = self.contacts.get(name)
        if details:
            messagebox.showinfo(
                "Contact Details",
                f"Name: {name}\nPhone: {details['Phone']}\nEmail: {details['Email']}\nAddress: {details['Address']}"
            )

    def update_contact(self):
        selected = self.listbox_contacts.get(self.listbox_contacts.curselection())
        name = selected.split(" - ")[0]
        if name in self.contacts:
            self.entry_name.delete(0, tk.END)
            self.entry_name.insert(0, name)

            self.entry_phone.delete(0, tk.END)
            self.entry_phone.insert(0, self.contacts[name]["Phone"])

            self.entry_email.delete(0, tk.END)
            self.entry_email.insert(0, self.contacts[name]["Email"])

            self.entry_address.delete(0, tk.END)
            self.entry_address.insert(0, self.contacts[name]["Address"])

            del self.contacts[name]

    def delete_contact(self):
        selected = self.listbox_contacts.get(self.listbox_contacts.curselection())
        name = selected.split(" - ")[0]
        if name in self.contacts:
            del self.contacts[name]
            self.refresh_contact_list()
            messagebox.showinfo("Success", "Contact deleted successfully!")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
