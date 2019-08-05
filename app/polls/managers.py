from django.db import models
from django.db.models import Q


class AuthorQuerySet(models.QuerySet):

    def IsContainedByOrEqual(self, query=None):
        print("in progress...")
        qs = self
        if query is not None:
            lookup = 'field__net_contains_or_equals'
            qs = qs.filter(lookup)
        return qs


class AuthorManager(models.Manager):

    def get_queryset(self):
        return AuthorQuerySet(self.model, using=self._db)

    def IsContainedByOrEqual(self):
        return self.get_queryset().IsContainedByOrEqual()
