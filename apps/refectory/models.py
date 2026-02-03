from django.db import models
from django.db.models import Max
from django.utils import timezone
import uuid

from apps.users.models import User


class Token(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    token = models.PositiveIntegerField()


    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)
    used_at = models.DateTimeField(null=True, blank=True)

    is_valid = models.BooleanField(default=True)

    invalidated_reason = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Ficha {self.token} - {self.user.full_name}"