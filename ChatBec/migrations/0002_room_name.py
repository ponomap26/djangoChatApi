# Generated by Django 4.2.1 on 2023-05-25 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChatBec', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]