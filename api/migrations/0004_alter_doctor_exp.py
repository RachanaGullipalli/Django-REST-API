# Generated by Django 4.1.1 on 2022-09-08 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_doctor_exp_alter_doctor_hosp_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='exp',
            field=models.TextField(max_length=200, null=True),
        ),
    ]