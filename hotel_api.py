"""
Code workint witk hotels api
"""
import json
import requests

def search_hotels(destination, departure_date, return_date, adults):
    """
    Поиск отелей по заданным параметрам.

    Аргументы:
        destination (str): город назначения.
        departure_date (str): дата отъезда.
        return_date (str): дата возвращения.
        adults (int): количество взрослых.

    Вывод:
        list: список отелей.
    """
    # URL-адрес для отправки запроса
    url = "https://engine.hotellook.com/api/v2/cache.json?"

    # Параметры для запроса
    params = {
        "location": destination,
        "currency": "rub",
        "checkIn": departure_date,
        "checkOut": return_date,
        "adults": adults,
        "limit": 10000
    }

    # Отправка GET-запроса и получение ответа
    response = requests.get(url, params=params)

    # Преобразование ответа из формата JSON в объект Python
    data = json.loads(response.text)

    hotels = [] # пустой список для хранения информации об отелях

    # Проход по всем отелям и добавление их в список
    for i in range(len(data)):
        hotels.append({
            'location': data[i]['location']['name'],
            'hotelName': data[i]['hotelName'],
            'stars': data[i]['stars'],
            'avgPrice': data[i]['priceAvg'],
            'checkIn': departure_date,
            'checkOut': return_date,
            'id': data[i]['hotelId'],
            'adults': adults
        })
    return hotels # возврат списка с информацией об отелях
