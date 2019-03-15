from django.conf import settings

from bs4 import BeautifulSoup


def get_flickr_api_url(query):
    url = f'{settings.FLICKR_API}/?api_key={settings.FLICKR_API_KEY}&method={settings.FLICKR_METHOD}&text={query}'
    return url


def get_image_urls(data):
    urls = []

    soup = BeautifulSoup(data, features='xml')
    photo_tags = soup.find_all('photo')

    for photo_tag in photo_tags:
        url = build_url(farm_id=photo_tag['farm'],
                        server_id=photo_tag['server'],
                        photo_id=photo_tag['id'],
                        secret=photo_tag['secret'])
        urls.append(url)

    return urls


def build_url(farm_id, server_id, photo_id, secret):
    return f'https://farm{farm_id}.staticflickr.com/{server_id}/{photo_id}_{secret}.jpg'
