import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .managers import AuthorQuerySet
from netfields import InetAddressField, NetManager


class Author(models.Model):
    # name = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    inet = InetAddressField(null=True)

    def __str__(self):
        return str(self.name)

    """
    3. Add an IP address field to the author model and implement a custom lookup field
    for IsContainedByOrEqual using PostgreSQL inet operators
    """
    objects = NetManager()


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    pub_date = models.DateField('Date Published')
    author = models.ForeignKey(
        Author, verbose_name='author', related_name='polls', on_delete=models.CASCADE)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(
        Question, related_name="choices", on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
