# Generated by Django 4.2.1 on 2023-06-09 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=200, unique=True)),
                ('definition', models.TextField()),
                ('box', models.CharField(choices=[('front', 'Front'), ('middle', 'Middle'), ('back', 'Back')], default='front', max_length=6)),
            ],
        ),
    ]
