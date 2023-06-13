# Generated by Django 4.2.1 on 2023-06-13 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Correlacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code1', models.CharField(max_length=255)),
                ('code2', models.CharField(max_length=255)),
                ('correlacao', models.FloatField()),
                ('delay', models.IntegerField()),
            ],
        ),
    ]
