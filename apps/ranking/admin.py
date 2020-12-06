from django.contrib import admin

# Register your models here.
from apps.categorias.models import Categoria

admin.site.register(Categoria)