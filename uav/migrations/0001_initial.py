# Generated by Django 4.1.4 on 2022-12-17 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
        ),
        migrations.CreateModel(
            name='UAV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('weight', models.IntegerField(verbose_name='Weight')),
                ('color', models.CharField(choices=[('BU', 'Blue'), ('RD', 'Red'), ('GR', 'Green'), ('WT', 'White')], default='WT', max_length=12, verbose_name='Color')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uav.model')),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('founded_at', models.DateField(verbose_name='Founded At')),
                ('uav', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uav.uav')),
            ],
        ),
    ]
