"""
Profile page for travel app
"""
from tkinter import BOTTOM, X, LEFT, Text, WORD, END, TOP
from tkinter import INSERT, ttk

from TravelApp_BIV222.files.database_connector import clear, show_info


class ProfilePage(ttk.Frame):
    """
    Страница профиля пользователя, показывает историю покупок.
    """

    def __init__(self, parent, controller):
        """
        Инициализация страницы профиля.
        """
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        # Создание и размещение виджетов на странице
        label = ttk.Label(self, text="Travel History", font=("Verdana", "22", "bold"))
        label.pack(side=TOP)
        self.saved_info_text = Text(self, wrap=WORD, height=10, width=30)
        self.saved_info_text.pack(fill='both', expand=True)
        bottom_frame = ttk.Frame(self)
        bottom_frame.pack(side=BOTTOM, fill=X)
        # Создание и размещение кнопки для очистки поля ввода
        clear_button = ttk.Button(bottom_frame, text="Clear", command=self.clear_button)
        clear_button.pack(side=LEFT, padx=5)
        # Создание и размещение кнопки для вывода билетов
        save_button = ttk.Button(bottom_frame, text="Show saved tickets",
                                 command=self.show_saved_tickets)
        save_button.pack(side=LEFT, padx=5)
        # Создание и размещение кнопки для вывода отелей
        save_button = ttk.Button(bottom_frame, text="Show saved hotels",
                                 command=self.show_saved_hotels)
        save_button.pack(side=LEFT, padx=5)
        # Создание и размещение кнопки для вывода мероприятий
        save_button = ttk.Button(bottom_frame, text="Show saved events",
                                 command=self.show_saved_events)
        save_button.pack(side=LEFT, padx=5)
        # Создание и размещение кнопки для возвращения в начало
        back_button = ttk.Button(bottom_frame, text="Back",
                                 command=lambda: controller.show_frame("TicketsPage"))
        back_button.pack(side=LEFT, padx=5)

    def show_saved_tickets(self):
        """
        Воспроизведение билетов
        """
        self.saved_info_text.delete(1.0, END)
        self.saved_info_text.insert(INSERT, "Saved tickets:" + "\n")
        self.rows = show_info("tickets")
        if self.rows:
            for row in self.rows:
                info = f"""
---------------
Origin: {row[1]}
Destination: {row[2]}
Airline: {row[3]}
Flight number: {row[4]}
Departure date: {row[5]}
Return date: {row[6]}
Price: {row[7]} rub
Link: https://www.aviasales.ru{row[8]}
"""
                self.saved_info_text.insert(INSERT, info)

    def show_saved_hotels(self):
        """
        Воспроизведение билетов
        """
        self.saved_info_text.delete(1.0, END)
        self.saved_info_text.insert(INSERT, "Saved hotels:" + "\n")
        self.rows = show_info("hotels")
        if self.rows:
            for row in self.rows:
                info = f"""
---------------
Hotel name: {row[1]}
Stars: {row[2]}
Check In: {row[3]}
Check Out: {row[4]}
Price: {row[5]} rub
Link: {row[6]}
"""
                self.saved_info_text.insert(INSERT, info)

    def show_saved_events(self):
        """
        Воспроизведение билетов
        """
        self.saved_info_text.delete(1.0, END)
        self.saved_info_text.insert(INSERT, "Saved events:" + "\n")
        self.rows = show_info("events")
        if self.rows:
            for row in self.rows:
                info = f"""
---------------
City: {row[1]}
Title: {row[2]}
Tagline: {row[3]}
Duration: {row[5]}
Price: {row[6]}
Link: {row[7]}
"""
                self.saved_info_text.insert(INSERT, info)

    def show_saved_info(self):
        """
        Воспроизведение информации
        """
        self.saved_info_text.delete(1.0, END)
        if self.controller.saved_info:
            self.saved_info_text.insert(INSERT, self.controller.saved_info)

    def clear_saved_info(self):
        """
        Очистка информации
        """
        self.controller.saved_info = ""
        self.show_saved_info()

    def clear_button(self):
        """
        Функция, объединяющая две другие
        """
        self.clear_saved_info()
        clear()

    def tkraise(self, aboveThis=None):
        self.show_saved_info()
        super().tkraise(aboveThis)
