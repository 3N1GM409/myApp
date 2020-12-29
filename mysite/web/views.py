from django.shortcuts import render, HttpResponse
from datetime import datetime
from web.models import contact
def index(request):
    return render(request, 'base.html')

def service(request):
    return HttpResponse("You landed on our service page")

def about(request):
    return HttpResponse("You landed on our about page")

def contact(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastName')
        email = request.POST.get('email')
        message = request.POST.get('message')
        docs = request.POST.get('docs')
        con = contact(firstname = firstname, lastname = lastname, email = email, message = message, docs = docs, date = datetime.today())
        con.save()

    return render(request, "contact.html")
    # return HttpResponse("You landed on our contact page")    