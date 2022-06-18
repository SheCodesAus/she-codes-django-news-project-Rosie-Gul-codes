from django.urls import path
from .views import AllUsersView, CreateAccountView, AccountDetailsView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(),
name='createAccount'),
    path('account-details/', AccountDetailsView.as_view(),
name='AccountInformation'),
    path('list-of-authors/', AllUsersView.as_view(), name='FilterByAuthors'), 
]

