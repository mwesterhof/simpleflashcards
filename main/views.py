import random

from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import FormView

from .forms import CardForm
from .models import Card


def pick_box():
    value = random.randint(0, 100)
    if value < 5:
        return ('back', 'middle', 'front')
    if value < 15:
        return ('middle', 'back', 'front')
    return ('front', 'middle', 'back')


class CardList(ListView):
    model = Card


class ShowCard(FormView):
    form_class = CardForm
    template_name = 'main/show_card.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['card'] = self.get_card()
        counts = {}
        for box_type in ['front', 'middle', 'back']:
            counts[box_type] = Card.objects.filter(box=box_type).count()

        context.update({
            'counts': counts,
            'sound_enabled': settings.PLAY_TERM_SOUND,
        })
        return context

    def get_card(self):
        for box in pick_box():
            card_set = Card.objects.filter(box=box)
            if card_set.exists():
                break

        return card_set.order_by('?').first()

    def form_valid(self, form):
        card = Card.objects.get(pk=form.cleaned_data['card_id'])
        answer = form.cleaned_data['answer']
        if card.definition.value == answer:
            if card.box == 'front':
                card.box = 'middle'
            elif card.box == 'middle':
                card.box = 'back'
        else:
            messages.warning(self.request, f"wrong, the answer was \"{card.definition}\"")
            card.box = 'front'
        card.save()
        return HttpResponseRedirect(reverse('random_card'))
