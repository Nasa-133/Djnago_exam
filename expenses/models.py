from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Oziq-ovqat'),
        ('transport', 'Transport'),
        ('bills', 'To\'lovlar'),
        ('other', 'Boshqa'),
    ]

    title = models.CharField(max_length=200)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    description = models.TextField(blank=True, null=True)
    expense_date = models.DateField()
    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default='other'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-expense_date', '-created_at']

    def __str__(self):
        return f"{self.title} - {self.amount}"