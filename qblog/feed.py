from django.contrib.syndication.views import Feed
from .models import Entry


class LatestPostsFeed(Feed):
    title = "Q Blog"
    description = "Latest Posts of Q"
    link = "/feed/"


    def items(self):
        return Entry.objects.published()[:5]

    def item_link(self, item):
        return reverse ('feed', args=[item.pk])

    def item.title(self, item):
        return item.title

    def item_description(self, item):
        return item.description
