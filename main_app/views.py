from django.shortcuts import render
from django.views.generic import View, TemplateView
from food_app.models import Food
from .models import HomeSlider, Gallery
from .forms import ContactForm
from django.contrib import messages


class Home(View):
    def get(self, request):
        foods = Food.objects.all()
        slider = HomeSlider.objects.all()
        gallery = Gallery.objects.all()
        return render(request, 'main_app/home.html',
                      {'foods': foods, 'ImgSlider': slider, 'ImgGallery': gallery})


class Menu(View):
    def get(self, request):
        foods = Food.objects.all()
        return render(request, 'main_app/menu.html', {'foods': foods})


class GalleryView(View):
    def get(self, request):
        gallery = Gallery.objects.all()
        return render(request, 'main_app/gallery.html', {'ImgGallery': gallery})


class About(TemplateView):
    template_name = 'main_app/about.html'


class Contact(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'main_app/contact.html', {'forms': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message Sent')

        return render(request, 'main_app/contact.html', {'forms': form})