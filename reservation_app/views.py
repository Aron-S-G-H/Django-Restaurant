from django.shortcuts import render
from django.views.generic import View
from django.contrib import messages
from .forms import ReservationForm


# Create your views here.

class Reserve(View):
    def get(self, request):
        form = ReservationForm()
        return render(request, 'reservation_app/reservation.html', {'forms': form})

    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reservation Complete')

        return render(request, 'reservation_app/reservation.html', {'forms': form})
