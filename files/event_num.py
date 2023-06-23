"""
Функция для выбора типа мероприятия
"""
def change_event_type(event_type):
    """
    Функция для преобразования типа события в соответствующий ему код.

    :param event_type: Строка, описывающая тип события.
    :return: Целочисленный код типа события.
    """
    if event_type == "Экскурсия":
        return 1
    if event_type == "Активный отдых":
        return 2
    if event_type == "Трансфер":
        return 5
    if event_type == "Мастер-класс":
        return 7
    if event_type == "Билет в музей или на мероприятие":
        return 8
    return None
