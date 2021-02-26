from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    technology = models.CharField(max_length=32)
    image = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.title},  {self.technology}"

