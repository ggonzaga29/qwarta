# Generated by Django 4.2.3 on 2023-07-25 02:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="admin",
            name="type",
        ),
        migrations.RemoveField(
            model_name="client",
            name="salary",
        ),
        migrations.RemoveField(
            model_name="client",
            name="type",
        ),
        migrations.AddField(
            model_name="admin",
            name="hire_date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="admin",
            name="salary",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="client",
            name="monthly_expenses",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="client",
            name="monthly_income",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="client",
            name="occupation",
            field=models.CharField(default="Unemployed", max_length=50),
        ),
        migrations.AddField(
            model_name="loan",
            name="is_approved",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="loan",
            name="issue_date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="loan",
            name="issued_by",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="core.admin"
            ),
        ),
        migrations.AddField(
            model_name="loan",
            name="product_name",
            field=models.CharField(default="Personal Loan", max_length=255),
        ),
        migrations.AddField(
            model_name="transactionreport",
            name="amount",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="loan",
            name="amount",
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name="CreditScore",
            fields=[
                ("score_id", models.AutoField(primary_key=True, serialize=False)),
                ("score", models.IntegerField()),
                ("date_updated", models.DateField()),
                ("remarks", models.TextField()),
                (
                    "client_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.client"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ClientDocument",
            fields=[
                ("document_id", models.AutoField(primary_key=True, serialize=False)),
                ("document_name", models.CharField(max_length=50)),
                ("document_type", models.CharField(max_length=50)),
                ("document_date", models.DateField()),
                (
                    "adminid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.admin"
                    ),
                ),
                (
                    "clientid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.client"
                    ),
                ),
                (
                    "loanid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.loan"
                    ),
                ),
            ],
        ),
    ]
