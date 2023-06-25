"""
Hotels page for travel app
"""
from datetime import datetime
from tkinter import ttk, StringVar
from tkcalendar import DateEntry

import hotel_api
from city_codes import get_city_code


class HotelsPage(ttk.Frame):
    """
    Окно с информацией о бронировании отеля.
    """

    def __init__(self, parent, controller):
        """
        Инициализация класса HotelsPage.

        Args:
            parent: родительский виджет.
            controller: контроллер приложения.
        """
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.destination_city = StringVar()
        self.create_widgets()

    def update_destination_city(self, destination_city):
        """
        Обновить город назначения.

        Args:
            destination_city (str): новый город назначения.
        """
        self.destination_city.set(destination_city)

    def set_guests(self, guests):
        """
        Установить количество гостей.

        Args:
            guests (int): новое количество гостей.
        """
        self.guest_number_combobox.set(guests)

    def create_widgets(self):
        """
        Создание виджетов для страницы бронирования отеля.
        """
        # Пометка с вводом деталей отеля
        label = ttk.Label(self, text='Enter hotel information', font=("Verdana", "22", "bold"))
        label.place(x=80, y=20)

        # Метка и поле ввода для города
        city_name_label = ttk.Label(self, text='City')
        city_name_label.place(x=20, y=100)
        cities = ["Chelyabinsk", "Volgograd", "Kazan", "Krasnojarsk", "Moscow", "Omsk", "Sochi",
                  "Nizhniy Novgorod", "Novosibirsk", "Perm",
                  "Saint Petersburg", "Samara", "Ufa", "Yekaterinburg"]
        cities.sort()
        city_combobox = ttk.Combobox(self, width=12, values=cities,
                                     textvariable=self.destination_city)
        city_combobox.set(self.destination_city)
        city_combobox.place(x=380, y=100)

        # Метки и поля ввода для дат прибытия и отъезда
        arrival_date_label = ttk.Label(self, text='Check-in date')
        arrival_date_label.place(x=20, y=140)
        self.arrival_date_entry = DateEntry(self, width=12, foreground='white')
        self.arrival_date_entry.place(x=380, y=140)
        departure_date_label = ttk.Label(self, text='Eviction date')
        departure_date_label.place(x=20, y=180)
        self.departure_date_entry = DateEntry(self, width=12, foreground='white')
        self.departure_date_entry.place(x=380, y=180)

        # Метка и поле ввода для количества гостей
        guest_number_label = ttk.Label(self, text='Number of guests')
        guest_number_label.place(x=20, y=220)
        guests = ["1", "2", "3", "4", "5"]
        self.guest_number_combobox = ttk.Combobox(self, width=12, values=guests)
        self.guest_number_combobox.place(x=380, y=220)

        # Метка и поле ввода для максимальной цены
        max_hotels_price_label = ttk.Label(self, text='Maximum price')
        max_hotels_price_label.place(x=20, y=260)

        self.max_hotels_price_combobox = ttk.Spinbox(self, width=12, from_=1000.0,
                                                     to=1000000, increment=500)
        self.max_hotels_price_combobox.place(x=380, y=260)

        # Кнопки для перехода к следующему шагу и возврата назад
        first_button = ttk.Button(self, text='Next',
                                  command=lambda: [self.on_click_button(),
                                                   self.controller.show_frame(
                                                       "EventsPage", self.destination_city.get())])
        first_button.place(x=380, y=300)
        second_button = ttk.Button(self, text='Back',
                                   command=lambda: self.controller.show_frame("TicketsPage"))
        second_button.place(x=80, y=300)

    def get_max_hotels_price(self):
        """
        Функция для сохранения максимальной цены на отель
        """
        return self.max_hotels_price_combobox.get()

    def update_dates(self, when_date_str, back_date_str):
        """
        Обновить даты прибытия и отъезда.
        """
        when_date_obj = datetime.strptime(when_date_str, "%Y-%m-%d")
        back_date_obj = datetime.strptime(back_date_str, "%Y-%m-%d")
        self.arrival_date_entry.set_date(when_date_obj)
        self.departure_date_entry.set_date(back_date_obj)

    def on_click_button(self):
        """
        Выполнить при нажатии кнопки.
        """
        destination = get_city_code(self.destination_city.get())
        departure_date = self.arrival_date_entry.get_date().strftime("%Y-%m-%d")
        return_date = self.departure_date_entry.get_date().strftime("%Y-%m-%d")
        adults = int(self.guest_number_combobox.get())
        hotels = hotel_api.search_hotels(destination, departure_date, return_date, adults)
        max_hotels_price = self.get_max_hotels_price()
        self.controller.set_max_hotels_price(max_hotels_price)
        self.controller.frames["FullInfoPage"].update_hotels_info(hotels)
        self.controller.show_frame("FullInfoPage")
