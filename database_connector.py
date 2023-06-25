"""
Функции для сохранения данных в базу данных
"""
import mysql.connector


def tickets_update(origin, destination, airline, flight_number,
                   departure_date, return_date, price, link):
    """
    Обновление билетов в базе данных.
    """
    # Установка соединения с базой данных MySQL
    mydb = mysql.connector.connect(
        host="localhost",
        user="TravelUser",
        password="adv3nTur$",
        database="app"
    )

    mycursor = mydb.cursor()
    sql = "INSERT INTO tickets (Origin, Destination, Airline, FlightNumber, " \
          "DepartureDate, ReturnDate, Price, Url)" \
          " VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (origin, destination, airline, flight_number, departure_date, return_date, price, link)
    mycursor.execute(sql, val)
    mydb.commit() # Сохранение данных в БД
    mydb.close() # Закрытие соединения с БД


def hotels_update(hotel_name, stars, check_in, check_out, price, url):
    """
    Обновление отелей в базе данных.
    """
    # Установка соединения с базой данных MySQL
    mydb = mysql.connector.connect(
        host="localhost",
        user="TravelUser",
        password="adv3nTur$",
        database="app"
    )

    mycursor = mydb.cursor()
    sql = "INSERT INTO hotels (HotelName, Stars, CheckIn, CheckOut, " \
          "Price, Url)" \
          " VALUES (%s, %s, %s, %s, %s, %s)"
    val = (hotel_name, stars, check_in, check_out, price, url)
    mycursor.execute(sql, val)
    mydb.commit() # Сохранение данных в БД
    mydb.close() # Закрытие соединения с БД


def events_update(city, title, tagline, event_type, duration, price, url):
    """
    Обновление мероприятий в базе данных.
    """
    # Установка соединения с базой данных MySQL
    mydb = mysql.connector.connect(
        host="localhost",
        user="TravelUser",
        password="adv3nTur$",
        database="app"
    )

    mycursor = mydb.cursor()
    sql = "INSERT INTO events (City, Title, Tagline, Event_type, " \
          "Duration, Price, Url)" \
          " VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (city, title, tagline, event_type, duration, price, url)
    mycursor.execute(sql, val)
    mydb.commit() # Сохранение данных в БД
    mydb.close() # Закрытие соединения с БД


def show_info(table_name):
    """
    Функиця для отображения информации из БД
    """
    # Установка соединения с базой данных MySQL
    mydb = mysql.connector.connect(
        host="localhost",
        user="TravelUser",
        password="adv3nTur$",
        database="app"
    )

    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * FROM {table_name}")
    rows = mycursor.fetchall()

    mydb.commit() # Сохранение данных в БД
    mydb.close() # Закрытие соединения с БД

    return rows


def clear():
    """
    Удаление билетов из базы данных.
    """
    # Установка соединения с базой данных MySQL
    mydb = mysql.connector.connect(
        host="localhost",
        user="TravelUser",
        password="adv3nTur$",
        database="app"
    )

    mycursor = mydb.cursor()
    sql1 = "DELETE FROM tickets;"
    sql2 = "DELETE FROM hotels;"
    sql3 = "DELETE FROM events;"
    mycursor.execute(sql1)
    mycursor.execute(sql2)
    mycursor.execute(sql3)
    mydb.commit() # Сохранение данных в БД
    mydb.close() # Закрытие соединения с БД
