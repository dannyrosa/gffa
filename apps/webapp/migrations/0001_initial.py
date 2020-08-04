# Generated by Django 3.0.8 on 2020-08-04 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=100)),
                ('birth_year', models.CharField(max_length=10, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('height', models.CharField(max_length=10, null=True)),
                ('mass', models.CharField(max_length=10, null=True)),
                ('eye_color', models.CharField(max_length=20, null=True)),
                ('hair_color', models.CharField(max_length=20, null=True)),
                ('skin_color', models.CharField(max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'People',
                'db_table': 'person',
                'ordering': ['name'],
                'managed': True,
            },
        ),
    ]