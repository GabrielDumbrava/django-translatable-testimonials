from django.views.generic import ListView, DetailView
from hvad.utils import get_translation_aware_manager
from .models import Event


class EvenimenteActive(ListView):
    model = Event
    manager = get_translation_aware_manager(Event)
    queryset = manager.get_query_set().filter(active=True)


class EvenimenteDetailsView(DetailView):
    #queryset = TipCurs.objects.all()
    manager = get_translation_aware_manager(Event)
    queryset = manager.get_query_set()


