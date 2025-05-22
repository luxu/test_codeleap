from django.db import models


class Careers(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    username = models.CharField(max_length=100)
    created_datetime = models.DateTimeField(auto_now_add=True)
    author_ip = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return self.title
