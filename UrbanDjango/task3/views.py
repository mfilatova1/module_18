from django.shortcuts import render

# Create your views here.

def cart(request):
    return render(request, 'third_task/cart.html')

def games(request):
    title = "Games"
    name = "Игры"
    button = "Купить"
    game1 = "Atomic Heart"
    game2 = "Cyberbank 2077"
    game3 = "PayDay 2"
    context = {
        'title': title,
        'name': name,
        'button': button,
        'game1': game1,
        'game2': game2,
        'game3': game3,

    }
    return render(request, 'third_task/games.html', context)

def platform(request):
    return render(request, 'third_task/platform.html')