"""
Функция для преобразования названия города в его IATA
"""
import json
import requests


def get_city_code(city_name):
    """
    Функция для получения кода города по его русскому названию.

    :param city_name: Русское название города.
    :return: Код города.
    """
    url = "https://api.travelpayouts.com/data/en/cities.json"
    response = requests.get(url)
    cities = json.loads(response.text)
    for city in cities:
        if city["name"] == city_name:
            return city["code"]


def change_city_code(city_name):
    """
    Функция для получения английского названия города по его русскому названию.

    :param city_name: Русское название города.
    :return: Английское название города.
    """
    url = "https://api.travelpayouts.com/data/en/cities.json"
    response = requests.get(url)
    cities = json.loads(response.text)

    for city in cities:
        if city["name"] == city_name:
            return city_name
