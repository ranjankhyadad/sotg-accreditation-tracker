# Generated by Django 2.2.4 on 2019-09-18 03:42

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_accreditation_date_wfdf_userid_no_blank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accreditation',
            name='date',
            field=models.DateField(help_text='Enter date as in the certificate', validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date(2019, 9, 18), message='Please enter valid accreditation date')], verbose_name='Accreditation Date'),
        ),
        migrations.AlterField(
            model_name='accreditation',
            name='wfdf_userid',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(limit_value=0, message='Please enter valid ID')], verbose_name='WFDF user ID'),
        ),
    ]