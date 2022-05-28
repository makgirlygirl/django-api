from django.db import models

# Create your models here.
class Paragraph(models.Model):
    paragraphId = models.IntegerField()
    paragraphBody = models.TextField(max_length=2000)

class Question(models.Model):
    questionId = models.IntegerField()
    paragraph = models.IntegerField()
    questionTitle = models.TextField(max_length=100)
    answer = models.TextField(max_length=100)
    distractor1 = models.TextField(max_length=100)
    distractor2 = models.TextField(max_length=100)
    distractor3 = models.TextField(max_length=100)
    distractor4 = models.TextField(max_length=100)