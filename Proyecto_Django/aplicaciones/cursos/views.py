from django.shortcuts import render

from .models import CertificacionCurso

def lista_certificaciones_cursos(request):
    certificaciones_cursos = CertificacionCurso.objects.all()
    return render(request, 'lista_certificaciones_cursos.html', {'certificaciones_cursos': certificaciones_cursos})

def detalle_certificacion_curso(request, certificacion_curso_id):
    certificacion_curso = CertificacionCurso.objects.get(id=certificacion_curso_id)
    return render(request, 'detalle_certificacion_curso.html', {'certificacion_curso': certificacion_curso})
