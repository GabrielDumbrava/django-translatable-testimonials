from .models import Curs, TipCurs
from django.contrib import admin
from unidecode import unidecode
from django.utils.text import slugify
from cms.admin.placeholderadmin import PlaceholderAdmin
from hvad.admin import TranslatableAdmin


class TipCursAdmin(TranslatableAdmin, PlaceholderAdmin):
    list_display = ('__unicode__', )
    list_display_links = ('__unicode__', )

    def __init__(self, *args, **kwargs):
            super(TipCursAdmin, self).__init__(*args, **kwargs)
            self.prepopulated_fields = {'slug': ('titlu',)}

    # def save_model(self, request, obj, form, change):
    #     obj.slug = slugify(u'%s' % unidecode(obj.titlu))
    #     obj.save()


class CursAdmin(TranslatableAdmin, PlaceholderAdmin):
    list_display = ('active', '__unicode__', 'data_start', 'all_translations')
    list_editable = ('active', )
    list_display_links = ('__unicode__',)
    #list_display_links = ('data_start',)

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(u'%s' % unidecode(obj.denumire))
        obj.save()

admin.site.register(Curs, CursAdmin)
admin.site.register(TipCurs, TipCursAdmin)
