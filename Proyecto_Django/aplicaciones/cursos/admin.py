from django.contrib import admin
from .models import CertificacionCurso

@admin.register(CertificacionCurso)
class CertificacionCursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'plataforma', 'fecha_realizacion', 'dificultad')
    search_fields = ('titulo', 'plataforma')
    list_filter = ('plataforma', 'fecha_realizacion', 'dificultad')

# Aquí podrías registrar otros modelos de la misma manera si los tienes
