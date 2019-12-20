# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from filebrowser.fields import FileBrowseField
from cms.models.fields import PlaceholderField
from parler.models import TranslatableModel, TranslatedFields


class string_with_title(str):
    # http://blog.ionelmc.ro/2011/06/24/custom-app-names-in-the-django-admin/
    def __new__(cls, value, title):
        instance = str.__new__(cls, value)
        instance._title = title
        return instance

    def title(self):
        return self._title

    __copy__ = lambda self: self
    __deepcopy__ = lambda self, memodict: self


class Testimonial(TranslatableModel):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(help_text=_("Updates itself on name change."), blank=True)
    org = models.TextField(blank=True, verbose_name=_('Organization'))

    translations = TranslatedFields(
        title=models.CharField(max_length=250, blank=True),
        quote=models.TextField()
    )

    def __str__(self):
        return self.name

    class Meta:
        app_label = string_with_title("django_translatable_testimonials", _("Testimonials"))