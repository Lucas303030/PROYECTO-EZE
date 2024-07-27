# Generated by Django 3.2.6 on 2024-07-25 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackitems', '0005_alter_tracking_estado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracking',
            old_name='ubicacion',
            new_name='destino',
        ),
        migrations.AddField(
            model_name='tracking',
            name='origen',
            field=models.CharField(default='AR', max_length=255),
            preserve_default=False,
        ),
    ]
