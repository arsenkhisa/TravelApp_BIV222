"""
TravelApp
"""
from tkinter import ttk, Tk
from tkinter import font as tkfont
import configparser

from TravelApp_BIV222.tickets_page import TicketsPage
from TravelApp_BIV222.hotels_page import HotelsPage
from events_page import EventsPage
from settings_page import SettingsPage
from profile_page import ProfilePage
from TravelApp_BIV222.full_info_page import FullInfoPage


class App(Tk):
    """
    Класс создает главное окно и управляет навигацией между различными страницами.
    """

    def __init__(self, *args, **kwargs):
        """
        Инициализация главного окна.
        """
        Tk.__init__(self, *args, **kwargs)

        self.title("Tour app")  # название приложения
        self.title_font = tkfont.Font(size=20)  # шрифт заголовка
        self.resizable(width=False, height=False)  # опция изменения размера окна
        self.geometry("560x450")  # начальные размеры окна
        self.saved_info = "" # инициализация сохраненной информации
        style = ttk.Style()
        style.configure("TLabel", font=('Verdana', 14))
        # Создание главной рамки
        main_frame = ttk.Frame(self)
        main_frame.pack_propagate(False)
        main_frame.pack(side="top", fill="both", expand=True)

        # Словарь для хранения всех страниц
        self.frames = {}
        self.destination_city = None

        # Создание всех страниц
        self.create_frames(main_frame)

        # Показать начальную страницу
        self.show_frame("TicketsPage")

        # Создание кнопки для открытия окна настроек
        settings_button = ttk.Button(self, text="Settings", command=self.open_settings)
        settings_button.place(x=250, y=390)
        # Создание кнопки для открытия личного кабинета
        profile_button = ttk.Button(self, text="Profile", command=lambda:
        self.show_frame("ProfilePage"))  # кнопка профиля
        profile_button.place(x=250, y=420)

    def create_frames(self, main_frame):
        """
        Создает все страницы приложения.
        """
        for page in (TicketsPage, HotelsPage, EventsPage, FullInfoPage, ProfilePage):
            frame = page(parent=main_frame, controller=self)
            page_name = page.__name__
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def set_dates(self, when_date, back_date):
        """
        Устанавливает даты путешествия.
        """
        self.when_date = when_date
        self.back_date = back_date

    def open_settings(self):
        """
        Открывает окно настроек.
        """
        SettingsPage(self)

    def open_profile(self):
        """
        Открывает окно настроек.
        """
        ProfilePage(self, self)

    def change_theme(self):
        """
        Изменение темы
        """
        config = configparser.ConfigParser()
        config.read('settings.ini')
        current_theme = config.get('theme', 'current_theme')
        style = ttk.Style()
        themes = style.theme_names()

        if 'yummy' in themes:
            if current_theme == 'light':
                style.theme_settings("yummy", {
                    "TFrame": {"configure": {"background": "#303030"}},
                    "TLabel": {"configure": {"background": "#303030", "foreground": "#F0F0F0"}},
                    "TButton": {"configure": {"background": "#303030",
                                              "foreground": "#F0F0F0", "borderwidth": "0"}}
                })
                config.set('theme', 'current_theme', 'dark')
            else:
                style.theme_settings("yummy", {
                    "TFrame": {"configure": {"background": "#F0F0F0"}},
                    "TLabel": {"configure": {"background": "#F0F0F0", "foreground": "#303030"}},
                    "TButton": {"configure": {"background": "#F0F0F0",
                                              "foreground": "#303030", "borderwidth": "0",
                                              "relief": "solid"}}
                })
                config.set('theme', 'current_theme', 'light')
        else:
            if current_theme == 'light':
                style.theme_create("yummy", parent="alt", settings={
                    "TFrame": {"configure": {"background": "#303030"}},
                    "TLabel": {"configure": {"background": "#303030", "foreground": "#F0F0F0"}},
                    "TButton": {"configure": {"background": "#303030",
                                              "foreground": "#F0F0F0", "borderwidth": "0"}}
                })
                config.set('theme', 'current_theme', 'dark')
            else:
                style.theme_create("yummy", parent="alt", settings={
                    "TFrame": {"configure": {"background": "#F0F0F0"}},
                    "TLabel": {"configure": {"background": "#F0F0F0", "foreground": "#303030"}},
                    "TButton": {"configure": {"background": "#F0F0F0",
                                              "foreground": "#303030", "borderwidth": "0",
                                              "relief": "solid"}}
                })
                config.set('theme', 'current_theme', 'light')

        style.theme_use("yummy")

        with open('settings.ini', 'w+') as configfile:
            config.write(configfile)

    def set_destination_city(self, destination_city):
        """
        Устанавливает город назначения.
        """
        self.destination_city = destination_city

    def set_max_tickets_price(self, max_price):
        """
        Установка параметра максимальной цены
        """
        self.max_tickets_price = max_price

    def set_max_hotels_price(self, max_price):
        """
        Установка параметра максимальной цены
        """
        self.max_hotels_price = max_price

    def show_frame(self, page_name, destination_city=None):
        """
        Показывает указанную страницу.
        """
        if destination_city:
            self.set_destination_city(destination_city)
            for page in (HotelsPage, EventsPage):
                frame = self.frames[page.__name__]
                frame.update_destination_city(destination_city)
        frame = self.frames[page_name]
        frame.tkraise()

    def change_font_size(self, new_font_size):
        """
        Изменение размера шрифта
        """
        self.title_font.configure(size=new_font_size)
        for frame in self.frames.values():
            for widget in frame.winfo_children():
                font = tkfont.Font(font=widget.cget("font"))
                font.configure(size=new_font_size)
                widget.configure(font=font)

    def change_font(self, new_font_family):
        """
        Функция для изменения шрифта
        """
        new_font_size = self.title_font.cget('size')
        self.title_font.configure(family=new_font_family)  # изменяем шрифт для заголовка

        for frame in self.frames.values():
            for widget in frame.winfo_children():
                if widget.winfo_class() in ["Label", "Button", "Entry"]:
                    font = tkfont.Font(font=widget.cget("font"))
                    font.configure(family=new_font_family)
                    widget.configure(font=font)
        style = ttk.Style()
        style.configure("TLabel", font=(new_font_family, new_font_size))
        style.configure("TButton", font=(new_font_family, new_font_size))
        style.configure("TCombobox", font=(new_font_family, new_font_size))
        style.configure("TSpinbox", font=(new_font_family, new_font_size))
        # Применить новый стиль к виджетам ttk
        for frame in self.frames.values():
            for widget in frame.winfo_children():
                if widget.winfo_class() in ["TLabel", "TButton"]:
                    widget.configure(style="NewFont.TLabel")

# Запуск главного цикла обработки событий
App().mainloop()
