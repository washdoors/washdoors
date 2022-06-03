import email
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .Backend import DatabaseConnection
from .Backend import EmailSender
from email.message import EmailMessage

def custLogin(request):
    entry = {}
    if request.method == 'POST':
        entry['_id'] = request.POST.get('email')
        entry['fname'] = request.POST.get('fname')
        entry['lname'] = request.POST.get('lname')
        entry['mobile'] = request.POST.get('mobile')
        entry['password'] = request.POST.get('password')
        entry['role'] = 'customer'
        print(entry)
        db = DatabaseConnection()
        db['person'].insert_one(entry)
        db.client.close()  #before this line code is working properly
        return HttpResponse("""
        <script>
        alert('You have been succefully registered to system');
        window.location.href = '/cust/login/';
        </script>
        """)
    return render(request,'customer//login.html')
def custRegister(request):
    return render(request, 'customer//register.html')

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

def dashboard(request):
    input = {}
    output = {}
    if request.method == 'POST':
        input['_id'] = request.POST.get('username')
        input['password'] = request.POST.get('password')
        db = DatabaseConnection()
        output['profile'] = db['person'].find_one(input)
        if output['profile']:
            # output['history'] = db['order'].find(input['_id'])
            return render(request,'customer//dashboard.html')
        else:
            return HttpResponse("""
            <script>
            alert('Entered username or password is wrong. Please try again');
            window.location.href = '/cust/login/';
            </script>
            """)