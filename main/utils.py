import random

from .models import Card


def pick_box():
    value = random.randint(0, 100)
    if value < 5:
        return ('back', 'middle', 'front')
    if value < 15:
        return ('middle', 'back', 'front')
    return ('front', 'middle', 'back')


def get_random_card():
    for box in pick_box():
        card_set = Card.objects.filter(box=box)
        if card_set.exists():
            break

    return card_set.order_by('?').first()


def get_box_counts():
    counts = {}
    for box_type in ['front', 'middle', 'back']:
        counts[box_type] = Card.objects.filter(box=box_type).count()

    return counts


def reposition_card(card, answer, callback):
    if card.definition.value == answer:
        callback("correct")
        if card.box == 'front':
            card.box = 'middle'
        elif card.box == 'middle':
            card.box = 'back'
    else:
        callback(f"wrong, the answer was \"{card.definition}\"")
        card.box = 'front'
    card.save()
