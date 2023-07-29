# Generated by Django 4.2.3 on 2023-07-29 14:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Loan",
            fields=[
                ("loan_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "product_name",
                    models.CharField(default="Personal Loan", max_length=255),
                ),
                ("amount", models.IntegerField(default=0)),
                (
                    "interest_rate",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                ("amount_to_pay", models.IntegerField(default=0)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("loan_length", models.IntegerField(default=0)),
                ("issue_date", models.DateField(null=True)),
                ("status", models.CharField(default="Pending", max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("user_id", models.AutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=50)),
                ("password", models.CharField(max_length=50)),
                ("email", models.CharField(max_length=50)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=100)),
                ("mobile_number", models.CharField(max_length=12)),
                ("user_type", models.CharField(default="client", max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Admin",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.user",
                    ),
                ),
                ("salary", models.IntegerField(default=0)),
                ("hire_date", models.DateField(default=django.utils.timezone.now)),
            ],
            bases=("core.user",),
        ),
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.user",
                    ),
                ),
                ("occupation", models.CharField(default="Unemployed", max_length=50)),
                (
                    "monthly_income",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "net_worth",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
            ],
            bases=("core.user",),
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                ("payment_id", models.AutoField(primary_key=True, serialize=False)),
                ("amount", models.IntegerField(default=0)),
                ("due_date", models.DateField(default=django.utils.timezone.now)),
                ("date_paid", models.DateField(null=True)),
                ("is_late", models.BooleanField(default=False)),
                ("status", models.CharField(default="Pending", max_length=50)),
                (
                    "loan_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.loan",
                    ),
                ),
                (
                    "client_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.client",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="loan",
            name="approved_by",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.admin",
            ),
        ),
        migrations.AddField(
            model_name="loan",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="core.client"
            ),
        ),
        migrations.CreateModel(
            name="CreditScore",
            fields=[
                (
                    "credit_score_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
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
    ]
