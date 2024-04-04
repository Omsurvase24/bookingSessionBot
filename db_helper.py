# db_helper.py
import mysql.connector


def insert_client_detail(name, phone_number, address):
    try:
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ti-21038",
            database="bookingsession"
        )
        cursor = cnx.cursor()

        add_client_detail = ("INSERT INTO bookingsession.client_detail (name, phone_number, address) "
                             "VALUES (%s, %s, %s)")
        data_client_detail = (name, phone_number, address)
        cursor.execute(add_client_detail, data_client_detail)

        cnx.commit()

        cursor.close()
        cnx.close()

        return True  # Insertion successful
    except mysql.connector.Error as err:
        print("Error:", err)
        return False  # Insertion failed


def insert_date(date):
    try:
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ti-21038",
            database="bookingsession"
        )
        cursor = cnx.cursor()

        add_date = ("INSERT INTO date (date) "
                    "VALUES (%s)")
        data_date = (date,)
        cursor.execute(add_date, data_date)

        cnx.commit()

        cursor.close()
        cnx.close()

        return True  # Insertion successful
    except mysql.connector.Error as err:
        print("Error:", err)
        return False  # Insertion failed
