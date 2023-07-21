from django.shortcuts import render, redirect
from .models import Food, Consume

def index(request):
    if request.method == "POST":
        food_consumed = request.POST.get('food_consumed')
        if food_consumed:
            try:
                consume = Food.objects.get(name=food_consumed)
                user = request.user
                consume = Consume(user=user, food_consumed=consume)
                consume.save()
            except Food.DoesNotExist:
                pass

    foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user) if request.user.is_authenticated else []

    return render(request, 'myapp/index.html', {'foods': foods, 'consumed_food': consumed_food})


def delete_consume(request, id):
    if request.method == 'POST':
        consumed_food = Consume.objects.filter(id=id)
        consumed_food.delete()
        return redirect('/')
    return render(request, 'myapp/delete.html')
