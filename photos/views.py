import os

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

import urllib
from urllib.parse import urlsplit
from random import shuffle

from pystagram.settings import STATIC_URL
from pystagram.settings import BASE_DIR
from .forms import PhotoForm
from .forms import SearchForm
from .models import Photo
from .models import get_photo
from .models import make_thumbnail


def delete_photos(request):
    Photo.objects.all().delete()
    return redirect('photos:list_photos')


def list_photos(request):
    photos = [ photo.thumb_url for photo in Photo.objects.all().order_by('-id')]
    return render(request, 'list_photos.html', {'photos':photos})


def view_photo(request, pk):
    photos = Photo.objects.all()
    return render(request, 'view_photo.html',{'photos':photos})


def import_photo(request):
    ''' 다음과 같은 포맷의 문자열이 imgs에 담겨서 넘어온다
    ['http://cnet4.cbsistatic.com/hub/i/r/2015/01/06/575c5dd6-d55e-44aa-b1b1-4dda78a
6683d/thumbnail/770x433/fb15539c8e6988f984b81578977a6d85/mercedes-f-015-press-ce
s-2015-3019.jpg', 'http://www.capiemall.com/wp-content/uploads/2015_honda_accord
_coupe_lx-s_fq_oem_1_7171.jpg', 'https://upload.wikimedia.org/wikipedia/commons/
thumb/6/65/Hands-free_Driving.jpg/220px-Hands-free_Driving.jpg', 'http://dreamat
ico.com/data_images/car/car-1.jpg', 'http://www.budgetjamaica.com/photos/suzukiS
wift.png']
    '''
    if request.method == 'POST':
        imgs = request.POST.get('imgs')
        imgs = imgs.replace('[', '')
        imgs = imgs.replace(']', '')
        imgs = imgs.replace(' ', '')
        imgs = imgs.replace("'", '')
        imglist = imgs.split(',')
        static_path = os.path.join(BASE_DIR, 'static')
        static_path = os.path.join(static_path, 'imgs')
        
        for im in imglist:
            try:
                filename = os.path.basename(urlsplit(im).path)
                img_url = '{}imgs/{}'.format(STATIC_URL, filename)
                imgpath = os.path.join(static_path, filename)
                urllib.request.urlretrieve(im, imgpath)

                thumb_path = make_thumbnail(imgpath, 100, 100)
                thumbpath, thumbext = os.path.split(thumb_path)
                thumb_url = '{}imgs/{}'.format(STATIC_URL, thumbext)

                photo = Photo()
                photo.image_url = img_url
                photo.thumb_url = thumb_url
                photo.save()

            except Exception as e:
                print('exception! @import_photo():', str(e))

    return redirect('photos:list_photos')


def search_photo(request):
    form = SearchForm()
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        form = SearchForm(request.POST)
        
        if form.is_valid():
            search = form.cleaned_data['search']
            imgs = get_photo(search)
            shuffle(imgs)
            imgs = imgs[0:4]

            return render(request, 'search_photo.html', {
                'form':form,
                'imgs':imgs,
            })

    return render(request, 'search_photo.html', {
                'form':form,
                'imgs':[]
            })