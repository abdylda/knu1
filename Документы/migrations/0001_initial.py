# Generated by Django 3.2.7 on 2021-09-13 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название документ ')),
                ('document', models.FileField(max_length=60, upload_to='document/', verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Документы',
                'verbose_name_plural': 'Документы',
            },
        ),
    ]
