# Generated by Django 5.0.4 on 2024-05-06 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('react_panel', '0002_category_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='content',
        ),
    ]