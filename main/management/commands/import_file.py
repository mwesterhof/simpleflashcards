from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from main.models import Card, Word


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file')

    def _create_word(self, value, language):
        try:
            word = Word.objects.get(value=value, language=language)
        except Word.DoesNotExist:
            word = Word()
            word.value = value
            word.language = language
            word.save(generate_audio=settings.PLAY_TERM_SOUND)

        return word

    def _create_card(self, term, definition):
        card = Card()
        card.term = term
        card.definition = definition
        card.save()
        return card

    def handle(self, *args, **options):
        with open(options['file']) as inf:
            lines = [line.strip().split(' - ') for line in inf.readlines() if ' - ' in line]

        with open(options['file']) as inf:
            language_codes = [code.strip() for code in inf.readlines()[0].strip('\n').split('/')]
        one_language, other_language = language_codes

        Card.objects.all().delete()
        Word.objects.all().delete()

        for one, other in lines:
            if not one or not other:
                continue

            one = self._create_word(one, one_language)
            other = self._create_word(other, other_language)

            self._create_card(term=one, definition=other)
            self._create_card(term=other, definition=one)
