from django.db import models
from datetime import datetime

class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)
    author = models.CharField(max_length=50, default='')
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now=False, default=datetime.now())

    def __str__(self):
    # def __unicode__(self):
        return self.title