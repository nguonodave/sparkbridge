# Generated by Django 3.1.14 on 2024-09-10 17:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('price_hr', models.DecimalField(decimal_places=2, max_digits=100)),
                ('date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
