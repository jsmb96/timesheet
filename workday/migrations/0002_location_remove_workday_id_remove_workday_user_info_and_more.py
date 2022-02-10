# Generated by Django 4.0.2 on 2022-02-09 19:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_delete_profiles'),
        ('workday', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='workday',
            name='id',
        ),
        migrations.RemoveField(
            model_name='workday',
            name='user_info',
        ),
        migrations.AddField(
            model_name='workday',
            name='AMCO_payroll',
            field=models.CharField(default='$', max_length=5),
        ),
        migrations.AddField(
            model_name='workday',
            name='FBP_payroll',
            field=models.CharField(default='$', max_length=5),
        ),
        migrations.AddField(
            model_name='workday',
            name='file_number',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='workday',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
        migrations.AddField(
            model_name='workday',
            name='sector',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='workday',
            name='time_in',
            field=models.DateTimeField(default=datetime.date.today, null=True),
        ),
        migrations.AddField(
            model_name='workday',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='workday.location'),
        ),
    ]
