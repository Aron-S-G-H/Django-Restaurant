from django.urls import path
from . import views
from django.conf.urls.static import static
from YamiFood import settings

app_name = 'main'
urlpatterns = [
    path('', views.Home.as_view(), name='home_page'),
    path('menu', views.Menu.as_view(), name='menu_page'),
    path('about', views.About.as_view(), name='about_page'),
    path('contact', views.Contact.as_view(), name='contact_page'),
    path('gallery', views.GalleryView.as_view(), name='gallery_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
