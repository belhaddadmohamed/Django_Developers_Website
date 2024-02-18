from rest_framework import serializers
from projects.models import Project, Tag, Review
from users.models import Profile, Message, Skill


# USERS ==========================================

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


# PROJECTS ==========================================

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__' 


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__' 


class ProjectSerializer(serializers.ModelSerializer):
    # owner = ProfileSerializer(many=False)
    # tags = TagSerializer(many=True)
    # Reviews = serializers.SerializerMethodField()    

    class Meta:
        model = Project
        fields = '__all__'


