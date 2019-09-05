# Generated by Django 2.2.4 on 2019-09-05 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_accreditation_form_allow_blank_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accreditation',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='accreditation',
            name='uc_username',
            field=models.CharField(max_length=50, unique=True, verbose_name='Ultimate Central username'),
        ),
        migrations.AlterField(
            model_name='accreditation',
            name='wfdf_userid',
            field=models.IntegerField(blank=True, unique=True, verbose_name='WFDF user ID'),
        ),
    ]