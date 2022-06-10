from django.urls import path
from .views import CreateAccountView, AccountDetailsView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(),
name='createAccount'),
    path('account-details/', AccountDetailsView.as_view(),
name='AccountInformation'),
]

