from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Expense
from .forms import ExpenseForm, CustomUserCreationForm, SearchForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Ro\'yxatdan o\'tish muvaffaqiyatli!')
            return redirect('expense_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    search_form = SearchForm(request.GET)

    if search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        category = search_form.cleaned_data.get('category')

        if query:
            expenses = expenses.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )

        if category:
            expenses = expenses.filter(category=category)

    context = {
        'expenses': expenses,
        'search_form': search_form,
    }
    return render(request, 'expenses/expense_list.html', context)


@login_required
def expense_create(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, 'Xarajat muvaffaqiyatli qo\'shildi!')
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/expense_form.html', {'form': form, 'title': 'Xarajat qo\'shish'})


@login_required
def expense_edit(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, 'Xarajat muvaffaqiyatli yangilandi!')
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expenses/expense_form.html', {'form': form, 'title': 'Xarajatni tahrirlash'})


@login_required
def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == 'POST':
        expense.delete()
        messages.success(request, 'Xarajat muvaffaqiyatli o\'chirildi!')
        return redirect('expense_list')
    return render(request, 'expenses/expense_confirm_delete.html', {'expense': expense})