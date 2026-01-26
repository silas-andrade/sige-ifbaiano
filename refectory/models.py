from django.db.models import Max
from accounts.models import User  # ajuste se o app tiver outro nome
from django.db import models
import uuid


class Token(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)
    used_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Ficha {self.token} - {self.user.full_name}"

    def save(self, *args, **kwargs):
        if not self.pk:
            last_token = Token.objects.aggregate(Max('token'))['token__max']
            self.token = (last_token or 0) + 1
        super().save(*args, **kwargs)