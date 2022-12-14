# Generated by Django 4.1.2 on 2022-10-13 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_issue_deleted_at_issue_is_deleted_alter_issue_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_at', models.DateField(verbose_name='Date of started')),
                ('finished_at', models.DateField(null=True, verbose_name='Date of finished')),
                ('title', models.CharField(max_length=50, verbose_name='Titile')),
                ('description', models.TextField(max_length=1000, null=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date of created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date of updates')),
                ('deleted_at', models.DateTimeField(default=None, null=True, verbose_name='Date of delete')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Delete')),
            ],
        ),
    ]
