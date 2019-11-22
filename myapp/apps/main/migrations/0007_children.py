# Generated by Django 2.1.5 on 2019-11-22 00:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_profile_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Children',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='Имя ребенка')),
                ('last_name', models.CharField(max_length=150, verbose_name='Фамилия ребенка')),
                ('father', models.CharField(max_length=150, verbose_name='Отчество ребенка')),
                ('bored', models.DateTimeField(verbose_name='Дата рождения')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]