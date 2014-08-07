from django.conf.urls import *

from .views import TestimonialsActiveList

urlpatterns = patterns('events.views',
                        url(r'^$', TestimonialsActiveList.as_view(), name='testimonials_active_list'),
)