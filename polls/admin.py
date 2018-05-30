from django.contrib import admin

from .models import Question, Choice

# Register your models here.

#6.Despues de crear un usuario para el sitio de administracion
#7.Debemos registrar aqui nuestras app, para su modificacion
#congiuramos mas el sitio de admin


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [
        ('Question',         {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
