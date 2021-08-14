# Generated by Django 3.1.13 on 2021-08-12 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('folders', '0001_initial'),
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='parent_folder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='folders.folder'),
        ),
    ]