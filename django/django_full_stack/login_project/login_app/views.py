from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Post
import bcrypt


def index(req):
    return render(req, 'index.html')


def register(req):
    errors = User.objects.reg_validator(req.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(req, value)
        return redirect("/")
    else:
        password = req.POST.get('password', 'password')
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(first_name=req.POST.get(
            'first_name', 'first_name'), last_name=req.POST.get(
            'last_name', 'last_name'), email=req.POST.get(
            'email', 'email'), password=pw_hash)
        req.session['logged_in_id'] = new_user.id
        return redirect("/success")


def login(req):
    errors = User.objects.login_validator(req.POST)
    user = User.objects.filter(
        email=req.POST.get('email', 'email'))
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(req, value)
        return redirect("/")
    else:
        req.session['logged_in_id'] = user[0].id
        return redirect('/success')


def success(req):
    if 'logged_in_id' not in req.session:
        messages.error(req, "You must log in to see this page.")
        return redirect("/")
    context = {
        "logged_in_user": User.objects.get(id=req.session['logged_in_id']),
        "all_posts": Post.objects.all()
    }
    return render(req, 'success.html', context)


def logout(req):
    req.session.clear()
    return redirect("/")
