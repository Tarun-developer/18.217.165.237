from django.contrib import admin
# from models import *
# Register your models here.

from .models import Property
from .models import Preference


admin.site.register(Property)
admin.site.register(Preference)
