# Generated by Django 2.2.20 on 2021-06-21 19:26

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tickets", "0010_auto_20210617_2121"),
        ("msgs", "0148_next_attempt_index"),
    ]

    operations = [
        migrations.AddField(
            model_name="broadcast",
            name="ticket",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.PROTECT, related_name="broadcasts", to="tickets.Ticket"
            ),
        ),
        migrations.AlterField(
            model_name="broadcast",
            name="created_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="broadcast_creations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="broadcast",
            name="created_on",
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="broadcast",
            name="modified_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="broadcast_modifications",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="broadcast",
            name="modified_on",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]