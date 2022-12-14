# Generated by Django 4.1.2 on 2022-10-06 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Status', 'verbose_name_plural': 'Statuses'},
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.ForeignKey(default='new', on_delete=django.db.models.deletion.RESTRICT, related_name='issue', to='webapp.status', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='type',
            field=models.ForeignKey(default='task', on_delete=django.db.models.deletion.RESTRICT, related_name='issue', to='webapp.type', verbose_name='Type'),
        ),
    ]
