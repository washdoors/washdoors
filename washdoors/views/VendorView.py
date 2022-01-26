from django.shortcuts import render
from .Backend import DatabaseConnection


def custLogin(request):
    custid = 'usr'
    psk = 'psk'
    conn = DatabaseConnection()
    cursor = conn.cursor(buffered=True)
    cursor.execute(f"SELECT * customer FROM WHERE CustId = '{custid}' AND Password = '{psk}';")
    conn.close()
    return render(request,'trail.html')

def custRegister(request):
    firstname = 'firstname'
    lastname = 'lastname'
    custid = 'custid'
    password = 'psk'
    city = 'city'
    area = 'area'
    pin = 1234
    mobile = 72525662
    start_time = "hh:mm:ss"
    stop_time = "hh:mm:ss"
    conn = DatabaseConnection()
    cursor = conn.cursor(buffered=True)
    cursor.execute(f"INSERT INTO rider VALUES('{firstname}','{lastname}','{custid}','{password}','{city}','{area}','{pin}','{mobile}','{start_time}','{stop_time}');")
    conn.close()
    return render(request, 'trail.html')