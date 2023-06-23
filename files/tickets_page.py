"""
Tickets page for travel app
"""
from datetime import datetime
from tkinter import ttk, StringVar
from tkcalendar import DateEntry

import TravelApp_BIV222.files.tickets_api
from city_codes import get_city_code


class TicketsPage(ttk.Frame):
    """
    Страница выбора билетов для перелета. Наследуется от класса Frame.
    """

    def __init__(self, parent, controller):
        """
        Инициализация страницы билетов.
        """
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        # Создание и размещение заголовка
        label = ttk.Label(self, text="Enter flight information",
                          font=("Verdana", "22", "bold"))
        label.place(x=80, y=20)

        # Метка для города вылета
        departure_city_label = ttk.Label(self, text='Departure city')
        departure_city_label.place(x=20, y=100)
        # Массив с городами
        cities = ["Chelyabinsk", "Volgograd", "Kazan", "Krasnojarsk", "Moscow", "Omsk", "Sochi",
                  "Nizhniy Novgorod", "Novosibirsk", "Perm", "Saint Petersburg",
                  "Samara", "Ufa", "Yekaterinburg"]
        cities.sort()

        # Поле ввода для города вылета
        self.departure_city_combobox = ttk.Combobox(self, width=12, values=cities)
        self.departure_city_combobox.place(x=380, y=100)

        # Метка и поле ввода для города назначения
        destination_city_label = ttk.Label(self, text='Destination city')
        destination_city_label.place(x=20, y=140)

        self.destination_city_combobox = ttk.Combobox(self, width=12, values=cities)
        self.destination_city_combobox.place(x=380, y=140)

        # Метка и поле ввода для даты вылета
        when_date_label = ttk.Label(self, text='Departure date')
        when_date_label.place(x=20, y=180)

        self.when_date_entry = DateEntry(self, width=12, foreground='white', state="readonly")
        self.when_date_entry.place(x=380, y=180)

        # Метка и поле ввода для даты возврата
        back_date_label = ttk.Label(self, text='Return date')
        back_date_label.place(x=20, y=220)

        self.back_date_entry = DateEntry(self, width=12, foreground='white', state="readonly")
        self.back_date_entry.place(x=380, y=220)

        # Метка и поле ввода для количества пассажиров
        passenger_number_label = ttk.Label(self, text='Number of passengers')
        passenger_number_label.place(x=20, y=260)

        numbers = ["1", "2", "3"]
        self.passenger_number_combobox = ttk.Combobox(self, width=12, values=numbers)
        self.passenger_number_combobox.place(x=380, y=260)

        # Метка и поле ввода для максимальной цены
        max_tickets_price_label = ttk.Label(self, text='Maximum price')
        max_tickets_price_label.place(x=20, y=300)

        self.max_tickets_price_var = StringVar()
        self.max_tickets_price_combobox = ttk.Spinbox(self, width=12,
                                                      textvariable=self.max_tickets_price_var,
                                                      from_=1000, to=100000, increment=500)
        self.max_tickets_price_combobox.place(x=380, y=300)

        # Переход на следующую страницу
        first_button = ttk.Button(self, text='Next', command=lambda: [
            self.on_click_button(),
            self.controller.set_dates(self.get_when_date(),
                                      self.get_back_date()),
            self.controller.frames["HotelsPage"].update_dates(
                self.get_when_date(),
                self.get_back_date()),
            self.controller.frames["HotelsPage"].set_guests(
                self.get_passenger_number()),
            self.controller.show_frame("HotelsPage",
                                       self.destination_city_combobox.get())
        ])
        first_button.place(x=380, y=338)

    def get_departure_city(self):
        """
        Получение кода города вылета.
        """
        departure_city = get_city_code(self.departure_city_combobox.get())
        return departure_city

    def get_destination_city(self):
        """
        Получение кода города назначения.
        """
        destination_city = get_city_code(self.destination_city_combobox.get())
        return destination_city

    def get_when_date(self):
        """
        Получение даты вылета.
        """
        when_date = self.when_date_entry.get()
        when_date_obj = datetime.strptime(when_date, "%m/%d/%y")
        formatted_date_str = when_date_obj.strftime("%Y-%m-%d")
        return formatted_date_str

    def get_back_date(self):
        """
        Получение даты возврата.
        """
        back_date = self.back_date_entry.get()
        back_date_obj = datetime.strptime(back_date, "%m/%d/%y")
        formatted_date_str = back_date_obj.strftime("%Y-%m-%d")
        return formatted_date_str

    def get_passenger_number(self):
        """
        Получение количества пассажиров.
        """
        return self.passenger_number_combobox.get()

    def get_max_tickets_price(self):
        """
        Получение максимальной цены билета.
        """
        return int(self.max_tickets_price_var.get())

    def on_click_button(self):
        """
        Функция, выполняемая при нажатии кнопки.
        """
        origin = self.get_departure_city()
        destination = self.get_destination_city()
        departure_date = self.get_when_date()
        return_date = self.get_back_date()
        adults = self.get_passenger_number()
        tickets = tickets_api.send_data(origin, destination, departure_date, return_date,
                                        int(adults))
        max_tickets_price = self.get_max_tickets_price()
        self.controller.set_max_tickets_price(max_tickets_price)
        self.controller.frames["FullInfoPage"].update_flights_info(tickets)
        self.controller.show_frame("FullInfoPage")
