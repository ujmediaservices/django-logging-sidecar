from django.db import models

class Logger(models.Model):
    """Logger object"""
    message = models.TextField()
    date_time = models.DateTimeField()
    def __str__(self):
        return self.title