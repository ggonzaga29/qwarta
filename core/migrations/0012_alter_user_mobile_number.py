# Generated by Django 4.2.3 on 2023-07-30 02:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0011_alter_loan_interest_rate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="mobile_number",
            field=models.CharField(max_length=21),
        ),
    ]