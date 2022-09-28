# Generated by Django 4.1.1 on 2022-09-28 21:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('body', models.TextField()),
                ('leido', models.BooleanField(default=False)),
                ('emisor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='emisor', to=settings.AUTH_USER_MODEL)),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='receptor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['receptor'],
            },
        ),
    ]
