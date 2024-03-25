from tempfile import TemporaryFile

from gtts import gTTS

from django.core.files.base import File
from django.db import models
from django.utils.translation import gettext_lazy as _


BOXES = [
    ('front', _("Front")),
    ('middle', _("Middle")),
    ('back', _("Back")),
]


def audio_upload_path(instance, filename):
    language_code = instance.language

    return f'audio/{language_code}/{filename}'


class Word(models.Model):
    value = models.CharField(unique=True, max_length=200)
    language = models.CharField(max_length=5)
    audio = models.FileField(blank=True, upload_to=audio_upload_path)

    @property
    def audio_cleaned(self):
        return self.audio.url.replace('/audio/', '/')

    def save(self, *args, **kwargs):
        if 'generate_audio' in kwargs:
            generate_audio = kwargs.pop('generate_audio')
            if generate_audio:
                f = TemporaryFile()
                gTTS(self.value, lang=self.language).write_to_fp(f)
                self.audio.save(f'{self.pk}.mp3', File(f))
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.value


class Card(models.Model):
    term = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='+')
    definition = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='+')

    box = models.CharField(
        choices=BOXES,
        default=BOXES[0][0],
        max_length=max([len(code) for code, _ in BOXES])
    )

    def __str__(self):
        return str(self.term)
