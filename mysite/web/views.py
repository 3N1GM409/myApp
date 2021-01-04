from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'base.html')

def service(request):
    return HttpResponse("You landed on our service page")

def about(request):
    return HttpResponse("You landed on our about page")

def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("You landed on our contact page")    