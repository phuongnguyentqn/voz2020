# Generated by Django 2.2.4 on 2019-09-05 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190905_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='box',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='forums', to='api.Box'),
        ),
    ]
