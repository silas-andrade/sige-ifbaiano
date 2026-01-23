from django.db import models
import uuid
from accounts.models import User  # ajuste se o app tiver outro nome

class Token(models.Model):
    token = models.PositiveIntegerField(default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    usada = models.BooleanField(default=False)
    hora_uso = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"Ficha {self.ficha_numero} - {self.aluno}"