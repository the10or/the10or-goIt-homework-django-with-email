import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw_quotes.settings")
django.setup()

from quotes.models import Quote, Author, Tag  # noqa

from quotes.utils import db  # noqa

authors = db.authors.find()

for author in authors:
    Author.objects.get_or_create(
        fullname=author["fullname"],
        born_date=author["born_date"],
        born_location=author["born_location"],
        description=author["description"],
    )

quotes = db.quotes.find()

for quote in quotes:
    tags = []
    for tag in quote["tags"]:
        tags.append(Tag.objects.get_or_create(name=tag)[0])

    exist_quote = bool(len(Quote.objects.filter(text=quote["quote"])))

    if not exist_quote:
        print(quote["_id"])
        author = db.authors.find_one({"_id": quote["author"]})

        a = Author.objects.get(fullname=author["fullname"])
        q = Quote.objects.create(text=quote["quote"], author=a)

        for tag in tags:
            q.tags.add(tag)
