# Generated by Django 4.2.3 on 2023-07-28 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_alter_client_monthly_income_alter_client_net_worth"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="payment",
            name="due_date",
        ),
        migrations.CreateModel(
            name="ExpectedPayment",
            fields=[
                (
                    "expected_payment_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("amount", models.IntegerField()),
                ("due_date", models.DateField()),
                (
                    "loan_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.loan"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="payment",
            name="expected_payment_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.expectedpayment",
            ),
        ),
    ]
