from django.db import models

class CertificacionCurso(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='certificaciones_cursos/')
    plataforma = models.CharField(max_length=100)
    fecha_realizacion = models.DateField()
    dificultad = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo
