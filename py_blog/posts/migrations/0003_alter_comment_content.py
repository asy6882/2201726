# Generated by Django 4.2.7 on 2023-12-17 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(default='', verbose_name='내용'),
        ),
    ]
