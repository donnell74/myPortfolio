from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GithubToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    github_username = models.CharField(max_length=256)
    token = models.TextField()
