# Generated by Django 4.0.2 on 2022-02-08 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='Blank', max_length=50)),
                ('lname', models.CharField(default='Blank', max_length=50)),
                ('id_number', models.IntegerField(default=0)),
                ('email', models.CharField(default='Blank', max_length=50)),
            ],
        ),
    ]
