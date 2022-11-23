from tkinter import *
import customtkinter as ctk
import os
from PIL import Image, ImageTk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


PATH = os.path.dirname(os.path.realpath(__file__))
image_down = Image.open(PATH + '\\images\\down.png').resize((60, 60))
image_up = Image.open(PATH + '\\images\\up.png').resize((60, 60))


class AdminMainMenu(ctk.CTk):

    WIDTH = 412
    HEIGHT = 640

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
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        self.button_display_entries = ctk.CTkButton(master=self, text="Просмотреть записи", width=240, height=80,
                                         command=self.display_entries, text_font=("Arial", -20))
        self.button_display_entries.grid(row=1, column=1)

        self.button_add = ctk.CTkButton(master=self, text="Добавить запись", width=240, height=80, command=self.add,
                                         text_font=("Arial", -20))
        self.button_add.grid(row=2, column=1)

        self.button_edit = ctk.CTkButton(master=self, text="Изменить запись", width=240, height=80, command=self.edit,
                                         text_font=("Arial", -20))
        self.button_edit.grid(row=3, column=1)

        self.button_delete = ctk.CTkButton(master=self, text="Удалить запись", width=240, height=80,
                                           command=self.delete, text_font=("Arial", -20))
        self.button_delete.grid(row=4, column=1)

        self.button_stats = ctk.CTkButton(master=self, text="Просмотреть статистику",
                                          width=240, height=80, command=self.stats, text_font=("Arial", -20))
        self.button_stats.grid(row=5, column=1)

        ctk.CTkLabel(text="").grid(row=0, column=1)
        ctk.CTkLabel(text="").grid(row=6, column=1)

    def on_closing(self, event=0):
        self.destroy()

    def add(self):
        self.destroy()
        add_user = AddEntry()
        add_user.mainloop()

    def delete(self):
        self.destroy()
        add_user = DeleteEntry()
        add_user.mainloop()

    def edit(self):
        self.destroy()
        edit_entry = ChooseEntryToEdit()
        edit_entry.mainloop()

    def stats(self):
        self.destroy()
        show_stats = SetStatsParameters()
        show_stats.mainloop()

    def display_entries(self):
        self.destroy()
        add_user = DisplayEntries()
        add_user.mainloop()


class DeleteEntry(ctk.CTk):

    WIDTH = 412
    HEIGHT = 640

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
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self.picture_down = ImageTk.PhotoImage(image_down)
        self.picture_up = ImageTk.PhotoImage(image_up)

        self.check1 = ctk.CTkCheckBox(master=self, text='')
        self.check1.grid(row=1, column=0, padx=20)

        self.frame1 = ctk.CTkFrame(master=self, height=100)
        self.frame1.grid(row=1, column=1, columnspan=3)
        self.frame1.grid_rowconfigure((0, 1, 2), weight=1)
        self.frame1.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.down_label1 = ctk.CTkLabel(master=self.frame1, image=self.picture_down, width=65)
        self.down_label1.grid(row=0, column=0, rowspan=3, sticky="w")
        self.label_date1 = ctk.CTkLabel(master=self.frame1, text="Дата 1")
        self.label_date1.grid(row=0, column=3)
        self.label_sum1 = ctk.CTkLabel(master=self.frame1, text="Сумма 1")
        self.label_sum1.grid(row=1, column=1)
        self.label_author1 = ctk.CTkLabel(master=self.frame1, text="Автор 1")
        self.label_author1.grid(row=2, column=3, columnspan=3)
        self.label_comment1 = ctk.CTkLabel(master=self.frame1, text="Комментарий: купил слона")
        self.label_comment1.grid(row=3, column=0, columnspan=4, sticky="w", padx=15)

        self.check2 = ctk.CTkCheckBox(master=self, text='')
        self.check2.grid(row=2, column=0, padx=20)

        self.frame2 = ctk.CTkFrame(master=self, height=100)
        self.frame2.grid(row=2, column=1, columnspan=3)
        self.frame2.grid_rowconfigure((0, 1, 2), weight=1)
        self.frame2.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.down_label2 = ctk.CTkLabel(master=self.frame2, image=self.picture_down, width=65)
        self.down_label2.grid(row=0, column=0, rowspan=3, sticky="w")
        self.label_date2 = ctk.CTkLabel(master=self.frame2, text="Дата 2")
        self.label_date2.grid(row=0, column=3)
        self.label_sum2 = ctk.CTkLabel(master=self.frame2, text="Сумма 2")
        self.label_sum2.grid(row=1, column=1)
        self.label_author2 = ctk.CTkLabel(master=self.frame2, text="Автор 2")
        self.label_author2.grid(row=2, column=3, columnspan=3)
        self.label_comment2 = ctk.CTkLabel(master=self.frame2, text="Комментарий: купил булочку")
        self.label_comment2.grid(row=3, column=0, columnspan=4, sticky="w", padx=15)

        self.check3 = ctk.CTkCheckBox(master=self, text='')
        self.check3.grid(row=3, column=0, padx=20)

        self.frame3 = ctk.CTkFrame(master=self, height=100)
        self.frame3.grid(row=3, column=1, columnspan=3)
        self.frame3.grid_rowconfigure((0, 1, 2), weight=1)
        self.frame3.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.up_label3 = ctk.CTkLabel(master=self.frame3, image=self.picture_up, width=65)
        self.up_label3.grid(row=0, column=0, rowspan=3, sticky="w")
        self.label_date3 = ctk.CTkLabel(master=self.frame3, text="Дата 3")
        self.label_date3.grid(row=0, column=3)
        self.label_sum3 = ctk.CTkLabel(master=self.frame3, text="Сумма 3")
        self.label_sum3.grid(row=1, column=1)
        self.label_author3 = ctk.CTkLabel(master=self.frame3, text="Автор 3")
        self.label_author3.grid(row=2, column=3, columnspan=3)
        self.label_comment3 = ctk.CTkLabel(master=self.frame3, text="Комментарий: продал почку")
        self.label_comment3.grid(row=3, column=0, columnspan=4, sticky="w", padx=15)

        ctk.CTkLabel(text="", master=self, width=20).grid(row=0, rowspan=3, column=4)

        self.button_delete = ctk.CTkButton(text="Удалить выбранные записи", command=self.next, width=240, height=80,
                                           text_font=("Arial", -20))
        self.button_delete.grid(row=4, column=0, columnspan=5)

        self.button_back = ctk.CTkButton(text="Назад", command=self.back, width=120, height=40,
                                         text_font=("Arial", -20))
        self.button_back.grid(row=5, column=0, columnspan=5)

    def on_closing(self, event=0):
        self.destroy()

    def next(self):
        pass

    def back(self):
        self.destroy()
        add_user = AdminMainMenu()
        add_user.mainloop()


class DisplayEntries(ctk.CTk):

    WIDTH = 412
    HEIGHT = 640

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
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self.picture_down = ImageTk.PhotoImage(image_down)
        self.picture_up = ImageTk.PhotoImage(image_up)

        self.frame1 = ctk.CTkFrame(master=self, height=100)
        self.frame1.grid(row=1, column=0, columnspan=3)
        self.frame1.grid_rowconfigure((0, 1, 2), weight=1)
        self.frame1.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.down_label1 = ctk.CTkLabel(master=self.frame1, image=self.picture_down, width=65)
        self.down_label1.grid(row=0, column=0, rowspan=3, sticky="w")
        self.label_date1 = ctk.CTkLabel(master=self.frame1, text="Дата 1")
        self.label_date1.grid(row=0, column=3)
        self.label_sum1 = ctk.CTkLabel(master=self.frame1, text="Сумма 1")
        self.label_sum1.grid(row=1, column=1)
        self.label_author1 = ctk.CTkLabel(master=self.frame1, text="Автор 1")
        self.label_author1.grid(row=2, column=3, columnspan=3)
        self.label_comment1 = ctk.CTkLabel(master=self.frame1, text="Комментарий: купил слона")
        self.label_comment1.grid(row=3, column=0, columnspan=4, sticky="w", padx=15)

        self.frame2 = ctk.CTkFrame(master=self, height=100)
        self.frame2.grid(row=2, column=0, columnspan=3)
        self.frame2.grid_rowconfigure((0, 1, 2), weight=1)
        self.frame2.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.down_label2 = ctk.CTkLabel(master=self.frame2, image=self.picture_down, width=65)
        self.down_label2.grid(row=0, column=0, rowspan=3, sticky="w")
        self.label_date2 = ctk.CTkLabel(master=self.frame2, text="Дата 2")
        self.label_date2.grid(row=0, column=3)
        self.label_sum2 = ctk.CTkLabel(master=self.frame2, text="Сумма 2")
        self.label_sum2.grid(row=1, column=1)
        self.label_author2 = ctk.CTkLabel(master=self.frame2, text="Автор 2")
        self.label_author2.grid(row=2, column=3, columnspan=3)
        self.label_comment2 = ctk.CTkLabel(master=self.frame2, text="Комментарий: купил булочку")
        self.label_comment2.grid(row=3, column=0, columnspan=4, sticky="w", padx=15)

        self.frame3 = ctk.CTkFrame(master=self, height=100)
        self.frame3.grid(row=3, column=0, columnspan=3)
        self.frame3.grid_rowconfigure((0, 1, 2), weight=1)
        self.frame3.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.up_label3 = ctk.CTkLabel(master=self.frame3, image=self.picture_up, width=65)
        self.up_label3.grid(row=0, column=0, rowspan=3, sticky="w")
        self.label_date3 = ctk.CTkLabel(master=self.frame3, text="Дата 3")
        self.label_date3.grid(row=0, column=3)
        self.label_sum3 = ctk.CTkLabel(master=self.frame3, text="Сумма 3")
        self.label_sum3.grid(row=1, column=1)
        self.label_author3 = ctk.CTkLabel(master=self.frame3, text="Автор 3")
        self.label_author3.grid(row=2, column=3, columnspan=3)
        self.label_comment3 = ctk.CTkLabel(master=self.frame3, text="Комментарий: продал почку")
        self.label_comment3.grid(row=3, column=0, columnspan=4, sticky="w", padx=15)

        self.frame4 = ctk.CTkFrame(master=self, height=100)
        self.frame4.grid(row=4, column=0, columnspan=3)
        self.frame4.grid_rowconfigure((0, 1, 2), weight=1)
        self.frame4.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.up_label4 = ctk.CTkLabel(master=self.frame4, image=self.picture_down, width=65)
        self.up_label4.grid(row=0, column=0, rowspan=3, sticky="w")
        self.label_date4 = ctk.CTkLabel(master=self.frame4, text="Дата 4")
        self.label_date4.grid(row=0, column=3)
        self.label_sum4 = ctk.CTkLabel(master=self.frame4, text="Сумма 4")
        self.label_sum4.grid(row=1, column=1)
        self.label_author4 = ctk.CTkLabel(master=self.frame4, text="Автор 4")
        self.label_author4.grid(row=2, column=3, columnspan=3)
        self.label_comment4 = ctk.CTkLabel(master=self.frame4, text="Комментарий: купил видеокарту")
        self.label_comment4.grid(row=3, column=0, columnspan=4, sticky="w", padx=15)

        # ctk.CTkLabel(text="", master=self, width=20).grid(row=0, rowspan=3, column=4)

        self.button_back = ctk.CTkButton(text="Назад", command=self.back, width=120, height=40,
                                         text_font=("Arial", -20))
        self.button_back.grid(row=5, column=0, columnspan=5)

    def on_closing(self, event=0):
        self.destroy()

    def back(self):
        self.destroy()
        add_user = AdminMainMenu()
        add_user.mainloop()

    def next(self):
        pass


class AddEntry(ctk.CTk):

    WIDTH = 412
    HEIGHT = 640

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
        self.grid_columnconfigure((0, 1), weight=1)

        self.picture_down = ImageTk.PhotoImage(image_down)
        self.picture_up = ImageTk.PhotoImage(image_up)

        ctk.set_default_color_theme("green")
        self.button_gain = ctk.CTkButton(master=self, width=140, height=50, text_font=("Arial", -16),
                                         text="Поступление", image=self.picture_up, command=self.up)
        self.button_gain.grid(row=1, column=0, padx=5)

        ctk.set_default_color_theme("dark-blue")
        self.button_down = ctk.CTkButton(master=self, width=140, height=50, text_font=("Arial", -16),
                                         text="Списание", image=self.picture_down, command=self.down)
        self.button_down.grid(row=1, column=1)

        ctk.set_default_color_theme("green")
        self.entry_sum = ctk.CTkEntry(master=self, width=240, height=80, text_font=("Arial", -20))
        self.entry_sum.insert(END, "Введите сумму")
        self.entry_sum.grid(row=2, column=0, columnspan=2)

        self.entry_currency = ctk.CTkEntry(master=self, width=240, height=60, text_font=("Arial", -20))
        self.entry_currency.insert(END, "Введите валюту")
        self.entry_currency.grid(row=3, column=0, columnspan=2)

        self.entry_comment = ctk.CTkEntry(master=self, width=280, height=160, text_font=("Arial", -20))
        self.entry_comment.insert(END, "Комментарий")
        self.entry_comment.grid(row=4, column=0, columnspan=2)

        self.button_add = ctk.CTkButton(master=self, text="Добавить запись", width=240, height=80, command=self.next,
                                         text_font=("Arial", -20))
        self.button_add.grid(row=5, column=0, columnspan=2)

        self.button_back = ctk.CTkButton(text="Назад", command=self.back, width=120, height=40,
                                         text_font=("Arial", -20))
        self.button_back.grid(row=6, column=0, columnspan=2)

        ctk.CTkLabel(text="").grid(row=0, column=0, columnspan=2)
        ctk.CTkLabel(text="").grid(row=7, column=1)

    def on_closing(self, event=0):
        self.destroy()

    def down(self):
        pass

    def up(self):
        pass

    def back(self):
        self.destroy()
        add_user = AdminMainMenu()
        add_user.mainloop()

    def next(self):
        # print(PATH + "\\addUser.py")
        # os.startfile(PATH+"\\addUser.py")
        pass


class ChooseEntryToEdit(ctk.CTk):

    WIDTH = 412
    HEIGHT = 640

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
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self.picture_down = ImageTk.PhotoImage(image_down)
        self.picture_up = ImageTk.PhotoImage(image_up)

        self.button1 = ctk.CTkButton(master=self, text='Изм.', command=self.open1, width=60)
        self.button1.grid(row=1, column=0, padx=20)

        self.frame1 = ctk.CTkFrame(master=self, height=100)
        self.frame1.grid(row=1, column=1, columnspan=3)
        self.frame1.grid_rowconfigure((0, 1, 2), weight=1)
        self.frame1.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.down_label1 = ctk.CTkLabel(master=self.frame1, image=self.picture_down, width=65)
        self.down_label1.grid(row=0, column=0, rowspan=3, sticky="w")
        self.label_date1 = ctk.CTkLabel(master=self.frame1, text="Дата 1")
        self.label_date1.grid(row=0, column=3)
        self.label_sum1 = ctk.CTkLabel(master=self.frame1, text="Сумма 1")
        self.label_sum1.grid(row=1, column=1)
        self.label_author1 = ctk.CTkLabel(master=self.frame1, text="Автор 1")
        self.label_author1.grid(row=2, column=3, columnspan=3)
        self.label_comment1 = ctk.CTkLabel(master=self.frame1, text="Комментарий: купил слона")
        self.label_comment1.grid(row=3, column=0, columnspan=4, sticky="w", padx=15)

        self.button2 = ctk.CTkButton(master=self, text='Изм.', command=self.open2, width=60)
        self.button2.grid(row=2, column=0, padx=20)

        self.frame2 = ctk.CTkFrame(master=self, height=100)
        self.frame2.grid(row=2, column=1, columnspan=3)
        self.frame2.grid_rowconfigure((0, 1, 2), weight=1)
        self.frame2.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.down_label2 = ctk.CTkLabel(master=self.frame2, image=self.picture_down, width=65)
        self.down_label2.grid(row=0, column=0, rowspan=3, sticky="w")
        self.label_date2 = ctk.CTkLabel(master=self.frame2, text="Дата 2")
        self.label_date2.grid(row=0, column=3)
        self.label_sum2 = ctk.CTkLabel(master=self.frame2, text="Сумма 2")
        self.label_sum2.grid(row=1, column=1)
        self.label_author2 = ctk.CTkLabel(master=self.frame2, text="Автор 2")
        self.label_author2.grid(row=2, column=3, columnspan=3)
        self.label_comment2 = ctk.CTkLabel(master=self.frame2, text="Комментарий: купил булочку")
        self.label_comment2.grid(row=3, column=0, columnspan=4, sticky="w", padx=15)

        self.button3 = ctk.CTkButton(master=self, text='Изм.', command=self.open3, width=60)
        self.button3.grid(row=3, column=0, padx=20)

        self.frame3 = ctk.CTkFrame(master=self, height=100)
        self.frame3.grid(row=3, column=1, columnspan=3)
        self.frame3.grid_rowconfigure((0, 1, 2), weight=1)
        self.frame3.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.up_label3 = ctk.CTkLabel(master=self.frame3, image=self.picture_up, width=65)
        self.up_label3.grid(row=0, column=0, rowspan=3, sticky="w")
        self.label_date3 = ctk.CTkLabel(master=self.frame3, text="Дата 3")
        self.label_date3.grid(row=0, column=3)
        self.label_sum3 = ctk.CTkLabel(master=self.frame3, text="Сумма 3")
        self.label_sum3.grid(row=1, column=1)
        self.label_author3 = ctk.CTkLabel(master=self.frame3, text="Автор 3")
        self.label_author3.grid(row=2, column=3, columnspan=3)
        self.label_comment3 = ctk.CTkLabel(master=self.frame3, text="Комментарий: продал почку")
        self.label_comment3.grid(row=3, column=0, columnspan=4, sticky="w", padx=15)

        ctk.CTkLabel(text="", master=self, width=20).grid(row=0, rowspan=3, column=4)

        self.button_back = ctk.CTkButton(text="Назад", command=self.back, width=120, height=40,
                                         text_font=("Arial", -20))
        self.button_back.grid(row=4, column=0, columnspan=5)

    def on_closing(self, event=0):
        self.destroy()

    def open1(self):
        self.open(1)

    def open2(self):
        self.open(2)

    def open3(self):
        self.open(3)

    def open(self, number):
        self.destroy()
        add_user = EditEntry(number-1)
        add_user.mainloop()

    def back(self):
        self.destroy()
        add_user = AdminMainMenu()
        add_user.mainloop()


class EditEntry(ctk.CTk):

    WIDTH = 412
    HEIGHT = 640

    comment_list = ["Купил слона", "Купил булочку", "Продал почку"]

    def __init__(self, number):
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
        self.initUI(number)

    def initUI(self, number):
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.picture_down = ImageTk.PhotoImage(image_down)
        self.picture_up = ImageTk.PhotoImage(image_up)

        ctk.set_default_color_theme("green")
        self.button_gain = ctk.CTkButton(master=self, width=140, height=50, text_font=("Arial", -16),
                                         text="Поступление", image=self.picture_up, command=self.up)
        self.button_gain.grid(row=1, column=0, padx=5)

        ctk.set_default_color_theme("dark-blue")
        self.button_down = ctk.CTkButton(master=self, width=140, height=50, text_font=("Arial", -16),
                                         text="Списание", image=self.picture_down, command=self.down)
        self.button_down.grid(row=1, column=1)

        ctk.set_default_color_theme("green")
        self.entry_sum = ctk.CTkEntry(master=self, width=240, height=80, text_font=("Arial", -20))
        self.entry_sum.insert(END, "Введите сумму")
        self.entry_sum.grid(row=2, column=0, columnspan=2)

        self.entry_currency = ctk.CTkEntry(master=self, width=240, height=60, text_font=("Arial", -20))
        self.entry_currency.insert(END, "Введите валюту")
        self.entry_currency.grid(row=3, column=0, columnspan=2)

        self.entry_comment = ctk.CTkEntry(master=self, width=280, height=160, text_font=("Arial", -20))
        self.entry_comment.insert(END, self.comment_list[number])
        self.entry_comment.grid(row=4, column=0, columnspan=2)

        self.button_edit = ctk.CTkButton(master=self, text="Изменить запись", width=240, height=80, command=self.next,
                                         text_font=("Arial", -20))
        self.button_edit.grid(row=5, column=0, columnspan=2)

        self.button_back = ctk.CTkButton(text="Назад", command=self.back, width=120, height=40,
                                         text_font=("Arial", -20))
        self.button_back.grid(row=6, column=0, columnspan=2)

        ctk.CTkLabel(text="").grid(row=0, column=0, columnspan=2)
        ctk.CTkLabel(text="").grid(row=7, column=1)

    def on_closing(self, event=0):
        self.destroy()

    def next(self):
        pass

    def down(self):
        pass

    def up(self):
        pass

    def back(self):
        self.destroy()
        add_user = ChooseEntryToEdit()
        add_user.mainloop()


class SetStatsParameters(ctk.CTk):

    WIDTH = 412
    HEIGHT = 640

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
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        self.label_make_stats = ctk.CTkLabel(master=self, text="Составить статистику\nза период",
                                             text_font=("Arial", 28))
        self.label_make_stats.grid(row=0, column=1)

        self.entry_start = ctk.CTkEntry(master=self, width=240, height=80, text_font=("Arial", -20))
        self.entry_start.insert(END, "Дата начала")
        self.entry_start.grid(row=1, column=1)

        self.entry_end = ctk.CTkEntry(master=self, width=240, height=80, text_font=("Arial", -20))
        self.entry_end.insert(END, "Дата окончания")
        self.entry_end.grid(row=2, column=1)

        self.label_currency = ctk.CTkLabel(master=self, text="Валюта:",
                                           text_font=("Arial", 28))
        self.label_currency.grid(row=3, column=1)

        self.entry_currency = ctk.CTkEntry(master=self, width=240, height=80, text_font=("Arial", -20))
        self.entry_currency.insert(END, "Введите валюту")
        self.entry_currency.grid(row=4, column=1)

        self.button_next = ctk.CTkButton(master=self, text="Далее", width=240, height=80, command=self.next,
                                         text_font=("Arial", -20))
        self.button_next.grid(row=5, column=1)

        self.button_back = ctk.CTkButton(text="Назад", command=self.back, width=120, height=40,
                                         text_font=("Arial", -20))
        self.button_back.grid(row=6, column=0, columnspan=2)

    def on_closing(self, event=0):
        self.destroy()

    def next(self):
        self.destroy()
        next_app = ShowDiagrams()
        next_app.mainloop()

    def back(self):
        self.destroy()
        go_back = AdminMainMenu()
        go_back.mainloop()


class ShowDiagrams(ctk.CTk):

    WIDTH = 412
    HEIGHT = 640

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

        self.button_back = ctk.CTkButton(text="Назад", command=self.back, width=120, height=40,
                                         text_font=("Arial", -20))
        self.button_back.grid(row=6, column=0, columnspan=3, pady=20)

        self.draw_diagrams()

    def draw_diagrams(self):
        data1 = {'Дата': ['01.02', '02.03', '03.04'],
                 'Сумма Потрачено':     [12, 9, 31],
                 'Сумма Получено':      [4, 11, 13]}
        df1 = pd.DataFrame(data1)

        figure = plt.Figure(figsize=(6, 5), dpi=100)
        ax = figure.add_subplot(111)
        chart_type = FigureCanvasTkAgg(figure, self)
        chart_type.get_tk_widget().grid(row=0, column=1, rowspan=5)
        df = df1[['Дата', 'Сумма Потрачено', 'Сумма Получено']].groupby('Дата').sum()
        print(df)
        df.plot(kind='bar', legend=True, ax=ax)
        ax.set_title('Статистика')

    def on_closing(self, event=0):
        self.destroy()

    def back(self):
        self.destroy()
        go_back = SetStatsParameters()
        go_back.mainloop()
        # pass


class MainMenu(ctk.CTk):
    WIDTH = 412
    HEIGHT = 640

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
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        self.button_display = ctk.CTkButton(master=self, text="Просмотреть записи", width=240, height=80,
                                            command=self.display_entries, text_font=("Arial", -20))
        self.button_display.grid(row=1, column=1)

        self.button_add = ctk.CTkButton(master=self, text="Добавить запись", width=240, height=80, command=self.add,
                                        text_font=("Arial", -20))
        self.button_add.grid(row=2, column=1)

        self.button_edit = ctk.CTkButton(master=self, text="Изменить запись", width=240, height=80, command=self.edit,
                                         text_font=("Arial", -20))
        self.button_edit.grid(row=3, column=1)

        self.button_stats = ctk.CTkButton(master=self, text="Просмотреть статистику",
                                          width=240, height=80, command=self.stats, text_font=("Arial", -20))
        self.button_stats.grid(row=5, column=1)

        ctk.CTkLabel(text="").grid(row=0, column=1)
        ctk.CTkLabel(text="").grid(row=6, column=1)

    def on_closing(self, event=0):
        self.destroy()

    def next(self):
        pass

    def add(self):
        self.destroy()
        add_user = AddEntry()
        add_user.mainloop()

    def delete(self):
        self.destroy()
        add_user = DeleteEntry()
        add_user.mainloop()

    def edit(self):
        self.destroy()
        edit_entry = ChooseEntryToEdit()
        edit_entry.mainloop()

    def stats(self):
        self.destroy()
        show_stats = SetStatsParameters()
        show_stats.mainloop()

    def display_entries(self):
        self.destroy()
        add_user = DisplayEntries()
        add_user.mainloop()
