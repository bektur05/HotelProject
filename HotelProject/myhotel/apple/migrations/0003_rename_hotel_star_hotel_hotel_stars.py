# Generated by Django 5.1.6 on 2025-02-17 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apple', '0002_alter_review_stars_alter_userprofile_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='hotel_star',
            new_name='hotel_stars',
        ),
    ]
