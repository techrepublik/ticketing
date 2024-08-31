from django import forms
from .models import Ticket, Category
from django.contrib.auth.forms import UserCreationForm
from .models import User


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'status', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class UserRegistrationForm(UserCreationForm):
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email',
                  'profile_picture', 'password1', 'password2']
