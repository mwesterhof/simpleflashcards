from django.db import models
from django.utils.translation import gettext_lazy as _


BOXES = [
    ('front', _("Front")),
    ('middle', _("Middle")),
    ('back', _("Back")),
]


class Card(models.Model):
    term = models.CharField(unique=True, max_length=200)
    definition = models.TextField()

    box = models.CharField(
        choices=BOXES,
        default=BOXES[0][0],
        max_length=max([len(code) for code, _ in BOXES])
    )

    def __str__(self):
        return self.term
