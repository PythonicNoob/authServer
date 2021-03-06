# Generated by Django 3.2.5 on 2021-08-04 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licensekeys', '0004_alter_licensekey_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licensekey',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='licensekey',
            name='last_activity',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
