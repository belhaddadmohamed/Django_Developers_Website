from django.shortcuts import render
from projects.models import Project, Review, Tag
from users.models import Profile

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProjectSerializer, TagSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'},
        {'POST': '/api/projects/id/vote'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
    ]

    return Response(routes)



@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getProject(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def createProject(request):
    serializer = ProjectSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)



@api_view(['GET'])
def getTags(request):
    tags = Tag.objects.all()
    serializer = TagSerializer(tags, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def createTag(request):
    serializer = TagSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

