# Generated by Django 4.1.3 on 2022-11-22 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sbdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(max_length=50)),
                ('address', models.TextField(max_length=255)),
            ],
            options={
                'db_table': 'SB_Table',
            },
        ),
    ]
