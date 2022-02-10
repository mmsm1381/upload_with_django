from django.db import models
from django.contrib.auth.models import User


class Flile(models.Model):

    name = models.CharField(max_length=255,blank=True,null=True,unique=True)
    size = models.BigIntegerField(null=True,blank=True)
    body = models.FileField(upload_to='user/files')
    user = models.ForeignKey(User,on_delete=models.CASCADE , related_name="files",null=True)
    visitors = models.ManyToManyField(User)

    def __str__(self) -> str:
        return f"{self.user.username}/{self.name}"

    def set_file_size(self):
        self.size = self.body.size
        return self.size