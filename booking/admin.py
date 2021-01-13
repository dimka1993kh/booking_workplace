from django.contrib import admin
from .models import Booking
from .models import Workplace

admin.site.register(Booking)
admin.site.register(Workplace)