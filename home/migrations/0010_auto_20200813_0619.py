# Generated by Django 3.0.8 on 2020-08-13 06:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('home', '0009_auto_20200813_0618'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ThemesPage',
            new_name='ThemeListingPage',
        ),
        migrations.AlterModelOptions(
            name='themelistingpage',
            options={'verbose_name': 'theme_listing_page'},
        ),
    ]
