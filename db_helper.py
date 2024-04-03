# db_helper.py
import mysql.connector


def insert_booking(name, phone_number, address, date):
    try:
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ti-21038",
            database="bookingsession"
        )
        cursor = cnx.cursor()

        add_booking = ("INSERT INTO client_detail (name, phone_number, address, date) "
                       "VALUES (%s, %s, %s, %s)")
        data_booking = (name, phone_number, address, date)
        cursor.execute(add_booking, data_booking)

        cnx.commit()

        cursor.close()
        cnx.close()

        return True  # Insertion successful
    except mysql.connector.Error as err:
        print("Error:", err)
        return False  # Insertion failed
