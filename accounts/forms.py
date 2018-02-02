from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField


class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email")
        field_classes = {'username': UsernameField}