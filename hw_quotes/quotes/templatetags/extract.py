from bson import ObjectId
from django import template
from ..models import Author

register = template.Library()

@register.filter
def author(id_):
    try:
        author = Author.objects.get(pk=ObjectId(id_))
        return author.fullname
    except (Author.DoesNotExist, ValueError, TypeError):
        return None

