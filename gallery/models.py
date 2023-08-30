# tools
from django.db import models
from django.contrib.auth.models import User
# category class
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
# client class
class Client(models.Model):
    info = models.ForeignKey(User , on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)
    image = models.ImageField(upload_to='client')
    description = models.TextField()
    # __str__ function
    def __str__(self):
        return self.info.username
# gallery class
class Gallery(models.Model):
    content = models.TextField()
    category = models.ManyToManyField(Category)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='photo')
    project_date = models.DateTimeField()
    client_company=models.CharField(max_length=100)
    updated_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    # meta class
    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
    
    def capt(self):
        return self.title.capitalize()
