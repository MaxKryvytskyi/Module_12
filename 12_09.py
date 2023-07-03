'''
Реалізуйте метод __copy__ для класу Person.

Реалізуйте методи __copy__ та __deepcopy__ для класу Contacts.
'''


import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        copy_person = Person(None, None, None, None)
        copy_person.name = self.name
        copy_person.email = self.email
        copy_person.phone = self.phone
        copy_person.favorite = self.favorite
        return copy_person
            
            
class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        copy_contacts = Contacts(None)
        copy_contacts.filename = self.filename 
        copy_contacts.contacts = self.contacts 
        copy_contacts.is_unpacking = self.is_unpacking 
        copy_contacts.count_save = self.count_save
        return copy_contacts
        

    def __deepcopy__(self, memo):
        copy_contacts = Contacts(None)
        memo[id(copy_contacts)] = copy_contacts
        copy_contacts.filename = copy.deepcopy(self.filename)
        copy_contacts.contacts = copy.deepcopy(self.contacts)
        copy_contacts.is_unpacking = copy.deepcopy(self.is_unpacking)
        copy_contacts.count_save = copy.deepcopy(self.count_save)
        return copy_contacts