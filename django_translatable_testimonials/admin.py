from django.contrib import admin
from unidecode import unidecode
from django.utils.text import slugify
from parler.admin import TranslatableAdmin

from .models import Testimonial


class TestimonialAdmin(TranslatableAdmin):
    list_display = ('__unicode__', 'active')
    list_display_links = ('__unicode__', )

    def save_model(self, request, obj, form, change):
        # the default Django slugify algorithm fails with diacritics
        obj.slug = slugify(u'%s' % unidecode(obj.name))
        obj.save()


admin.site.register(Testimonial, TestimonialAdmin)
