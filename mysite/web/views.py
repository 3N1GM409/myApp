from django.shortcuts import render, HttpResponse
from web.models import Contact
from django.contrib import messages

def index(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        file = request.POST.get('file')
        message = request.POST.get('message')
        contact = Contact(first_name=first_name, last_name=last_name, email= email, file= file, message=message)
        contact.save()
        messages.success(request, 'Great!! Your details are submitted successfully.')
    return render(request, 'contact.html')
    # return HttpResponse("You landed on our contact page")    