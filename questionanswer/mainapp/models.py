from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    asked_user = models.ForeignKey(User, on_delete=models.CASCADE)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=0)
    answer_content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    answered_user = models.ForeignKey(User, on_delete=models.CASCADE)
