from django.db import models
from accounts.models import EmailUser

# from datetime import datetime

# obj.date_modified = datetime.now()

class TubeDetails(models.Model):
    user = models.OneToOneField(EmailUser, on_delete=models.CASCADE, unique=True)
    channelid = models.CharField(max_length=500, unique=True)
    count = models.PositiveIntegerField(default=0)
    date = models.DateField()

    def __str__(self) -> str:
        return (self.user.email + ' <-> ' + self.channelid + ' <-> ' + str(self.count) + ' <-> ' + str(self.date))
    
# class TubeData(models.Model):
#     user = models.OneToOneField(EmailUser, on_delete=models.CASCADE, unique=True)  
#     count = models.PositiveIntegerField()
#     day = models.DateField()