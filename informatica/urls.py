from django.urls import path

from . import views

app_name = 'informatica'

urlpatterns = [
    path('', views.index, name="index"),
    path('noticias/', views.noticias, name="noticias"),
    path('noticias/<int:notice_id>', views.noticia, name="noticia"),
    path('sobre_o_curso/', views.sobre_o_curso, name="sobre_o_curso")
]