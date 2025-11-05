from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    public_date = models.DateTimeField(default=timezone.now)

    def summary(self):
        return self.body[:100]

    def __str__(self):
        return f"{self.title} - {self.public_date.strftime('%Y-%m-%d')}"
