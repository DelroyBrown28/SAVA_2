# Generated by Django 3.1.7 on 2021-03-19 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SAVAsite', '0004_auto_20210319_1324'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContentManagementService',
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Content Management Items', 'verbose_name_plural': 'Content Management'},
        ),
        migrations.RemoveField(
            model_name='question',
            name='priority',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='title',
        ),
        migrations.AddField(
            model_name='question',
            name='content_management_service_1',
            field=models.CharField(default='Service Item', max_length=150),
        ),
        migrations.AddField(
            model_name='question',
            name='content_management_service_10',
            field=models.CharField(default='Service Item', max_length=150),
        ),
        migrations.AddField(
            model_name='question',
            name='content_management_service_2',
            field=models.CharField(default='Service Item', max_length=150),
        ),
        migrations.AddField(
            model_name='question',
            name='content_management_service_3',
            field=models.CharField(default='Service Item', max_length=150),
        ),
        migrations.AddField(
            model_name='question',
            name='content_management_service_4',
            field=models.CharField(default='Service Item', max_length=150),
        ),
        migrations.AddField(
            model_name='question',
            name='content_management_service_5',
            field=models.CharField(default='Service Item', max_length=150),
        ),
        migrations.AddField(
            model_name='question',
            name='content_management_service_6',
            field=models.CharField(default='Service Item', max_length=150),
        ),
        migrations.AddField(
            model_name='question',
            name='content_management_service_7',
            field=models.CharField(default='Service Item', max_length=150),
        ),
        migrations.AddField(
            model_name='question',
            name='content_management_service_8',
            field=models.CharField(default='Service Item', max_length=150),
        ),
        migrations.AddField(
            model_name='question',
            name='content_management_service_9',
            field=models.CharField(default='Service Item', max_length=150),
        ),
    ]
