from django.db import models
from accounts.models import User


class Material(models.Model):
    name = models.CharField(max_length=50)
    total_quantity = models.PositiveIntegerField(default=0)
    available_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user')
    material = models.ForeignKey(Material, on_delete=models.DO_NOTHING)
    who_approved = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='who_approved', null=True, blank=True)
    quantity = models.PositiveIntegerField()
    expected_return_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    date_returned = models.DateTimeField(blank=True, null=True)
    is_returned = models.BooleanField(default=False)
    is_return_confirmed = models.BooleanField(default=False)
    who_confirmed_the_return = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='who_confirmed_the_return', null=True, blank=True)

    def __str__(self):
        return f'{self.user} | {self.material} | {self.is_returned} | {self.is_return_confirmed}'
    
    class Meta:
        ordering = ['-created_at']


class LoanApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    material = models.ForeignKey(Material, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    expected_return_date = models.DateTimeField()
    is_pending = models.BooleanField(default=True) 
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} | {self.material} | {self.is_pending} | {self.is_approved}'
    
    class Meta:
        ordering = ['-created_at']
        