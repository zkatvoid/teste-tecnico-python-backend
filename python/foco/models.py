from django.db import models


# Manager para centralizar as queries em comum, evitando duplicatas
class FocoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class Foco(models.Model):
    id: int
    objects = FocoManager()

    nivel_foco = models.PositiveIntegerField()
    tempo_minutos = models.PositiveIntegerField()
    comentario = models.TextField(null=True, blank=True, default=None)
    categoria = models.CharField(max_length=150, null=True, blank=True, default=None)
    data = models.DateTimeField(null=True, blank=True, default=None)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
