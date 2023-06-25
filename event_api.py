"""
Работа с api для мероприятий
"""
import json
import requests


def search_events(destination, event_type):
    """
    Функция для поиска событий по заданному направлению и типу события.

    :param destination: Строка, описывающая город назначения.
    :param event_type: Целое число, описывающее тип события.
    :return: Список словарей с информацией о найденных событиях.
    """
    # URL-адрес для отправки запроса
    url = "https://experience.tripster.ru/api/partners/%3Cpartner_name%3E/experiences/?"

    # Параметры для запроса
    params = {
        "city__name_en": destination,
        "exp_format": event_type,
    }

    # Отправка GET-запроса и получение ответа
    response = requests.get(url, params=params)

    # Преобразование ответа из формата JSON в объект Python
    data = json.loads(response.text)
    events = [] # пустой список для хранения информации о мероприятиях

    # Проход по всем мероприятиям и добавление их в список
    for i in range(len(data['results'])):
        events.append({
            'city': destination,
            'eventType': event_type,
            'eventName': data['results'][i]['title'],
            'description': data['results'][i]['tagline'],
            'price': data['results'][i]['price']['value_string'],
            'movementType': 'By ' + data['results'][i]['movement_type'],
            'duration': str(data['results'][i]['duration']) + ' hours',
            'link': data['results'][i]['url']
        })
    return events # возврат списка с информацией о мероприятиях
