# Generated by Django 3.2.6 on 2021-11-10 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_feature_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='email',
            field=models.EmailField(default='user@gmail.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='feature',
            name='due_date',
            field=models.DateField(),
        ),
    ]
