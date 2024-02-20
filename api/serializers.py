from rest_framework import serializers
from projects.models import Project, Tag, Review
from users.models import Profile, Message, Skill


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


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
    # reviews = serializers.SerializerMethodField()

    # def get_reviews(self, obj):
    #     reviews = obj.review_set.all()
    #     serializer = ReviewSerializer(reviews, many=True)
    #     return serializer

    class Meta:
        model = Project
        fields = '__all__'

    # def create(self, validated_data):
    #     print('Try to create new project...')
    #     print(validated_data)
    #     obj = Project.objects.create(
    #         title = validated_data['title'],
    #         description = validated_data['description'],
    #     )
    #     return obj





