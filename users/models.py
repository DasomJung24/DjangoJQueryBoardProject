from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class Writer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', blank=True, null=True)

    name = models.CharField(_('이름'), max_length=20)

    created_datetime = models.DateTimeField(auto_now_add=True, blank=True)
    updated_datetime = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name
