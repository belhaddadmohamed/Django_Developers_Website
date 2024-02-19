from django.db import models
from users.models import Profile
import uuid

# Create your models here.

class Project(models.Model):
    owner = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(upload_to="project/", default="project/default.jpg", null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', null=True, blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVote = reviews.filter(value='up').count()
        totalVotes = reviews.count()
        ratio = (upVote / totalVotes) * 100
        print("the ratio= " + str(ratio))

        self.vote_total = totalVotes
        self.vote_ratio = ratio
        self.save()

    @property
    def reviewers(self):
        # Give me the list of 'id' of the reviewers of this project (flat means : convert it to a True list because it was an object)
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset

    class Meta:
        ordering = ['-vote_ratio', '-vote_total', 'title']



class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        unique_together = [['owner', 'project']]

    def __str__(self):
        return str(self.value) +" / "+ str(self.owner) +" / "+ str(self.project) 



class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name