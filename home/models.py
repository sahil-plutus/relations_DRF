from django.db import models


class Singer(models.Model):
    name = models.CharField(max_length=122)
    gender = models.CharField(max_length=122)
    def __str__(self):
        return self.name
    


class Song(models.Model):
    title = models.CharField(max_length=122)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='song')
    duration = models.IntegerField()

    def __str__(self):
        return str(self.title)