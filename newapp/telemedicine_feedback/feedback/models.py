from django.db import models


class Feedback(models.Model):
    user_name = models.CharField(max_length=100)
    session_id = models.IntegerField()

    def __str__(self):
        return self.user_name
