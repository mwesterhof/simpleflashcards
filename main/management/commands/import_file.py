from django.core.management.base import BaseCommand, CommandError

from main.models import Card


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file')

    def handle(self, *args, **options):
        with open(options['file']) as inf:
            lines = [line.strip().split(' - ') for line in inf.readlines() if ' - ' in line]

        Card.objects.all().delete()
        for one, other in lines:
            Card.objects.create(term=one, definition=other)
            Card.objects.create(term=other, definition=one)
