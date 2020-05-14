from django.contrib.auth.models import User

from rest_framework.response import Response

class Login(generics.GenericAPIView):
	def post(self, request, *args, **kwargs):
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			resp = serialize user (selfUser, différent de user: infos privées, timeline...)
		else:
			resp = {'error': 'Error'}
		return Response(resp)

class Register(generics.GenericAPIView):
	def post(self, request, *args, **kwargs):
		user = User.objects.create_user(username, email, password)
		return Response(resp)