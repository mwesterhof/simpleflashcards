from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import FormView

from .forms import CardForm
from .models import Card
from .utils import get_box_counts, get_random_card, reposition_card


class CardList(ListView):
    model = Card


class ShowCard(FormView):
    form_class = CardForm
    template_name = 'main/show_card.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['card'] = get_random_card()
        counts = get_box_counts()

        context.update({
            'counts': counts,
            'sound_enabled': settings.PLAY_TERM_SOUND,
        })
        return context

    def form_valid(self, form):
        card = Card.objects.get(pk=form.cleaned_data['card_id'])
        answer = form.cleaned_data['answer']

        def _callback(message):
            messages.warning(self.request, message)

        reposition_card(card, answer, _callback)

        return HttpResponseRedirect(reverse('random_card'))
