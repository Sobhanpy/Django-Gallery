#  tools
from django.contrib import admin
from .models import *
# register models
admin.site.register(Client)
admin.site.register(Category)
admin.site.register(Gallery)