# Generated by Django 2.2.1 on 2019-07-28 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20190728_1116'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='people',
            unique_together={('designation', 'name')},
        ),
    ]
