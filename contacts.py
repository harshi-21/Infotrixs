# contacts.py

import json

CONTACTS_FILE = "contacts.json"

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file)

def add_contact(contacts, name, phone, email):
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)

def search_contact(contacts, name):
    return contacts.get(name)

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)

def update_contact(contacts, name, phone, email):
    if name in contacts:
        contacts[name]["phone"] = phone
        contacts[name]["email"] = email
        save_contacts(contacts)
