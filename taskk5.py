import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = []

        # UI Elements
        self.label = tk.Label(root, text="Contact Book", font=("Helvetica", 16))
        self.label.grid(row=0, column=1, pady=10)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=1, column=0, padx=10, pady=10)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=1, column=1, padx=10, pady=10)

        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=1, column=2, padx=10, pady=10)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=2, column=0, padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=2, column=1, padx=10, pady=10)

        self.exit_button = tk.Button(root, text="Exit", command=root.destroy)
        self.exit_button.grid(row=2, column=2, padx=10, pady=10)

    def add_contact(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Contact")

        # UI Elements for adding a contact
        tk.Label(add_window, text="Store Name:").grid(row=0, column=0)
        store_name_entry = tk.Entry(add_window)
        store_name_entry.grid(row=0, column=1)

        tk.Label(add_window, text="Phone Number:").grid(row=1, column=0)
        phone_number_entry = tk.Entry(add_window)
        phone_number_entry.grid(row=1, column=1)

        tk.Label(add_window, text="Email:").grid(row=2, column=0)
        email_entry = tk.Entry(add_window)
        email_entry.grid(row=2, column=1)

        tk.Label(add_window, text="Address:").grid(row=3, column=0)
        address_entry = tk.Entry(add_window)
        address_entry.grid(row=3, column=1)

        add_button = tk.Button(add_window, text="Add", command=lambda: self.save_contact(
            store_name_entry.get(), phone_number_entry.get(), email_entry.get(), address_entry.get()))
        add_button.grid(row=4, column=0, columnspan=2, pady=10)

    def save_contact(self, store_name, phone_number, email, address):
        contact = {
            "Store Name": store_name,
            "Phone Number": phone_number,
            "Email": email,
            "Address": address
        }
        self.contacts.append(contact)
        messagebox.showinfo("Contact Book", "Contact added successfully!")

    def view_contacts(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("View Contacts")

        if not self.contacts:
            tk.Label(view_window, text="No contacts available.").pack(pady=10)
        else:
            for i, contact in enumerate(self.contacts, start=1):
                contact_info = f"{i}. {contact['Store Name']} - {contact['Phone Number']}"
                tk.Label(view_window, text=contact_info).pack(pady=5)

    def search_contact(self):
        search_window = tk.Toplevel(self.root)
        search_window.title("Search Contact")

        tk.Label(search_window, text="Enter name or phone number:").pack()
        search_entry = tk.Entry(search_window)
        search_entry.pack(pady=10)

        search_button = tk.Button(search_window, text="Search", command=lambda: self.display_contact(search_entry.get()))
        search_button.pack(pady=10)

    def display_contact(self, search_term):
        search_result = []
        for contact in self.contacts:
            if search_term.lower() in contact['Store Name'].lower() or search_term in contact['Phone Number']:
                search_result.append(contact)

        display_window = tk.Toplevel(self.root)
        display_window.title("Search Result")

        if not search_result:
            tk.Label(display_window, text="No matching contacts found.").pack(pady=10)
        else:
            for i, contact in enumerate(search_result, start=1):
                contact_info = f"{i}. {contact['Store Name']} - {contact['Phone Number']}"
                tk.Label(display_window, text=contact_info).pack(pady=5)

    def update_contact(self):
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Contact")

        tk.Label(update_window, text="Enter name or phone number to update:").pack()
        update_entry = tk.Entry(update_window)
        update_entry.pack(pady=10)

        update_button = tk.Button(update_window, text="Update", command=lambda: self.edit_contact(update_entry.get()))
        update_button.pack(pady=10)

    def edit_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact['Store Name'].lower() or search_term in contact['Phone Number']:
                edit_window = tk.Toplevel(self.root)
                edit_window.title("Edit Contact")

                tk.Label(edit_window, text="Edit contact information:").pack()

                tk.Label(edit_window, text="New Store Name:").pack()
                new_store_name_entry = tk.Entry(edit_window)
                new_store_name_entry.pack()

                tk.Label(edit_window, text="New Phone Number:").pack()
                new_phone_number_entry = tk.Entry(edit_window)
                new_phone_number_entry.pack()

                tk.Label(edit_window, text="New Email:").pack()
                new_email_entry = tk.Entry(edit_window)
                new_email_entry.pack()

                tk.Label(edit_window, text="New Address:").pack()
                new_address_entry = tk.Entry(edit_window)
                new_address_entry.pack()

                save_button = tk.Button(edit_window, text="Save", command=lambda: self.save_edit(
                    contact, new_store_name_entry.get(), new_phone_number_entry.get(),
                    new_email_entry.get(), new_address_entry.get(), edit_window))
                save_button.pack(pady=10)

                return

        messagebox.showinfo("Contact Book", "No matching contact found for update.")

    def save_edit(self, contact, new_store_name, new_phone_number, new_email, new_address, edit_window):
        contact['Store Name'] = new_store_name if new_store_name else contact['Store Name']
        contact['Phone Number'] = new_phone_number if new_phone_number else contact['Phone Number']
        contact['Email'] = new_email if new_email else contact['Email']
        contact['Address'] = new_address if new_address else contact['Address']

        messagebox.showinfo("Contact Book", "Contact updated successfully!")
        edit_window.destroy()

    def delete_contact(self):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Contact")

        tk.Label(delete_window, text="Enter name or phone number to delete:").pack()
        delete_entry = tk.Entry(delete_window)
        delete_entry.pack(pady=10)

        delete_button = tk.Button(delete_window, text="Delete", command=lambda: self.remove_contact(delete_entry.get()))
        delete_button.pack(pady=10)

    def remove_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact['Store Name'].lower() or search_term in contact['Phone Number']:
                confirm = messagebox.askyesno("Delete Contact", f"Are you sure you want to delete {contact['Store Name']}?")
                if confirm:
                    self.contacts.remove(contact)
                    messagebox.showinfo("Contact Book", "Contact deleted successfully!")
                return

        messagebox.showinfo("Contact Book", "No matching contact found for deletion.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()