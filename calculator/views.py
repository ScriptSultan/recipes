from django.http import HttpResponseBadRequest
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def menu(request):
    count = request.GET.get('count', 1)
    recept = request.GET.get('recept')
    print(recept)
    recipe = DATA[str(recept)]
    print(recipe)
    context = {recept: recipe, "count": int(count)}
    return render(request, 'calculator/index.html', context)

# def menu(request, name):
#     count = int(request.GET.get('count', '1'))
#     ingredients = DATA.get(name, None)
#     for ingrid in ingredients:
#         ingredients[ingrid] *= count
#     context = {
#         'recipe': ingredients,
#     }
#     return render(request, 'calculator/index.html', context)

