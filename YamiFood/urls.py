from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('food/', include('food_app.urls')),
    path('reserve/', include('reservation_app.urls')),
    path('blog/', include('blog_app.urls')),
]
