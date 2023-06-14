from django.contrib import admin

from .models import Place

from .models import People
admin.site.register(People)

# Register your models here.
admin.site.register(Place)
