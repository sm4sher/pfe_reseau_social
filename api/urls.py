from django.urls import path, include

import api.views

urlpatterns = [
	path('login/', views.Login.as_view()),
	path('register/', views.Register.as_view()),
]