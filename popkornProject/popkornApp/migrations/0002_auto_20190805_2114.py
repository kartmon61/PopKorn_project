# Generated by Django 2.2.1 on 2019-08-05 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('popkornApp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notice',
        ),
        migrations.RemoveField(
            model_name='postingcomment',
            name='posting',
        ),
        migrations.DeleteModel(
            name='Posting',
        ),
        migrations.DeleteModel(
            name='PostingComment',
        ),
    ]