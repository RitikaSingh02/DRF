from django.conf import settings
from django.db import models


def status_image(user, file):
    return "upload_status_image/{user}/{file}".format(user=user, file=file)


class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True,
                             on_delete=models.SET_NULL)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=status_image,
                              null=True,
                              blank=True)
    email = models.EmailField(null=True, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "status"
        verbose_name = "status"
        # as django itself keep all the objects of that class with 's' appended so to stop that we can define it
        verbose_name_plural = "statuses"
# Create your models here.
