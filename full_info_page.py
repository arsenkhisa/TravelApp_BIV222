"""
Page with full info for travel app
"""
from tkinter import END, INSERT, WORD, Text
from tkinter import ttk

from TravelApp_BIV222.browser import browse_ticket, browse_hotel, browse_event
from database_connector import tickets_update, hotels_update, events_update


class FullInfoPage(ttk.Frame):
    """
    Класс страницы полной информации.
    """

    def __init__(self, parent, controller):
        """
        Инициализация страницы полной информации.
        :param parent: родительский виджет.
        :param controller: контроллер, управляющий страницами.
        """
        super().__init__(parent)

        self.controller = controller
        self.marker = "event"
        self.link = ""
        # Создание и размещение виджетов на странице
        label = ttk.Label(self, text="Information", font=("Verdana", "22", "bold"))
        label.grid(row=0, column=1, ipady=6, pady=5)
        # Создание и размещение окна для вывода результатов
        self.info_text = Text(self, wrap=WORD, height=11, width=45)
        self.info_text.grid(row=1, column=1, ipady=6, pady=5)
        # Создание и размещение кнопки для открытия в браузере
        open_in_web = ttk.Button(self, text="Open in browser", command=self.open_in_browser)
        open_in_web.grid(row=2, column=1)
        # Создание и размещение кнопки для просмотра предыдущего билета
        prev_flight_button = ttk.Button(self, text="Previous ticket",
                                        command=self.show_previous_flight)
        prev_flight_button.grid(row=3, column=0)
        # Создание и размещение кнопки для просмотра следующего билета
        next_flight_button = ttk.Button(self, text="Next ticket", command=self.show_next_flight)
        next_flight_button.grid(row=3, column=2)
        # Создание и размещение кнопки для просмотра предыдущего отеля
        prev_hotel_button = ttk.Button(self, text="Previous hotel",
                                       command=self.show_previous_hotel)
        prev_hotel_button.grid(row=4, column=0)
        # Создание и размещение кнопки для просмотра следующего отеля
        next_hotel_button = ttk.Button(self, text="Next hotel", command=self.show_next_hotel)
        next_hotel_button.grid(row=4, column=2)
        # Создание и размещение кнопки для просмотра предыдущего мероприятия
        prev_event_button = ttk.Button(self, text="Previous event",
                                       command=self.show_previous_event)
        prev_event_button.grid(row=5, column=0)
        # Создание и размещение кнопки для просмотра следующего мероприятия
        next_event_button = ttk.Button(self, text="Next event", command=self.show_next_event)
        next_event_button.grid(row=5, column=2)
        # Создание и размещение кнопки для переключения на предыдущую страницу
        back_button = ttk.Button(self, text="Back", command=lambda:
                                 controller.show_frame("EventsPage"))
        back_button.grid(row=6, column=0)
        # Создание и размещение кнопки для сохранения варианта
        save_button = ttk.Button(self, text="Save", command=self.on_click_button)
        save_button.grid(row=6, column=2)

    def open_in_browser(self):
        """
        Функция для открытия ссылки в интернете
        """
        if self.marker == "ticket" and self.flights:
            flight = self.flights[self.flight_index]
            browse_ticket(flight['link'])
        elif self.marker == "hotel" and self.hotels:
            hotel = self.hotels[self.hotels_index]
            destination = hotel['location']
            departure_date = hotel['checkIn']
            return_date = hotel['checkOut']
            adults = hotel['adults']
            hotel_id = hotel['id']
            hotel_link = "https://search.hotellook.com/hotels?=1" + "&adults=" \
                + str(adults) + "&checkIn=" + \
                         str(departure_date) + "&checkOut=" + str(return_date) + "&currency=rub" \
                         + "&destination=" + str(destination) + "&language=ru" + \
                             "&hotelId=" + str(hotel_id)
            browse_hotel(hotel_link)
        else:
            event = self.events[self.events_index]
            browse_event(event['link'])


    def update_flights_info(self, flights):
        """
        Обновление информации о полетах.
        :param flights: список полетов.
        """
        self.flights = [flight for flight in flights if flight['price']
                        <= float(self.controller.max_tickets_price)]
        self.flight_index = 0
        self.show_flight_info()

    def update_hotels_info(self, hotels):
        """
        Обновление информации об отелях.
        :param hotels: список отелей.
        """
        self.hotels = [hotel for hotel in hotels if hotel['avgPrice']
                       <= int(self.controller.max_hotels_price)]
        self.hotels_index = 0
        self.show_hotels_info()

    def update_events_info(self, events):
        """
        Обновление информации о событиях.
        :param events: список событий.
        """
        self.events = events
        self.events_index = 0
        self.show_events_info()

    def show_flight_info(self):
        """
        Отображение информации о билетах.
        """
        self.info_text.delete(1.0, END)
        if self.flights:
            flight = self.flights[self.flight_index]
            info = f"""
Flight tickets:
---------------
Airline: {flight['airline']}
Departure: {flight['departure']}
From: {flight['from']}
To: {flight['to']}
Price: {flight['price']}
"""
            self.info_text.insert(INSERT, info)

    def show_hotels_info(self):
        """
        Отображение информации об отелях.
        """
        self.info_text.delete(1.0, END)
        if self.flights:
            hotel = self.hotels[self.hotels_index]
            info = f"""
Hotel rooms:
---------------
Hotel name: {hotel['hotelName']}
Stars: {hotel['stars']}
Check In: {hotel['checkIn']}
Check Out: {hotel['checkOut']}
Average price: {hotel['avgPrice']}
"""
            self.info_text.insert(INSERT, info)

    def show_events_info(self):
        """
        Отображение информации о мероприятиях.
        """
        self.info_text.delete(1.0, END)
        if self.events:
            event = self.events[self.events_index]
            info = f"""
Events:
--------------
Event name: {event['eventName']}
Description: {event['description']}
Price: {event['price']}
Movement type: {event['movementType']}
Duration: {event['duration']}
"""
            self.info_text.insert(INSERT, info)

    def show_previous_flight(self):
        """
        Отображение прошлой информации о билетах.
        """
        self.marker = "ticket"
        if self.flight_index > 0:
            self.flight_index -= 1
            self.show_flight_info()

    def show_next_flight(self):
        """
        Отображение новой информации о билетах.
        """
        self.marker = "ticket"
        if self.flight_index < len(self.flights) - 1:
            self.flight_index += 1
            self.show_flight_info()

    def show_previous_hotel(self):
        """
        Отображение прошлой информации об отелях.
        """
        self.marker = "hotel"
        if self.hotels_index > 0:
            self.hotels_index -= 1
            self.show_hotels_info()

    def show_next_hotel(self):
        """
        Отображение новой информации об отелях.
        """
        self.marker = "hotel"
        if self.hotels_index < len(self.hotels) - 1:
            self.hotels_index += 1
            self.show_hotels_info()

    def show_previous_event(self):
        """
        Отображение прошлой информации о мероприятиях.
        """
        self.marker = "event"
        if self.events_index > 0:
            self.events_index -= 1
            self.show_events_info()

    def show_next_event(self):
        """
        Отображение новой информации о мероприятиях.
        """
        self.marker = "event"
        if self.events_index < len(self.events) - 1:
            self.events_index += 1
            self.show_events_info()

    def on_click_button(self):
        """
        Функция, срабатывающая при нажатии на кнопку
        """
        # self.save_info()
        if self.marker == 'ticket' and self.flights:
            flight = self.flights[self.flight_index]
            tickets_update(flight['from'], flight['to'], flight['airline'],
                           str(flight['number']), flight['departure'],
                           flight['return'], str(flight['price']), flight['link'])
        elif self.marker == "hotel" and self.hotels:
            hotel = self.hotels[self.hotels_index]
            hotel_link = "https://search.hotellook.com/hotels?=1" + "&adults=" + \
                str(hotel['adults']) + "&checkIn=" + str(hotel['checkIn']) + \
                    "&checkOut=" + str(hotel['checkOut']) + "&currency=rub" + \
                        "&destination=" + str(hotel['location']) + "&language=ru" + \
                            "&hotelId=" + str(hotel['id'])
            hotels_update(hotel['hotelName'], hotel['stars'], hotel['checkIn'],
                          hotel['checkOut'], hotel['avgPrice'], hotel_link)
        else:
            event = self.events[self.events_index]
            events_update(event['city'], event['eventName'], event['description'],
                          event['eventType'], event['duration'], event['price'], event['link'])
