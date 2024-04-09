# Generated by Django 5.0.4 on 2024-04-09 13:53

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(max_length=128)),
                ('mpaa_rating', models.CharField(max_length=32)),
                ('budget', models.IntegerField()),
                ('gross', models.IntegerField()),
                ('release_date', models.DateField()),
                ('genre', models.CharField(max_length=64)),
                ('runtime', models.IntegerField()),
                ('rating', models.DecimalField(decimal_places=2, max_digits=6)),
                ('rating_count', models.IntegerField()),
                ('summary', models.CharField(max_length=1024)),
            ],
        ),
    ]
