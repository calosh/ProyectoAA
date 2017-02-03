from django.contrib import admin

# Register your models here.
from .models import Codigo


class CodigoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nombre",)}

admin.site.register(Codigo, CodigoAdmin)
