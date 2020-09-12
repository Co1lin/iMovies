from django.db import models

# Create your models here.

class Actor(models.Model):
    name = models.TextField(default='（演员）')
    gender = models.TextField(default='')
    birthday = models.TextField(default='')
    birthplace = models.TextField(default='')
    occupation = models.TextField(default='')
    introduction = models.TextField(default='（暂无）')
    # content = models.TextField()

    def __str__(self):
        return self.name

class CoActor(models.Model):
    coactor_id =  models.IntegerField()
    coactor_name = models.TextField(default='（合作演员）')
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    count = models.IntegerField()

class Movie(models.Model):
    actors = models.ManyToManyField(Actor, through='MovieActor')
    name = models.TextField(default='（电影）')
    score = models.FloatField(default=0.0)
    vote_count = models.IntegerField(default=0)
    date = models.DateField(default='1000-01-01')
    type = models.TextField(default='')
    region = models.TextField(default='')
    director = models.TextField(default='')
    scriptwriter = models.TextField(default='')
    introduction = models.TextField(default='（暂无）')

    def __str__(self):
        return self.name

class MovieActor(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    # addtional keys:

    def __str__(self):
        return self.movie.__str__() + " <-> " + self.actor.__str__()

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField(default='')
    writer = models.TextField(default='（评论者）')
    date = models.DateField(default='1000-01-01')

    def __str__(self):
        return self.movie.__str__() + ' : ' + self.content + self.writer
