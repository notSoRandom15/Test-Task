# Generated by Django 4.2.4 on 2023-09-29 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0010_remove_book_isreccomended_remove_book_url_book_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='uploaded_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6),
        ),
    ]
