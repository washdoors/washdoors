from http import client
import smtplib
from pymongo import MongoClient
import urllib.parse
#class for data connectivity with MySql
class DatabaseConnection(object):
    client = None    
    def __new__(cls, *args, **kwargs):
        username = urllib.parse.quote_plus('rushi')
        password = urllib.parse.quote_plus('Rushi_1192')
        client = MongoClient('mongodb://%s:%s@127.0.0.1'%(username, password))
        db = client['washdoors']
        return db
    def __del__(self):
        self.client.close()
        print('client is closed')

#functions for convertiting functions
class ConvertFunction(object):
    pass

#class for email
class EmailSender(object):
    def __init__(self):
        self.server = smtplib.SMTP_SSL("smtp.gmail.com")
        self.server.login("rushikeshborakhede@student.sfit.ac.in", "Rushi_1192#")

    def sendEmail(self,receiver,content):
        self.server.sendmail('rushikeshborakhede@student.sfit.ac.in',receiver,content)

    # def setContent(self):
    #     msg = EmailMessage()

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

    def chechAvailibilty(self):
        # send push notification
        availiibity = 'fet from vendor'
        if (availiibity):
            return True
        else:
            return False


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

    def chechAvailibilty(self):
        #send push notification
        availiibity = 'fet from vendor'
        if(availiibity):
            return True
        else:
            return False


class Order(object):
    def createOrder(self,custid):
        #use the api of payment
        print(custid)