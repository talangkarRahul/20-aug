from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.question_text

