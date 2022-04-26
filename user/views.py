from django.contrib.auth import login, get_user_model
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import FormView, UpdateView, DetailView

from relation.models import Relation
from user.forms import RegistrationForm, LoginForm

User = get_user_model()


class RegisterView(FormView):
    form_class = RegistrationForm
    template_name = 'user/register.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'user/login.html'
    success_url = '/'

    def form_valid(self, form):
        login(self.request, form.cleaned_data['user'])
        return super().form_valid(form)


class ProfileUpdateView(UpdateView):
    model = User
    template_name = 'user/profile_update.html'
    fields = ['username', 'avatar', 'bio', 'website']
    success_url = '/'

    def get_object(self, queryset=None):
        return self.request.user


class ProfileDetailView(DetailView):
    model = User
    slug_url_kwarg = 'username'
    slug_field = 'username'
    template_name = 'user/profile.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        user = self.get_object()
        # contex['followers_count'] = user.followers.count()
        contex['followers_count'] = cache.get_or_set('{}:followers'.format(user.username), user.followers.count())
        # contex['followings_count'] = user.followings.count()
        contex['followings_count'] = cache.get_or_set('{}:followings'.format(user.username), user.followings.count())
        contex['posts_count'] = user.posts.count()
        contex['is_following'] = Relation.objects.filter(from_user=self.request.user, to_user=user).exists()
        return contex
