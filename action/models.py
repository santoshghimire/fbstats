from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserData(models.Model):
    name = models.CharField(max_length=1000, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return str(self.name)

    # def save(self, *args, **kwargs):
    #     request = kwargs.get('request')
    #     print(request)
    #     if request.user.is_authenticated():
    #         self.user = request.user
    #     else:
    #         print("User not authenticated")
    #     super(UserData, self).save(*args, **kwargs)
