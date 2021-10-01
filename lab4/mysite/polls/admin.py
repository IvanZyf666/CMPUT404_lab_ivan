
from django.contrib import admin

from .models import Choice, Question, Department

admin.site.site_header = 'My First Django Website Admin'
admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Department)