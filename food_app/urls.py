from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('detail/<slug:slug>', views.FoodDetail.as_view(), name='FoodDetail_page'),
    path('search', views.food_search, name='foodSearch_page'),
]
