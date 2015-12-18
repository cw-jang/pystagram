import os

from django.db import models
from django.conf import settings

import urllib
from bs4 import BeautifulSoup
from PIL import Image

class Photo(models.Model):
    image_url = models.CharField(max_length=512)
    thumb_url = models.CharField(max_length=512)


# Downloading Google Images with Python Tutorial 참고
# https://www.youtube.com/watch?v=WHboCBSVTWU
def get_photo(search):
    search = search.replace(' ', '%20')
    url = 'https://www.google.co.kr/search?q={}&safe=strict&hl=ko&biw=944&bih=951&site=webhp&source=lnms&tbm=isch'.format(search)
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.19 (KHTML, like Gecko) Ubuntu/12.04 Chromium/18.0.1025.168 Chrome/18.0.1025.168 Safari/535.19'

    # FIXME: 한글키워드도 검색하고 싶은데 안되네요.
    # {"Content-Type":" application/x-www-form-urlencoded;charset=utf-8"}
    html = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': user_agent, "Content-Type":" application/x-www-form-urlencoded;charset=utf-8"}))
    htmltext = html.read()
    soup = BeautifulSoup(htmltext)

    img_urls = []
    formatted_images = []
    results = soup.findAll("a")
    
    for r in results:
        try:
            if "imgres?imgurl" in r['href']:
                img_urls.append(r['href'])
        except Exception as e:
            print('exception! @img_url.append():', str(e))
    
    for im in img_urls:
        refer_url = urllib.parse.urlparse(str(im))
        image_f = refer_url.query.split('&')[0].replace('imgurl=', '')
        formatted_images.append(image_f)
    
    return formatted_images


def make_thumbnail(path, width, height):
    # filepath, ext = os.path.splittext(path)
    filepath, ext = os.path.split(path)
    output_path = '{}\\thumb{}'.format(filepath, ext)

    if os.path.exists(output_path):
        return output_path

    im = Image.open(path)
    im.thumbnail((width, height, ), Image.ANTIALIAS)
    im.save(output_path)
    im.close()
    return output_path