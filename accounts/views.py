from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import FormView, UpdateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile
from .forms import UserCreateForm

class UserRegistrationView(FormView):
    template_name = 'accounts/register.html'
    success_url = '/'
    form_class = UserCreateForm

    def form_valid(self, form):
        saved_user = form.save()
        user = authenticate(
            username=saved_user.username,
            password=form.cleaned_data['password1'])
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())

class EditProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'accounts/profile.html'
    fields = ('phone_number',)

    def get_object(self, queryset=None):
        return self.request.user.profile
