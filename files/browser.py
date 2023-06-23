"""
Модуль для открытия ссылок в браузере
"""
import webbrowser


def browse_ticket(ticket_link):
    """
    Функция для открытия браузера с результатами поиска билетов.
    """
    webbrowser.open_new('https://www.aviasales.ru' + str(ticket_link))


def browse_hotel(hotel_link):
    """
    Функция для открытия браузера с результатами поиска отелей.
    """
    webbrowser.open_new(hotel_link)


def browse_event(event_link):
    """
    Функция для открытия браузера с результатами поиска мероприятий.
    """
    webbrowser.open_new(event_link)
