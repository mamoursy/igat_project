# Generated by Django 2.2.1 on 2019-06-13 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=200)),
                ('Organisme', models.CharField(max_length=300)),
                ('TEL', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=20)),
                ('Adresse_Postale', models.CharField(max_length=200)),
                ('Ville', models.CharField(max_length=200)),
            ],
        ),
    ]
