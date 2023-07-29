# Generated by Django 4.2.3 on 2023-07-28 16:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_alter_user_mobile_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="payment",
            name="loan_id",
        ),
        migrations.RemoveField(
            model_name="payment",
            name="status",
        ),
        migrations.AddField(
            model_name="expectedpayment",
            name="status",
            field=models.CharField(default="Pending", max_length=50),
        ),
    ]
