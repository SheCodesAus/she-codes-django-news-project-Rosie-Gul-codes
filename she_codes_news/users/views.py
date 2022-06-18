from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class AccountDetailsView(generic.TemplateView):
    template_name = 'users/Account_Details.html'
# Create your views here.

class AllUsersView(generic.ListView):
    template_name = "users/allUsers.html"
    
    def get_queryset(self):
        return CustomUser.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_users"] = CustomUser.objects.all()
        return context