from django.db import models

# Create your models here.


class query(models.Model):
    ques = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.ques


