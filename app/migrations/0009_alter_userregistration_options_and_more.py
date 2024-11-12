# Generated by Django 5.0.1 on 2024-02-13 13:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_userregistration_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userregistration',
            options={},
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterModelTable(
            name='userregistration',
            table=None,
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('pincode', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]