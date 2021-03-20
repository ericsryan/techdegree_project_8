# Generated by Django 3.1.7 on 2021-03-19 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('caption', models.CharField(max_length=300)),
                ('category', models.CharField(blank=True, max_length=300, null=True)),
                ('group', models.CharField(blank=True, max_length=300, null=True)),
                ('formula', models.CharField(blank=True, max_length=300, null=True)),
                ('strunz_classification', models.CharField(blank=True, max_length=300, null=True)),
                ('crystal_system', models.CharField(blank=True, max_length=300, null=True)),
                ('mohs_scale_hardness', models.CharField(blank=True, max_length=300, null=True)),
                ('luster', models.CharField(blank=True, max_length=300, null=True)),
                ('color', models.CharField(blank=True, max_length=300, null=True)),
                ('specific_gravity', models.CharField(blank=True, max_length=300, null=True)),
                ('cleavage', models.CharField(blank=True, max_length=300, null=True)),
                ('diaphaneity', models.CharField(blank=True, max_length=300, null=True)),
                ('crystal_habit', models.CharField(blank=True, max_length=300, null=True)),
                ('streak', models.CharField(blank=True, max_length=300, null=True)),
                ('optical_properties', models.CharField(blank=True, max_length=300, null=True)),
                ('refractive_index', models.CharField(blank=True, max_length=300, null=True)),
                ('unit_cell', models.CharField(blank=True, max_length=300, null=True)),
                ('crystal_symmetry', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
