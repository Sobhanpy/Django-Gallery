from django.db import models

# Create your models here.

class Services (models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=500)
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
#  __str__ function
    def __str__(self ):
        return self.title
    #  meta class
    class Meta:
        ordering = ['-created_data']
# contact class
class Contact (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=200)
    message = models.TextField()
#  __str__ function
    def __str__(self):
        return self.name
# price class
class Price(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
#  __str__ function
    def __str__(self):
        return self.name