# Generated by Django 5.0.4 on 2024-05-06 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('react_panel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
