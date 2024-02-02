from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Quote, Author, Tag  # Імпортуємо моделі Django


def main(request, page=1):
    quotes = Quote.objects.all().prefetch_related("tags")  # Використовуємо модель Quote замість db.quotes.find()

    per_page = 10
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.get_page(page)
    return render(request, "quotes/index.html", context={"quotes": quotes_on_page})


def details(request, author_id):
    author = Author.objects.get(pk=author_id)  # Використовуємо модель Author замість db.authors.find_one()
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(author.fullname)
    return render(request, "quotes/author_details.html", context={"author": author})


def author_list(request):
    authors = Author.objects.all()
    return render(request, "quotes/authors.html", context={"authors": authors})


def tag_list(request, tag):
    tag = Tag.objects.get(name=tag)
    quotes = Quote.objects.filter(tags=tag)

    return render(
        request, "quotes/quotes_by_tag.html", context={"quotes": quotes, "tag": tag}
    )
