from .models import Booking, Workplace
from django.forms import ModelForm, TextInput, DateTimeInput, Select
from django import forms

from pprint import pprint

class BookingForm(ModelForm):

    def __init__(self, let, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        # self.fields['datetime_from'].queryset = Workplace.objects.get(number=let)
        ttt = kwargs['initial']['workplace']
        print(ttt)
    class Meta:
        model = Booking 
        fields = ['user', 'workplace', 'datetime_from', 'datetime_to']    

        widgets = {
                'user' : TextInput(attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Пользователь'
                }),
                'workplace' : TextInput(attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Номер рабочего места'                    
                }), 
                'datetime_from' : Select(attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Со скольки хотите начать работать'                  
                }), 
                'datetime_to' : Select(attrs={
                    'class' : 'form-control',
                    'placeholder' : 'До скольки хотите работать'                   
                }),                                                        
        }
        

class WorkplaceForm(ModelForm):
    class Meta:
        model = Workplace
        fields = ['number', 'free_time_for_booking']

