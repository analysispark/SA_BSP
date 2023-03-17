# Generated by Django 4.1.5 on 2023-03-17 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculate', '0006_student_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='park_test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match', models.CharField(max_length=10)),
                ('game', models.CharField(max_length=10)),
                ('team', models.CharField(max_length=20)),
                ('value', models.FloatField()),
            ],
        ),
    ]