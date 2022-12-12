# Generated by Django 4.1.4 on 2022-12-10 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=60)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('mobile', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('submitted_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Batches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fees', models.IntegerField()),
                ('batch', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('batches_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admissionapi.user')),
            ],
            options={
                'db_table': 'batches',
            },
        ),
    ]
