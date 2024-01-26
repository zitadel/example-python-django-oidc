from django.shortcuts import render


def HomeView(request):
    return render(request, "mysite/home.html")


def UserView(request):
    return render(request, "mysite/user.html")
