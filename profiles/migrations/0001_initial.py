# Generated by Django 3.1.2 on 2020-11-20 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
                ('address_line_1', models.CharField(max_length=254)),
                ('address_line_2', models.CharField(max_length=254)),
                ('town_or_city', models.CharField(max_length=254)),
                ('county_province', models.CharField(max_length=254)),
                ('country', django_countries.fields.CountryField(max_length=256)),
                ('post_code_zip_code', models.CharField(max_length=254)),
                ('phone_number', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('primary_address', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
