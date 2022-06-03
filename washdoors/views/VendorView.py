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
    return render(request, 'vendor//register.html')