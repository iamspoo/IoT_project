# Generated by Django 2.2.3 on 2020-11-09 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='area',
            fields=[
                ('areacode', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='light',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=1)),
                ('mode', models.CharField(max_length=1)),
                ('areafk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='light.area')),
            ],
        ),
    ]