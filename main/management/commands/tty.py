from django.core.management.base import BaseCommand, CommandError

from main.models import Card
from main.utils import get_box_counts, get_random_card, reposition_card


class Command(BaseCommand):
    def _print_boxes(self):
        counts = get_box_counts()
        self.stdout.write(f"f: {counts['front']} m: {counts['middle']} b: {counts['back']}")

    def handle(self, *args, **options):
        def _callback(message):
            self.stdout.write(message)

        while True:
            self._print_boxes()
            card = get_random_card()
            answer = input(f"\"{card.term}\": ")
            reposition_card(card, answer, _callback)
