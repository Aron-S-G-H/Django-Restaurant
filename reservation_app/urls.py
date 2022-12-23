from django.urls import path
from .views import Reserve

app_name = 'reservation'
urlpatterns = [
    path('', Reserve.as_view(), name='reserve_page')
]
