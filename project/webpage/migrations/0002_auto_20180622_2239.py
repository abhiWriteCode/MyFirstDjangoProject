# Generated by Django 2.0.6 on 2018-06-22 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='put_date',
            new_name='pub_date',
        ),
    ]
