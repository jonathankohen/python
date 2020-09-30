from django.shortcuts import render, redirect


def index(req):
    if "counter" in req.session:
        req.session["counter"] += 1
    else:
        req.session["counter"] = 1
    return render(req, 'index.html')


def destroy_session(req):
    if "counter" in req.session:
        req.session["counter"] = 0
    return redirect('/')
