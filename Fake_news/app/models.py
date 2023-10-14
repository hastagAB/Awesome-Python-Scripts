from django.db import models

# Create your models here.

class FakeNews_model(models.Model):
    title=models.CharField(max_length=100)
    text=models.TextField(max_length=2000)
    subject=models.CharField(max_length=20)
    date=models.CharField(max_length=10)

    def __str__(self):
        return self.title
