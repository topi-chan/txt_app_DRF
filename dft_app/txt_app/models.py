from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    '''
    Created at a beginning of a project for a better backward integration.
    May be developed (e.g. with more fields) later.
    '''

    id = models.AutoField(primary_key=True)

    def __str__(self):
        if (self.first_name and self.last_name) != '':
            return '{} {}'.format(self.first_name, self.last_name)
        else:
            return self.email


class Message(models.Model):

    id = models.AutoField(primary_key=True)
    tittle = models.CharField(max_length=80, blank=True)
    content = models.CharField(max_length=160)
    view_counter = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        if self.tittle != '':
            return self.tittle
        else:
            return self.id
