# Generated by Django 4.2.1 on 2023-06-06 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_poster_expl_img_poster_film'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Poster',
        ),
    ]
