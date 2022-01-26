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

