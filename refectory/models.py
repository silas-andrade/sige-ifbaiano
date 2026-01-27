from django.db import models
from django.db.models import Max
from django.utils import timezone
import uuid

from accounts.models import User


class Token(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)
    used_at = models.DateTimeField(null=True, blank=True)

    is_valid = models.BooleanField(default=True)
    

    def __str__(self):
        return f"Ficha {self.token} - {self.user.full_name}"

    def save(self, *args, **kwargs):
        if not self.pk:
            today = timezone.now().date()

            last_token_today = Token.objects.filter(
                created_at__date=today
            ).aggregate(Max('token'))['token__max']

            self.token = (last_token_today or 0) + 1

        super().save(*args, **kwargs)