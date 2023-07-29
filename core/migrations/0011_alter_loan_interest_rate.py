from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0010_user_user_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="loan",
            name="interest_rate",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
