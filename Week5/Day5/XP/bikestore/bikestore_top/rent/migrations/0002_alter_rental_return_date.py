# Generated by Django 4.2.1 on 2023-06-02 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='return_date',
            field=models.DateTimeField(null=True),
        ),
    ]