# Generated by Django 3.2.6 on 2021-11-06 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_feature_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='task',
            field=models.CharField(default=False, max_length=100000),
        ),
    ]