from django.db import models
from django.contrib.auth import get_user_model


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    #date_updated = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image = models.URLField(null=True, blank=True)
    category = models.CharField(max_length=50, choices=[("dogs", "Dogs"), ("cats", "Cats"), ("dadj", "Dad's Jokes"), ("other", "Other")], blank=True)