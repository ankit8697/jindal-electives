from django.db import models
from django.contrib.auth.models import User

class Elective(models.Model):
    name = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)
    credit = models.IntegerField()
    school = models.CharField(max_length=100)
    cross = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    body = models.TextField()
    elective = models.ForeignKey(Elective, on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    total_score = models.IntegerField(default=0)

    def __str__(self):
        return self.body

    def increment(self):
        self.upvotes+=1
    
    def decrement(self):
        self.downvotes+=1

    def computeTotal(self):
        self.total_score = upvotes - downvotes
        if self.total_score < 0:
            self.total_score = 0
    
