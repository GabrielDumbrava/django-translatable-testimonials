from django.conf.urls import *
from .views import EvenimenteActive, EvenimenteDetailsView

urlpatterns = patterns('events.views',
                        url(r'^(?P<slug>[-\w]+)/$', EvenimenteDetailsView.as_view(), name='evenimente_details'),
                        url(r'^$', EvenimenteActive.as_view(), name='evenimente_active_list'),
)