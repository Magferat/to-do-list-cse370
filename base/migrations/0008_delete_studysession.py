# Generated by Django 4.2.7 on 2023-12-12 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_note_studysession_timer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudySession',
        ),
    ]
