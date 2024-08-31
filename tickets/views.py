
from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket, Category
from .forms import TicketForm, CategoryForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# User Registration View


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

# User Login View


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

# User Logout View


def logout_view(request):
    logout(request)
    return redirect('login')

# Dashboard View


@login_required
def dashboard_view(request):
    tickets = Ticket.objects.filter(created_by=request.user)
    categories = Category.objects.all()
    ticket_counts = {
        'open': tickets.filter(status='open').count(),
        'in_progress': tickets.filter(status='in_progress').count(),
        'closed': tickets.filter(status='closed').count(),
    }
    context = {
        'tickets': tickets,
        'categories': categories,
        'ticket_counts': ticket_counts,
    }
    return render(request, 'dashboard.html', context)

# Ticket List View


@login_required
def ticket_list_view(request):
    tickets = Ticket.objects.all()
    categories = Category.objects.all()
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets, 'categories': categories})

# Ticket Create View


@login_required
def ticket_create_view(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user
            ticket.save()
            messages.success(request, 'Ticket created successfully.')
            return redirect('ticket-list')
    else:
        form = TicketForm()
    return render(request, 'tickets/ticket_form.html', {'form': form})

# Ticket Update View


@login_required
def ticket_update_view(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ticket updated successfully.')
            return redirect('ticket-list')
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'tickets/ticket_form.html', {'form': form, 'ticket': ticket})

# Ticket Delete View


@login_required
def ticket_delete_view(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        ticket.delete()
        messages.success(request, 'Ticket deleted successfully.')
        return redirect('ticket-list')
    return render(request, 'tickets/ticket_confirm_delete.html', {'ticket': ticket})

# Category List View


@login_required
def category_list_view(request):
    categories = Category.objects.all()
    return render(request, 'categories/categories.html', {'categories': categories})

# Category Create View


@login_required
def category_create_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category created successfully.')
            return redirect('category-list')
    else:
        form = CategoryForm()
    return render(request, 'categories/category_form.html', {'form': form})

# Category Update View


@login_required
def category_update_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully.')
            return redirect('category-list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/category_form.html', {'form': form, 'category': category})

# Category Delete View


@login_required
def category_delete_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category deleted successfully.')
        return redirect('category-list')
    return render(request, 'categories/category_confirm_delete.html', {'category': category})
