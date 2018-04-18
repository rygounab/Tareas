# Generated by Django 2.0.4 on 2018-04-17 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age_old', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('rut', models.CharField(max_length=30)),
                ('nickname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('age_old', models.IntegerField()),
                ('rut', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('photo', models.ImageField(upload_to='photos')),
                ('positionGame', models.CharField(choices=[('BA', 'Base'), ('EC', 'Escolta'), ('AL', 'Alero'), ('AP', 'Ala_Pivot'), ('PV', 'Pivot')], default='BA', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='photos')),
                ('code', models.CharField(max_length=200)),
            ],
        ),
    ]
