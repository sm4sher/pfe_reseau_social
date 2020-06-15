#from django.contrib.auth import get_user_model
#User = get_user_model()
from django.contrib.auth import authenticate, login, logout

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from api.models import Post, User
from api.serializers import PostSerializer, UserSerializer

class Login(APIView):
	def post(self, request):
		username = request.data['username']
		password = request.data['password']
		print(username, password)
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			#resp = serialize user (selfUser, différent de user: infos privées, timeline...)
			s = UserSerializer(user, context={'request': request})
			resp = {'status': 'success', 'user': s.data}
		else:
			resp = {'status': 'failure', 'error': 'Username or password is invalid'}
		return Response(resp)

class Logout(APIView):
	def get(self, request):
		logout(request)
		return Response()

# class Register(generics.GenericAPIView):
# 	def post(self, request, *args, **kwargs):
# 		user = User.objects.create_user(username, email, password)
# 		return Response(resp)

# class Posts(generics.GenericAPIView):
# 	def get(self, request, *args, **kwargs):
# 		posts = {"posts": [
# 					{
# 						"id": 1,
# 						"author": None,
# 						"text": "test post1",
# 					},
# 					{
# 						"id": 2,
# 						"author": None,
# 						"text": "test post2",
# 					},
# 					{
# 						"id": 3,
# 						"author": None,
# 						"text": "test post3",
# 					}
# 				]}
# 		return Response(posts)

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
    	serializer.save(author=self.request.user)

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	lookup_field = 'username'
	serializer_class = UserSerializer
	permission_classes = [IsAuthenticated]

class UserPostList(generics.ListAPIView):
	serializer_class = PostSerializer

	def get_queryset(self):
		user = User.objects.get(username=self.kwargs['username'])
		return user.post_set.all()

class UserLikeList(generics.ListAPIView):
	serializer_class = PostSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		user = User.objects.get(username=self.kwargs['username'])
		return user.liked_posts.all()

class LikePost(APIView):
	permission_classes = [IsAuthenticated]

	def post(self, request, pk):
		post = Post.objects.get(id=pk)
		like = post.likes.filter(id=self.request.user.id)
		if like.count() > 0:
			post.likes.remove(like.first())
			r = False
		else:
			post.likes.add(self.request.user)
			r = True
		post.save()
		return Response({'post_id': pk, 'liked': r})

class FollowUser(APIView):
	permission_classes = [IsAuthenticated]

	def post(self, request, username):
		print("username:", username)
		user = User.objects.get(username=username)
		follow = user.profile.followers.filter(id=self.request.user.id)
		if follow.count() > 0:
			user.profile.followers.remove(follow.first())
			r = False
		else:
			user.profile.followers.add(self.request.user.profile)
			r = True
		user.save()
		return Response({'user_id': user.id, 'followed': r})
