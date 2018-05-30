from django.urls import path
from . import views

#2.Lego creo una url en mi app
app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='inicio'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detalle'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='resultado'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='voto'),
]
