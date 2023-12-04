from django.db import models
from django.contrib.auth import get_user_model
#from django.utils import timezone


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    last_update = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image = models.URLField(null=True, blank=True)
    category = models.CharField(max_length=50, choices=[
        ("dogs", "Dogs"), 
        ("cats", "Cats"), 
        ("motorbikes", "Motorbikes"), 
        ("other", "Other")
        ], blank=True)

    #removed the pub_date as visile editable field and made it appear automatically at creation and update story
    #def save(self, *args, **kwargs):
    #    self.pub_date = timezone.now()
    #    super(NewsStory, self).save(*args, **kwargs)