from django.shortcuts import render
from .Backend import DatabaseConnection

def trail(request):
    conn = DatabaseConnection()
    name = 'Road Issue'
    isseid = 2
    cursor = conn.cursor(buffered=True)
    cursor.execute(f"select * from Issues where Name = '{name}';")
    print(cursor.fetchone())
    conn.close()
    return render(request,"trail.html")

