# Generated by Django 3.1.4 on 2022-03-19 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_auto_20220319_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='rno',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subject1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subject2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subject3',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
