from django.db import models


class Post(models.Model):
    titulo = models.CharField(max_length=20)
    cuerpo = models.TextField()

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    post = models.ForeignKey(Post, related_name='comentarios')
    padre = models.ForeignKey("self", related_name='hijos', null=True, blank=True)
    fecha = models.DateField()
    usuario = models.CharField(max_length=50)
    mensaje = models.TextField()

    def __str__(self):
        return str(self.fecha) + self.mensaje[:10]
