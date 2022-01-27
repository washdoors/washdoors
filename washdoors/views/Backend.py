import mysql.connector as mysql
import smtplib
from email.message import EmailMessage

#class for data connectivity with MySql
class DatabaseConnection(object):
    def __new__(cls, *args, **kwargs):
        conn = mysql.connect(
            host='sql6.freemysqlhosting.net',
            database='sql6468008',
            user='sql6468008',
            password='eqHRn7SbqA'
        )
        print("connected")
        print(type(conn))
        return conn

    def __del__(self):
        self.conn.close()

#functions for convertiting functions
class ConvertFunction(object):
    pass

#class for email
class EmailSender(object):
    def __init__(self):
        self.server = smtplib.SMTP_SSL("smtp.gmail.com")
        self.server.login("send@address.com", "sender_psk")

    def sendEmail(self,sender,receiver,content):
        self.server.sendmail(sender,receiver,content)

    def setContent(self):
        msg = EmailMessage()

#class for vendor
class Vendor(object):
    def __init__(self,id):
        self.id = id

    def getServices(self):
        conn = DatabaseConnection()
        cursor = conn.cursor(buffered=True)
        cursor.execute(f"SELECT * service FROM WHERE VendorId = '{self.id}';")
        services = cursor.fetchall()
        conn.close()
        return services

    def getProfile(self):
        conn = DatabaseConnection()
        cursor = conn.cursor(buffered=True)
        cursor.execute(f"SELECT * FROM vendor WHERE VendorId = '{self.id}';")
        profile_details = cursor.fetchone()
        conn.close()
        return profile_details

    def getOrders(self):
        conn = DatabaseConnection()
        cursor = conn.cursor(buffered=True)
        cursor.execute(f"SELECT * FROM orders WHERE VendorId = '{self.id}';")
        orders = cursor.fetchall()
        conn.close()
        return orders

#customer class
class Customer(object):
    def __init__(self,id):
        self.id = id

    def __init__(self):
        pass

    def getProfile(self):
        conn = DatabaseConnection()
        cursor = conn.cursor(buffered=True)
        cursor.execute(f"SELECT * FROM customer WHERE CustId = '{self.id}';")
        profile_details = cursor.fetchone()
        conn.close()
        return profile_details

    def getOrders(self):
        conn = DatabaseConnection()
        cursor = conn.cursor(buffered=True)
        cursor.execute(f"SELECT * FROM orders WHERE CustId = '{self.id}';")
        orders = cursor.fetchall()
        conn.close()
        return orders

#Rider class
class Rider(object):
    def __init__(self, id):
        self.id = id

    def __int__(self):
        pass

    def getProfile(self):
        conn = DatabaseConnection()
        cursor = conn.cursor(buffered=True)
        cursor.execute(f"SELECT * FROM rider WHERE RiderId = '{self.id}';")
        profile_details = cursor.fetchone()
        conn.close()
        return profile_details

    def getOrders(self):
        conn = DatabaseConnection()
        cursor = conn.cursor(buffered=True)
        cursor.execute(f"SELECT * FROM orders WHERE RiderId = '{self.id}';")
        orders = cursor.fetchall()
        conn.close()
        return orders



