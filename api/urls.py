from django.urls import path, include

import api.views as views

urlpatterns = [
	#path('login/', views.Login.as_view()),
	#path('register/', views.Register.as_view()),
	path('posts/', views.PostList.as_view()),
	path('posts/<int:pk>/', views.PostDetail.as_view()),
]