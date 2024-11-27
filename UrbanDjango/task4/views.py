from django.shortcuts import render

# Create your views here.

def cart(request):
    return render(request, 'fourth_task/cart.html')

def games(request):
    title = "Games"
    name = "Игры"
    button = "Купить"
    games = ["Atomic Heart", "Cyberbank 2077", "PayDay 2"]
    context = {
        'title': title,
        'name': name,
        'button': button,
        'games': games,

    }
    return render(request, 'fourth_task/games.html', context)

def platform(request):
    return render(request, 'fourth_task/platform.html')