from django.shortcuts import render, redirect
from .models import Dojo, Ninja


def index(req):
    context = {
        "all_dojos": Dojo.objects.all()
    }
    return render(req, 'index.html', context)


def new_dojo(req):
    print(req.POST)

    form_dojo_name = req.POST.get('dojo_name', 'Main')
    form_dojo_city = req.POST.get('dojo_city', 'NYC')
    form_dojo_state = req.POST.get('dojo_state', 'MA')

    Dojo.objects.create(name=form_dojo_name,
                        city=form_dojo_city, state=form_dojo_state)

    return redirect('/')


def new_ninja(req):
    print(req.POST)

    form_ninja_fn = req.POST.get('first_name', 'Jon')
    form_ninja_ln = req.POST.get('last_name', 'Kohen')
    form_ninja_dojo = req.POST.get('ninja_dojo', 4)

    Ninja.objects.create(first_name=form_ninja_fn,
                         last_name=form_ninja_ln, dojo=Dojo.objects.get(id=form_ninja_dojo))

    return redirect('/')
