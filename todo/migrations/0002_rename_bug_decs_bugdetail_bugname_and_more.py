# Generated by Django 4.0.3 on 2022-03-21 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bugdetail',
            old_name='bug_decs',
            new_name='bugname',
        ),
        migrations.AddField(
            model_name='bugdetail',
            name='decsription',
            field=models.CharField(max_length=100, null=True),
        ),
    ]