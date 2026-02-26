from django import forms
from complains.models import Complain, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = ('title', 'category', 'featured_image', 'short_description', 'complain_body', 'complain_status')
        labels={
            'title': 'caption',
            'short_description':'Location'
        }
        # slug is NOT in fields — we generate it in the view


class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')