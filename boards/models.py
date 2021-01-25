from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import Writer


class Posting(models.Model):
    writer = models.ForeignKey(Writer, on_delete=models.SET_NULL, related_name='postings', null=True)
    title = models.CharField(_('제목'), max_length=50)
    content = models.TextField(_('내용'))

    created_datetime = models.DateTimeField(auto_now_add=True, blank=True)
    updated_datetime = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        ordering = ('-created_datetime', )

    def __str__(self):
        return self.title
