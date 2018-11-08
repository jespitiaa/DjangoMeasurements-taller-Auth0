from django.contrib import admin
from . models import Measurement, Average, Variable, Threshold

# Register your models here.
admin.site.register(Measurement)
admin.site.register(Variable)
admin.site.register(Threshold)
admin.site.register(Average)
