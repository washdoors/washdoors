from django.shortcuts import render
from .Backend import DatabaseConnection
from .Backend import EmailSender
from email.message import EmailMessage

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
    conn = DatabaseConnection()
    cursor = conn.cursor(buffered=True)
    cursor.execute(f"INSERT INTO customer VALUES('{firstname}','{lastname}','{custid}','{password}','{city}','{area}','{pin}','{mobile}');")
    conn.close()
    return render(request, 'trail.html')

def home(request):
    return render(request,'customer//home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        senderemail = request.POST.get('email')
        address1 = request.POST.get('address1')
        # print(name,senderemail,address1)
        email = EmailSender()
        msg = EmailMessage()
        msg['subject'] = 'Query from customer'
        msg.set_content(f'{name} from {address1} has raised a query.')
        email.sendEmail(senderemail,str(msg))
    return render(request,'customer//contact.html')