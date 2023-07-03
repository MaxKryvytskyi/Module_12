'''
Ми продовжимо розширювати приклад попереднього завдання. 
Додайте до класу Contacts атрибут count_save, за замовчуванням він повинен мати значення 0. 
Реалізуйте магічний метод __getstate__ для класу Contacts. 
При упаковуванні екземпляра метод класу повинен збільшувати значення атрибута count_save на одиницю. 
Таким чином, ця властивість - лічильник повторних операцій пакування екземпляра класу

Приклад роботи коду:

persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
first = persons.read_from_file()
first.save_to_file()
second = first.read_from_file()
second.save_to_file()
third = second.read_from_file()

print(persons.count_save)  # 0
print(first.count_save)  # 1
print(second.count_save)  # 2
print(third.count_save)  # 3
'''

import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    
    def __init__(self, filename: str, contacts: list[Person] = None):
        self.count_save = 0
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        

    def save_to_file(self):
        
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
            return content

    def __getstate__(self):
        copy_self = self.__dict__.copy()
        copy_self['count_save'] = copy_self['count_save'] + 1
        return copy_self
    

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
persons.save_to_file()
first = persons.read_from_file()
first.save_to_file()
second = first.read_from_file()
second.save_to_file()
third = second.read_from_file()

print(persons.count_save)  # 0
print(first.count_save)  # 1
print(second.count_save)  # 2
print(third.count_save)  # 3