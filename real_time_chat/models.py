from django.db import models
from great_chat.models import AbstractBaseModel
from account.models import Account
# Create your models here.

class ChatGroup(AbstractBaseModel):
    group_name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.group_name
    
class GroupMessage(AbstractBaseModel):
    group = models.ForeignKey(ChatGroup, related_name="chat_messages", on_delete=models.CASCADE)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.author.username} : {self.body}"
        
    class Meta:
        ordering = ['-created']
