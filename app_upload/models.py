from django.db import models
from accounts.models import user


class Flile(models.Model):

    name = models.CharField(max_length=255,blank=True,null=True)
    size = models.BigIntegerField(null=True,blank=True)
    body = models.FileField(upload_to='user/files')
    user = models.ForeignKey(user,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username}/{self.name}"