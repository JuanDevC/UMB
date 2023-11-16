from django.urls import path
from . import views

app_name = 'cursos'

urlpatterns = [
    path('', views.lista_certificaciones_cursos, name='lista_certificaciones_cursos'),
    path('<int:certificacion_curso_id>/', views.detalle_certificacion_curso, name='detalle_certificacion_curso'),
]

