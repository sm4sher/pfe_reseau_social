from django.urls import path, include

import api.views as views

urlpatterns = [
	path('login/', views.Login.as_view()),
	path('logout/', views.Logout.as_view()),
	#path('register/', views.Register.as_view()),

	path('posts/', views.PostList.as_view()),
	path('posts/<int:pk>/', views.PostDetail.as_view()),
	path('posts/<int:pk>/like/', views.LikePost.as_view()),
	#path('posts/<int:pk>/comment', views.PostComment.as_view()),

	path('users/<str:username>/', views.UserDetail.as_view()),
	path('users/<str:username>/posts/', views.UserPostList.as_view()),
	path('users/<str:username>/likes/', views.UserLikeList.as_view()),
	#path('users/<str:username>/followers/', views.UserFollowerList.as_view()),
	#path('users/<str:username>/following/', views.UserFollowingList.as_view()),
	path('users/<str:username>/follow/', views.FollowUser.as_view()),
]