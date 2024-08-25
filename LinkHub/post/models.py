import  uuid
from django.db import models
from django.utils.timesince import timesince
from account.models import User 

class PostAttachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='post_attachments')
    created_by = models.ForeignKey(User, related_name='post_attachments', on_delete=models.CASCADE)
    # post = models.ForeignKey('Post', related_name='attachments', on_delete=models.CASCADE)
    # file = models.FileField(upload_to='post_attachments/')

    # def __str__(self):
    #     return self.file.name

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(blank=True,null=True)
    attachment = models.ManyToManyField(PostAttachment, blank= True)
    # LIkes and Like count 
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    class Meta:
        ordering = ('-created_at',)

    def created_at_formatted(self):
        return timesince(self.created_at.name) 
