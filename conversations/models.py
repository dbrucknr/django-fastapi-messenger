from django.db import models
from django.contrib.auth import get_user_model

from conversations.managers import AsyncManager

class Conversation(models.Model):
    participants = models.ManyToManyField(to=get_user_model())
    created_at = models.DateTimeField(auto_now_add=True)

    objects = AsyncManager()

    def __str__(self):
        return f'{self.id}'


class Message(models.Model):
    sender = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    conversation = models.ForeignKey(to=Conversation, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = AsyncManager()

    def __str__(self):
        return f'{self.sender.username}: {self.content} [{self.timestamp}]'
