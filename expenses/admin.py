from django.contrib import admin
from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount', 'category', 'expense_date', 'user', 'created_at']
    list_filter = ['category', 'expense_date', 'user']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']