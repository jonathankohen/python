from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show


def root(req):
    return redirect('/shows')


def index(req):
    return render(req, 'index.html')


def create(req):
    errors = Show.objects.basic_validator(req.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(req, value)
        return redirect('/shows/new')
    else:
        new_show = Show.objects.create(title=req.POST.get('title', 'Title'), network=req.POST.get(
            'network', 'network'), release_date=req.POST.get('release_date', 'Release Date'), desc=req.POST.get('desc', 'Description'))

    return redirect(f'/shows/{new_show.id}')


def single_show(req, idShow):
    context = {
        "show": Show.objects.get(id=idShow)
    }
    return render(req, 'single_show.html', context)


def shows(req):
    context = {
        "all_shows": Show.objects.all()
    }
    return render(req, 'shows.html', context)


def edit(req, idShow):
    context = {
        "show": Show.objects.get(id=idShow)
    }
    return render(req, 'edit.html', context)


def delete(req, idShow):
    show = Show.objects.get(id=idShow)
    show.delete()
    return redirect("/shows")


def update(req, idShow):
    errors = Show.objects.basic_validator(req.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(req, value)
        return redirect(f'/shows/{idShow}/edit')
    else:
        show = Show.objects.get(id=idShow)
        show.title = req.POST.get("title", "Title")
        show.network = req.POST.get("network", "Network")
        show.release_date = req.POST.get("release_date", "Release Date")
        show.desc = req.POST.get("desc", "Description")
        show.save()
    return redirect(f'/shows/{idShow}')
