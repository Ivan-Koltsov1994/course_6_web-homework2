# Generated by Django 4.2.1 on 2023-06-07 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('name', 'slug', '-created_at'), 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]
