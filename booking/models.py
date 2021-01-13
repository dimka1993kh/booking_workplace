from django.db import models
from django import forms

time_list = []
for i in range(8, 19):
    time_list.append((i, i))
time_tuple = tuple(time_list)







class Workplace(models.Model):
    number = models.IntegerField('Номер рабочего места')
    free_time_default = {
        '8' : {'title' : '8:00 - 9:00', 'status_free' : True},
        '9' : {'title' : '9:00 - 10:00', 'status_free' : True},
        '10' : {'title' : '10:00 - 11:00', 'status_free' : True},
        '11' : {'title' : '11:00 - 12:00', 'status_free' : True},
        '12' : {'title' : '12:00 - 13:00', 'status_free' : True},
        '13' : {'title' : '13:00 - 14:00', 'status_free' : True},
        '14' : {'title' : '14:00 - 15:00', 'status_free' : True},
        '15' : {'title' : '15:00 - 16:00', 'status_free' : True},
        '16' : {'title' : '16:00 - 17:00', 'status_free' : True},
        '17' : {'title' : '17:00 - 18:00', 'status_free' : True},
    }

    free_time_for_booking = models.JSONField('Свободное время для записи', default=free_time_default)

    class Meta:
        verbose_name = 'Рабочее место'
        verbose_name_plural = 'Рабочие места'

    def __str__(self):
        return f'Рабочее место {self.number}'    

# def uuu(**kwargs):
#     print('dddddddddddddddddddddddddddd',kwargs) 

class Booking(models.Model):

    user = models.CharField('Пользователь', max_length=20)
    workplace = models.IntegerField('Номер рабочего места')
    datetime_from = models.IntegerField('Со скольки хотите работать', max_length=1000)
    datetime_to = models.IntegerField('До скольки хотите работать', max_length=20, choices=time_tuple)
    

    # def __init__(self, some_data, *args, **kwargs):
    #     super(Booking, self).__init__(*args, **kwargs)
    #     self.fields['datetime_from'] = some_data
    
   
    def __str__(self):
        return f'Рабочее место {self.workplace}, пользователь {self.user}'

    class Meta:
        verbose_name = 'Бронь рабочего места'
        verbose_name_plural = 'Бронь рабочих мест'
