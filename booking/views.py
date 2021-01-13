from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking, Workplace
from django.views.generic import DetailView, UpdateView, DeleteView, ListView

from pprint import pprint

# Create your views here.

class Workplace_(ListView):
    model = Workplace
    template_name='booking/booking.html'
    context_object_name = 'workplaces'

# def booking(request):
#     return render(request, 'booking/booking.html')

def all_booking(request):
    table = Booking.objects.order_by('workplace')
    data = {
        'table' : table
    }
    return render(request, 'booking/all_booking.html', data)

def create_booking(request, pk):

    time_tuple = []
    yyy = ''

    for el in Workplace.objects.all():
        if pk == el.number:
            yyy = el
            for i in el.free_time_for_booking:
                time_tuple.append((i, i))
    let = time_tuple
    error = ''
    if request.method == 'POST':
        form = BookingForm(pk, request.POST)
        if form.is_valid():
            form.save()
            return redirect('end_booking')
        else:
            error = 'Форма была не верной'

    form = BookingForm(pk, initial={
        'user': request.user.username,
        'workplace' : pk,
        })

    table = Booking.objects.order_by('workplace')
    data = {
        'form' : form,
        'error' : error,
        'id' : pk,
        'table' : table,
    }

    return render(request, 'booking/workplace.html', data)

def end_booking(request):
    table = Booking.objects.order_by('workplace')
    data = {
        'table' : table
    }
    return render(request, 'booking/end_booking.html', data)

class BookingDelete(DeleteView):
    model = Booking
    template_name = 'booking/delete.html'
    success_url = '/booking/end_booking/'



# def create_booking(request, workplace, datetime_from, datetime_to, user):
#     error = ''
#     if request.method == 'POST':
#         data = {
#             'workplace' : workplace,
#             'datetime_from' : datetime_from, 
#             'datetime_to' : datetime_to,
#             'user' : user
#         }
#     return render(request, 'booking/create_booking.html', data)