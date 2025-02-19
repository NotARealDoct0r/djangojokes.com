# Generated by Django 5.1.5 on 2025-02-19 19:29

import jobs.models
import private_storage.fields
import private_storage.storage.files
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_alter_applicant_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='resume',
            field=models.FileField(blank=True, help_text='PDFs only', storage=private_storage.fields.PrivateFileField(storage=private_storage.storage.files.PrivateFileSystemStorage(), upload_to=''), upload_to='resumes', validators=[jobs.models.validate_pdf]),
        ),
    ]
