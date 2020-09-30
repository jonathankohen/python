from django.shortcuts import render, redirect
from .models import User, Item
from django.contrib import messages
import bcrypt
from django.db.models import Q


def index(req):
    return render(req, 'index.html')


def register(req):
    print(req.POST)
    errors = User.objects.regValidator(req.POST)
    if len(errors) > 0:
        for value in errors.values():
            messages.error(req, value)
        return redirect("/")
    else:
        pw_hash = bcrypt.hashpw(
            req.POST['pw'].encode(), bcrypt.gensalt()).decode()
        newUser = User.objects.create(
            name=req.POST['name'], username=req.POST['username'], password=pw_hash)
        req.session['logged_in_id'] = newUser.id
        return redirect("/dashboard")


def login(req):
    print(req.POST)
    errors = User.objects.loginValidator(req.POST)
    if len(errors) > 0:
        for value in errors.values():
            messages.error(req, value)
        return redirect("/")
    else:
        print(errors)
        username_filter = User.objects.filter(
            username=req.POST['username'])
        req.session['logged_in_id'] = username_filter[0].id
        return redirect("/dashboard")


def logout(req):
    req.session.clear()
    return redirect("/")


def dashboard(req):
    if 'logged_in_id' not in req.session:
        messages.error(req, "You must log in to see the dashboard.")
        return redirect("/")
    context = {
        'logged_in_user': User.objects.get(id=req.session['logged_in_id']),
        'favorites': Item.objects.filter(Q(favorites=User.objects.get(id=req.session['logged_in_id'])) | Q(uploader=User.objects.get(id=req.session['logged_in_id']))),
        'not_favorites': Item.objects.exclude(Q(favorites=User.objects.get(id=req.session['logged_in_id'])) | Q(uploader=User.objects.get(id=req.session['logged_in_id'])))
    }
    return render(req, "dashboard.html", context)


def add_item(req):
    return render(req, "add_item.html")


def create_item(req):
    print(req.POST)
    errors = Item.objects.itemValidator(req.POST)
    if len(errors) > 0:
        for value in errors.values():
            messages.error(req, value)
        return redirect("/wish_items/create")

    new_item = Item.objects.create(name=req.POST['item_name'], uploader=User.objects.get(
        id=req.session['logged_in_id']))
    return redirect("/dashboard")


def show_item(req, item_id):
    context = {
        'item': Item.objects.get(id=item_id)
    }
    return render(req, "show_item.html", context)


def fav_item(req, item_id):
    print(req.POST)
    user = User.objects.get(id=req.session['logged_in_id'])
    item = Item.objects.get(id=item_id)
    item.favorites.add(user)
    return redirect("/dashboard")


def unfav_item(req, item_id):
    print(req.POST)
    user = User.objects.get(id=req.session['logged_in_id'])
    item = Item.objects.get(id=item_id)
    item.favorites.remove(user)
    return redirect("/dashboard")


def delete_item(req, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()
    return redirect("/dashboard")
