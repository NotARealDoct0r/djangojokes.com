# Generated by Django 5.1.5 on 2025-02-09 05:33

import django.core.validators
import django.db.models.deletion
import jobs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField()),
                ('last_name', models.CharField()),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField(validators=[django.core.validators.URLValidator(schemes=['http', 'https'])])),
                ('employment_type', models.CharField(choices=[(None, '--Please choose--'), ('ft', 'Full-time'), ('pt', 'Part-time'), ('contract', 'Contract work')])),
                ('start_date', models.DateField(error_messages={'past_date': 'Please enter a future date.'}, help_text='The earliest date you can start working.', validators=[jobs.models.validate_future_date])),
                ('available_days', models.CharField(choices=[(1, 'MON'), (2, 'TUE'), (3, 'WED'), (4, 'THU'), (5, 'FRI')], help_text='Select all days that you can work.')),
                ('desired_hourly_wage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cover_letter', models.TextField()),
                ('confirmation', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jobs.applicant')),
            ],
        ),
    ]
