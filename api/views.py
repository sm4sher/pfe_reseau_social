from django.contrib.auth.models import User

from api.models import Post
from api.serializers import PostSerializer

from rest_framework.response import Response
from rest_framework import generics

# class Login(generics.GenericAPIView):
# 	def post(self, request, *args, **kwargs):
# 		user = authenticate(request, username=username, password=password)
# 		if user is not None:
# 			login(request, user)
# 			resp = serialize user (selfUser, différent de user: infos privées, timeline...)
# 		else:
# 			resp = {'error': 'Error'}
# 		return Response(resp)

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

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer