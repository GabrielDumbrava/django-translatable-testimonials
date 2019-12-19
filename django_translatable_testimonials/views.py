from django.views.generic import ListView
# from hvad.utils import get_translation_aware_manager
from parler.views import TranslatableSlugMixin

from .models import Testimonial


class TestimonialsActiveList(TranslatableSlugMixin, ListView):
    model = Testimonial
    # manager = get_translation_aware_manager(Testimonial)
    queryset = Testimonial.objects.get_queryset().filter(active=True)



