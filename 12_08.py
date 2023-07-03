'''
Як ви вже зрозуміли, для класу Contacts створення поверхневої копії екземпляра класу не увінчається успіхом через те, 
що ми маємо атрибут contacts, який є списком екземплярів об'єктів класу Person, а отже, всі вони будуть передані за посиланням. 
Тому необхідно використовувати глибоке копіювання методом deepcopy з пакета copy

Для класу Contacts реалізуйте функцію copy_class_contacts. 
Як параметр вона приймає екземпляр класу Contacts і повертає глибоку копію об'єкта за допомогою функції deepcopy з пакета copy.

Приклад коду:

persons = Contacts("user_class.dat", contacts)

new_persons = copy_class_contacts(persons)

new_persons.contacts[0].name = "Another name"

print(persons.contacts[0].name)  # Allen Raymond
print(new_persons.contacts[0].name)  # Another name

'''


import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
    return copy.copy(person)


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


def copy_class_contacts(contacts):
    return copy.deepcopy(contacts)



contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]



persons = Contacts("user_class.dat", contacts)

new_persons = copy_class_contacts(persons)

new_persons.contacts[0].name = "Another name"

print(persons.contacts[0].name)  # Allen Raymond
print(new_persons.contacts[0].name)  # Another name