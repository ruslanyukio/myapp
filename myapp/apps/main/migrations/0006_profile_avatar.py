# Generated by Django 2.1.5 on 2019-11-21 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20191122_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default.png', upload_to='users_avatar', verbose_name='Аватарка'),
        ),
    ]
