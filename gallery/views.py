from django.shortcuts import render, get_object_or_404
from .models import *
# gallery function
def gallery(request,cat=None):
    category= Category.objects.all()
    gallery = Gallery.objects.filter(category__name=cat)
    context = {'category' : category,'gallery' : gallery}
    return render(request,'gallery/gallery.html',context=context)
# gallery information function
def gallery_information(request, id):
    galleries = get_object_or_404(Gallery, id=id)
    client = Client.objects.get(id=id)
    context = {'galleries': galleries,'client' : client,}
    return render(request, 'gallery/gallery-single.html', context=context)


