from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Food, Comment


class FoodDetail(View):
    def get(self, request, slug):
        food = get_object_or_404(Food, slug=slug)
        recent_foods = Food.objects.all().order_by('-date')[:5]
        food_types = Food.TYPES

        return render(request, 'food_app/food-details.html',
                      {'food_details': food, 'recent_foods': recent_foods, 'food_types': food_types})

    def post(self, request, slug):
        food = get_object_or_404(Food, slug=slug)
        recent_foods = Food.objects.all().order_by('-date')[:5]
        food_types = Food.TYPES

        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('text')
        parent_id = request.POST.get('parent_id')
        print(parent_id, type(parent_id))
        print(name, email)
        print(text)

        Comment.objects.create(food=food, name=name, email=email, text=text, parent_id=parent_id)

        return render(request, 'food_app/food-details.html',
                      {'food_details': food, 'recent_foods': recent_foods, 'food_types': food_types})



def food_search(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        print(query)
        food = get_object_or_404(Food, name__icontains=query)
        recent_foods = Food.objects.all().order_by('-date')[:5]
        food_types = Food.TYPES
        return render(request, 'food_app/food-details.html',
                      {'food_details': food, 'recent_foods': recent_foods, 'food_types': food_types})
