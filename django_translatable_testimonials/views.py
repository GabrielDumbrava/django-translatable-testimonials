from django.views.generic import ListView
from hvad.utils import get_translation_aware_manager
from .models import Testimonial


class TestimonialsActiveList(ListView):
    model = Testimonial
    manager = get_translation_aware_manager(Testimonial)
    queryset = manager.get_query_set().filter(active=True)



