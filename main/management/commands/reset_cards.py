from django.core.management.base import BaseCommand

from main.models import Card


class Command(BaseCommand):
    def handle(self, *args, **options):
        Card.objects.update(box='front')
