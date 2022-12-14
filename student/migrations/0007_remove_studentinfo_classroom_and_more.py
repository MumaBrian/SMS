# Generated by Django 4.1.3 on 2022-11-16 01:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('classinfo', '0001_initial'),
        ('student', '0006_alter_studentinfo_admission_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinfo',
            name='classroom',
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='current_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='classinfo.classinfo'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='DoB',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='admission_id',
            field=models.CharField(max_length=7, unique=True),
        ),
    ]
