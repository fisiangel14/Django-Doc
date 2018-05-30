from django.contrib import admin

from .models import Question, Choice

# Register your models here.

#6.Despues de crear un usuario para el sitio de administracion
#7.Debemos registrar aqui nuestras app, para su modificacion

admin.site.register(Question)
admin.site.register(Choice)
