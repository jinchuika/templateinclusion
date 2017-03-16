from django.db import models


class Post(models.Model):
    titulo = models.CharField(max_length=20)
    cuerpo = models.TextField()


class Comentario(models.Model):
    post = models.ForeignKey(Post, related_name='comentarios')
    fecha = models.DateField()
    usuario = models.CharField(max_length=50)
    mensaje = models.TextField()
