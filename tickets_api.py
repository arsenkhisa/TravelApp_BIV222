"""
Code working with api for tickets page
"""
from datetime import datetime
import json
import requests


def send_data(origin, destination, departure_date, return_date, adults):
    """
    Отправка данных и получение информации о рейсах с сайта Travelpayouts.

    Args:
        origin (str): Код города вылета.
        destination (str): Код города назначения.
        departure_date (str): Дата вылета в формате 'YYYY-MM-DD'.
        return_date (str): Дата возвращения в формате 'YYYY-MM-DD'.
        adults (int): Количество взрослых пассажиров.

    Returns:
        list: Список словарей с информацией о рейсах.
    """
    # URL-адрес для отправки запроса
    url = "https://api.travelpayouts.com/aviasales/v3/prices_for_dates"

    # Параметры для запроса
    params = {
        "origin": origin,
        "destination": destination,
        "departure_at": departure_date,
        "return_at": return_date,
        "currency": "rub",
        "token": "9570cd803e10001a719af1e9aba6835a",
        "adults": adults
    }

    # Отправка GET-запроса и получение ответа
    response = requests.get(url, params=params)

    # Преобразование ответа из формата JSON в объект Python
    data = json.loads(response.text)

    flights = []  # пустой список для хранения информации о рейсах
    # Проход по всем рейсам и добавление их в список
    for i in range(len(data['data'])):
        departure_at = datetime.fromisoformat(data['data'][i]['departure_at'])
        return_at = datetime.fromisoformat(return_date)
        flights.append({
            'airline': data['data'][i]['airline'],
            'departure': departure_at.strftime("%Y-%m-%d %H:%M"),
            'return': return_at.strftime("%Y-%m-%d %H:%M"),
            'from': data['data'][i]['origin'],
            'to': data['data'][i]['destination'],
            'price': data['data'][i]['price'],
            'link': data['data'][i]['link'],
            'number': data['data'][i]['flight_number']
        })
    return flights  # возврат списка с информацией о рейсах
