# Generated by Django 4.2.11 on 2024-05-08 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socios',
            name='arq_autoDeclaracao',
            field=models.FileField(upload_to='declaracoes', verbose_name='Auto Declaração'),
        ),
    ]