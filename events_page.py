"""
Event page for travel app
"""
from tkinter import StringVar, ttk

import event_api
from city_codes import change_city_code
from TravelApp_BIV222.event_num import change_event_type


class EventsPage(ttk.Frame):
    """
    Класс страницы событий.
    """

    def __init__(self, parent, controller, destination_city=None):
        """
        Инициализация страницы событий.
        :param parent: родительский виджет.
        :param controller: контроллер, управляющий страницами.
        :param destination_city: город назначения.
        """
        super().__init__(parent)
        self.controller = controller
        self.destination_city = StringVar(value=destination_city)
        self.create_widgets()

    def update_destination_city(self, destination_city):
        """
        Обновление города назначения.
        :param destination_city: город назначения.
        """
        self.destination_city.set(destination_city)

    def update_event_date(self, arrival_date):
        """
        Обновление даты события.
        :param arrival_date: дата события.
        """

    def create_widgets(self):
        """
        Создание виджетов на странице.
        """
        # Пометка с вводом деталей мероприятий
        label = ttk.Label(self, text="Enter event information", font=("Verdana", "22", "bold"))
        label.place(x=80, y=20)

        # Метка и поле ввода для города
        event_city_label = ttk.Label(self, text='City')
        event_city_label.place(x=20, y=100)
        cities = ["Chelyabinsk", "Volgograd", "Voronezh", "Kazan", "Krasnojarsk",
                  "Rostov", "Moscow", "Omsk", "Nizhniy Novgorod", "Novosibirsk",
                  "Perm", "Saint Petersburg", "Samara", "Ufa", "Yekaterinburg"]
        cities.sort()
        city_combobox = ttk.Combobox(self, width=12, values=cities,
                                     textvariable=self.destination_city)
        city_combobox.set(self.destination_city)
        city_combobox.place(x=380, y=100)

        # Метки и поля ввода для типа мероприятия
        events = ["Экскурсия", "Активный отдых", "Трансфер", "Мастер-класс",
                  "Билет в музей или на мероприятие"]
        events.sort()
        type_of_event_label = ttk.Label(self, text='Type of event')
        type_of_event_label.place(x=20, y=140)
        self.type_of_event_combobox = ttk.Combobox(self, width=12, values=events)
        self.type_of_event_combobox.place(x=380, y=140)

        # Кнопки для перехода к следующему шагу и возврата назад
        first_button = ttk.Button(self, text='Results', command=lambda:
                                  [self.on_click_button(),
                                   self.controller.show_frame("FullInfoPage")])
        first_button.place(x=380, y=180)
        second_button = ttk.Button(self, text='Back', command=lambda:
        self.controller.show_frame("HotelsPage"))
        second_button.place(x=80, y=180)

    def on_click_button(self):
        """
        Обработка нажатия на кнопку.
        Вызывает поиск событий и обновление информации на странице полной информации.
        """
        destination = change_city_code(self.destination_city.get())
        event_type = change_event_type(self.type_of_event_combobox.get())
        event_api.search_events(destination, event_type)
        events = event_api.search_events(destination, event_type)
        self.controller.frames["FullInfoPage"].update_events_info(events)
        self.controller.show_frame("FullInfoPage")
