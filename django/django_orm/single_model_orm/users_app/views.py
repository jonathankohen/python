from django.shortcuts import render, redirect
from .models import User


def index(req):
    return render(req, 'index.html')


def all_users(req):
    context = {
        "all_the_users": User.objects.all(),
    }
    return render(req, 'all_users.html', context)


def process(req):
    print(req.POST)

    first_name = req.POST.get('first_name', 'Yoni')
    last_name = req.POST.get('last_name', 'Balboni')
    email = req.POST.get('email', 'test@test.com')
    age = req.POST.get('age', 0)

    User.objects.create(first_name=first_name, last_name=last_name,
                        email=email, age=age)

    return redirect('/all_users')
