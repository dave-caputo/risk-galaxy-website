import hashlib
import os

from django import template
from django.conf import settings


register = template.Library()


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


@register.simple_tag()
def staticv(static_url):
    fpath = os.path.join(settings.BASE_DIR, static_url)
    return md5(fpath)
