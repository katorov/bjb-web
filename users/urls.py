from django.urls import path

from users.views import UserUpdateView

urlpatterns = [
    path('<str:username>/', UserUpdateView.as_view()),
]