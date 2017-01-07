from django.db import models
from django.utils import timezone

# Create your models here.
class Guidlist(models.Model):
    gl_register = models.ForeignKey('auth.user')
    gl_guid = models.CharField(max_length=40)
    gl_gt_gameId = models.IntegerField()
    gl_insertDate = models.DateTimeField(default=timezone.now)
    gl_exportDate = models.DateTimeField(blank=True, null=True)
    gl_bannedDate = models.DateTimeField(blank=True, null=True)
    gl_unbannedDate = models.DateTimeField(blank=True, null=True)
    gl_currentBanStatus = models.IntegerField()
    gl_desc = models.TextField()

    def export(self):
        self.gl_exportDate = timezone.now()
        self.gl_currentBanStatus = 1
        self.save()

    def banned(self):
        self.gl_bannedDate = timezone.now()
        self.gl_currentBanStatus = 3
        self.save()

    def unbanned(self):
        self.gl_unbannedDate = timezone.now()
        self.gl_currentBanStatus = 2
        self.save()    

    def __str__(self):
        strTemp = self.gl_guid + '|' + self.gl_gt_gameId + '|' + self.gl_currentBanStatus
        return strTemp
