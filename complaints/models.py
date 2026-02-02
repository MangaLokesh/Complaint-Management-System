from django.db import models
from django.contrib.auth.models import User

class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    room_no=models.TextField(max_length=10)
    status = models.CharField(max_length=20,default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

