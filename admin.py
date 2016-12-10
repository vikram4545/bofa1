from django.contrib import admin

from .models import Number,Holder,Employer
admin.site.register(Employer)
admin.site.register(Number)
admin.site.register(Holder)

