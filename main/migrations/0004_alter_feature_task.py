# Generated by Django 3.2.6 on 2021-11-06 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_feature_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='task',
            field=models.CharField(max_length=100000),
        ),
    ]
