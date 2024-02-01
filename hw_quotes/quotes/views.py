from bson import ObjectId
from django.core.paginator import Paginator
from django.shortcuts import render

from .utils import db


def main(request, page=1):
    quotes = db.quotes.find()

    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.get_page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


def details(request, author):
    author = db.authors.find_one({'_id': ObjectId(author)})

    return render(request, 'quotes/author_details.html', context={'author': author})


def author_list(request):
    authors = db.authors.find()
    return render(request, 'quotes/authors.html', context={'authors': authors})


def tag_list(request, tag):
    quotes = list(db.quotes.find({'tags': tag}))

    return render(request, 'quotes/quotes_by_tag.html', context={'quotes': quotes, 'tag': tag})
