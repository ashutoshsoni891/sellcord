# Generated by Django 5.0.4 on 2024-05-13 17:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("amazon", "0003_basemodel_remove_customer_created_at_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="return",
            name="basemodel_ptr",
        ),
        migrations.RemoveField(
            model_name="dispute",
            name="basemodel_ptr",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="basemodel_ptr",
        ),
        migrations.RemoveField(
            model_name="order",
            name="basemodel_ptr",
        ),
        migrations.AddField(
            model_name="customer",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="customer",
            name="customer_id",
            field=models.AutoField(
                default=django.utils.timezone.now, primary_key=True, serialize=False
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="customer",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="dispute",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="dispute",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="order",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="return",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="return",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.DeleteModel(
            name="BaseModel",
        ),
    ]
