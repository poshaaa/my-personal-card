# Generated by Django 4.1 on 2022-08-25 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='description',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='skills.skills'),
        ),
    ]
