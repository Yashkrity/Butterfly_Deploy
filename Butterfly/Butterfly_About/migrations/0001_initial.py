# Generated by Django 2.2b1 on 2019-03-08 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_b', models.TextField(max_length=8000)),
                ('active_from', models.CharField(max_length=200)),
            ],
        ),
    ]