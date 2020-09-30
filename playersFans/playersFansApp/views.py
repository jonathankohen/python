from django.shortcuts import render, redirect
from .models import Player, Fan

# Create your views here.
def index(request):
    print("wazaaaaaa")
    allPlayers = Player.objects.all()
    print(allPlayers)
    # to pass info to HTML, need a dictionary
    context = {
        'allThePlayers': allPlayers
    }

    return render(request, "index.html", context)


def createPlayer(request):
    print("in post request function")
    #REQ.POST REPRESENTS INFORMATION SUBMITTED FROM THE FORM ON A POST REQUEST
    print(request.POST) 
    # <QueryDict: {'csrfmiddlewaretoken': ['3OKckjiy4WMphCTjudMba2l96JmiWsfM1nsfk3qpbFPYkJEfhokCiqbBtRxe8iOk'], 'fname': ['jamal'], 'lname': ['murray'], 'team': ['nuggets']}>
    #create a player using the info from form
    newPlayer = Player.objects.create(firstname = request.POST['fname'], lastname = request.POST['lname'] , team = request.POST['team'])
    print(newPlayer)
    return redirect("/")


def showPlayer(request, idPlayer):
    print("in showPlayer")
    print(idPlayer)
    # ClassName.objects.get(id=1) - gets the record in the table with the specified id
    playerToShow = Player.objects.get(id = idPlayer)
    print(playerToShow)
    context = {
        'playaPlaya': playerToShow
    }

    return render(request, "player.html", context)