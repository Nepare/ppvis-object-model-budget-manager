import datetime
from tkinter import *
import customtkinter as ctk
import os
from createAccountScreen import CreateAccountScreen
from addUser import AddUser
from adminMain import AdminMainMenu
from enum import Enum
from datetime import datetime

PATH = os.path.dirname(os.path.realpath(__file__))

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class EntryType(Enum):
    GAIN = 1
    LOSS = -1


class FamilyMember:
    def __init__(self, id, login, mail, password, entry_list):
        self.id = id
        self.login = login
        self.mail = mail
        self.password = password
        self.entry_list = entry_list


class HeadOfFamily(FamilyMember):
    status: str


class Entry:
    def __init__(self, type: EntryType, sum: float, currency: str, author: FamilyMember, date: datetime, comment: str):
        self.type = type
        self.sum = sum
        self.currency = currency
        self.author = author
        self.date = date
        self.comment = comment


class EntryStorage:
    def __init__(self, list_of_entries):
        self.list_of_entries = list_of_entries


class UserStorage:
    def __init__(self, user_list, admin):
        self.user_list = user_list
        self.admin = admin


class MyModel:
    def __init__(self, user_storage):
        self.user_storage = user_storage

    def add_user(self, family_member):
        pass

    def check(self, user, login, password):
        pass

    def get_users(self):
        return self.user_storage

    def display_stats(self):
        pass


class EntryModel:
    def __init__(self, user_storage, entry_storage):
        self.user_storage = user_storage
        self.entry_storage = entry_storage

    def add_entry(self, entry):
        self.entry_storage.append(entry)

    def delete_entry(self, entry_list):
        pass

    def get_entries(self):
        return self.entry_storage


class EntryController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_entries(self):
        pass

    def add_entry(self, entry):
        pass

    def edit_entry(self, entry):
        pass

    def delete_entry(self, entry_list):
        pass


class MyController:
    def __init__(self, model, view, entry_controller):
        self.model = model
        self.view = view
        self.entry_controller = entry_controller

    def update(self):
        pass

    def build(self):
        pass

    def add_user(self, mail: str):
        pass

    def display_stats(self, start_date: datetime, end_data: datetime, currency: str):
        pass

    def get_info(self):
        pass


class PassMVC:
    def __init__(self):
        self.model1 = MyModel([])
        self.model2 = EntryModel([], [])
        self.controller2 = EntryController(self.model2, NONE)
        self.controller1 = MyController(self.model1, NONE, self.controller2)

    def display_screen(self):
        pass


class MainClass:
    def start(self):
        screen_create_account = CreateAccountScreen()
        screen_create_account.mainloop()

    def create_controllers(self):
        pass

    def create_models(self):
        pass


if __name__ == "__main__":
    app = MainClass()
    app.start()
