from django.db import models
from django.core.urlresolvers import reverse


class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.slug

#QuerySet is use to filter everything that has been published.
class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

#These are my blog entry models, using the fields and a slug which is a user freindly
#ref, next is our boolean var using this we find out if our article can be pubished or not.
#I set the default value to true so that i dont have to fill it everytime.
#i also used a DateTime field so that django can keep track of all the entry.
#for modified i also use auto _now to keep track of when anything was modified.
class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)


    objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.title
        #def str and returns self.title
#set object to QuerySet.as_manager, the QuerySet gets automaicly converted into its manger form.
    def get_absolute_url(self):
        return reverse("entry_detail", kwargs={"slug": self.slug})
#using a verbose_name allows it to look better on the enterface.
#also adding ordering so that each entry is shown in order.
    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]
