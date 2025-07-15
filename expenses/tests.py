from django.test import TestCase
from django.contrib.auth.models import User
from .models import Expense
from decimal import Decimal
from django.urls import reverse

class ExpenseModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.expense = Expense.objects.create(
            title='Test Expense',
            amount=Decimal('100.00'),
            description='Test description',
            expense_date='2023-01-01',
            category='food',
            user=self.user
        )

    def test_expense_creation(self):
        self.assertEqual(self.expense.title, 'Test Expense')
        self.assertEqual(self.expense.amount, Decimal('100.00'))
        self.assertEqual(self.expense.user, self.user)

class ExpenseViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_expense_list_view(self):
        response = self.client.get(reverse('expense_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'expenses/expense_list.html')