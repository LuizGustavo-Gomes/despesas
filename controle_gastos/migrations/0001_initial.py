# Generated by Django 5.1 on 2024-08-23 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='despesas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('valor', models.CharField(max_length=20)),
                ('categoria', models.CharField(max_length=200)),
            ],
        ),
    ]
