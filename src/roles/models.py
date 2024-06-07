from django.db import models

# Create your models here.
class Role(models.Model):
    role_name = models.CharField(max_length=300,  blank=True, null=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return str(self.role_name)