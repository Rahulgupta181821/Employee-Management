# Generated by Django 4.2.7 on 2024-02-14 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emp_app", "0003_alter_emp_working"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emp", name="phone", field=models.IntegerField(),
        ),
    ]
