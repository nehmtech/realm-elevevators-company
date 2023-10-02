from django.db import models

class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    services = models.CharField(max_length=100)
    subject = models.TextField()

    def __str__(self):
        return self.fullname



class Help(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



