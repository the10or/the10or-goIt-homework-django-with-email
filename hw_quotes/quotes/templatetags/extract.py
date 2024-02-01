from django import template

from ..utils import db

register = template.Library()


@register.filter('author')
def get_author(id_):
    author = db.authors.find_one({'_id': id_})
    if not author:
        return None
    return author['fullname']


register.filter('author', get_author)
