from tkinter import *
import customtkinter as ctk
import os
from adminMain import AdminMainMenu


class AddUser(ctk.CTk):

    WIDTH = 412
    HEIGHT = 640

    usercount = 0

    def __init__(self):
        super().__init__()

        self.title("Менеджер семейного бюджета")

        w = self.WIDTH
        h = self.HEIGHT
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2 - 150
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed
        self.initUI()

    def initUI(self):
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        self.label_create_account = ctk.CTkLabel(master=self, text="Добавить\n"
                                                                   "пользователя", text_font=("Arial", 28))
        self.label_create_account.grid(row=1, column=1)

        self.entry_email = ctk.CTkEntry(master=self, width=240, height=80, text_font=("Arial", -20))
        self.entry_email.insert(END, "E-mail")
        self.entry_email.grid(row=2, column=1)

        self.button_add_user = ctk.CTkButton(master=self, text="Добавить ещё одного пользователя", command=self.add,
                                            width=240, height=80, text_font=("Arial", -20))
        self.button_add_user.grid(row=3, column=1)

        self.button_next = ctk.CTkButton(master=self, text="Далее", width=240, height=80, command=self.next,
                                         text_font=("Arial", -20))
        self.button_next.grid(row=4, column=1)

        ctk.CTkLabel(text="").grid(row=0, column=1)
        ctk.CTkLabel(text="").grid(row=5, column=1)

    def on_closing(self, event=0):
        self.destroy()

    def add(self):
        self.usercount += 1
        self.entry_email.delete(0, END)
        self.entry_email.insert(END, str(self.usercount))

    def next(self):
        self.destroy()
        add_user = AdminMainMenu()
        add_user.mainloop()

# app = AddUser()
# app.mainloop()


