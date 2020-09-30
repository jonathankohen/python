from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request, 'index.html')


def results(request):
    print(request.POST)

    name = request.POST.get('name', 'Guest')
    dojo_location = request.POST.get('dojo_location', 'Dojo')
    fav_lan = request.POST.get('fav_lan', 'Python')
    comments = request.POST.get('comments', 'Hello')

    context = {
        'name': name,
        'dojo_location': dojo_location,
        'fav_lan': fav_lan,
        'comments': comments
    }

    return render(request, 'results.html', context)
