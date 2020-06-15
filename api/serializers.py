from api.models import User, Profile, Post
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    nbposts = serializers.SerializerMethodField()
    nbfollowers = serializers.SerializerMethodField()
    nbfollowing = serializers.SerializerMethodField()
    nblikes = serializers.SerializerMethodField()
    followed = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['display_name', 'bio', 'picture', 'nbposts', 'nbfollowers', 'nbfollowing', 'nblikes', 'followed']

    def get_nbposts(self, profile):
        return profile.user.post_set.count()

    def get_nbfollowers(self, profile):
        return profile.followers.count()

    def get_nbfollowing(self, profile):
        return profile.following.count()

    def get_nblikes(self, profile):
        return profile.user.liked_posts.count()

    def get_followed(self, profile):
        if self.context['request'].user.profile.following.filter(id=profile.user.id).count() > 0:
            return True
        return False

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'profile']

    # def __init__(self, *args, **kwargs): #petit hack pour que ProfileSerializer ait bien accès au contexte (pour current_user)
    #     super().__init__(*args, **kwargs)
    #     self.fields['profile'].context.update(self.context)

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'text', 'created', 'liked']
        read_only_fields = ['id', 'created']

    def get_liked(self, post):
        if post.likes.filter(id=self.context['request'].user.id).count() > 0:
            return True
        return False
