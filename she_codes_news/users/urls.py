from django.urls import path
from .views import CreateAccountView, ViewProfileView

app_name = 'users'
urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>/', ViewProfileView.as_view(), name='viewProfile')
]