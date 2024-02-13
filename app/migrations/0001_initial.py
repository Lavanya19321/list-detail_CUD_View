# Generated by Django 4.2.6 on 2024-02-10 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=20)),
                ('sprincipal', models.CharField(max_length=20)),
                ('sloc', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stname', models.CharField(max_length=20)),
                ('st_age', models.IntegerField()),
                ('sname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='School', to='app.school')),
            ],
        ),
    ]