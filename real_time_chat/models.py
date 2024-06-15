from django.db import models
import shortuuid
from great_chat.models import AbstractBaseModel
from account.models import Account
# Create your models here.

class ChatGroup(AbstractBaseModel):
    group_name = models.CharField(max_length=128, unique=True, default=shortuuid.uuid)
    users_online = models.ManyToManyField(Account, related_name='online_in_groups', blank=True)
    members = models.ManyToManyField(Account, related_name='chat_groups', blank=True)
    is_private = models.BooleanField(default=False)
    admin = models.ForeignKey(Account, related_name="groupchats",blank=True, null=True, on_delete=models.SET_NULL)
    group_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True, default='profile_photos/group_chat.png')
    file = models.FileField(upload_to='files/', blank=True, null=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.group_name
    
class GroupMessage(AbstractBaseModel):
    group = models.ForeignKey(ChatGroup, related_name="chat_messages", on_delete=models.CASCADE)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    body = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.author.username} : {self.body}"
        
    class Meta:
        ordering = ['-created']
