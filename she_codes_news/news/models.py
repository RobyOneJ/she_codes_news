from django.db import models


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.TextField()
    category = models.CharField(max_length=50, choices=[("dogs", "Dogs"), ("cats", "Cats"), ("dadj", "Dad's Jokes"), ("other", "Other")], blank=True)