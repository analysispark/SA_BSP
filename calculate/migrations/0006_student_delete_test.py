# Generated by Django 4.1.5 on 2023-03-17 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculate', '0005_auto_20230118_2115'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match', models.CharField(max_length=255, null=True)),
                ('game', models.CharField(max_length=10, null=True)),
                ('team', models.CharField(max_length=150, null=True)),
                ('ame', models.CharField(max_length=150, null=True)),
                ('score_total', models.CharField(default='', max_length=10, null=True)),
                ('game_time', models.DateTimeField(null=True)),
                ('kpi_2p', models.FloatField(null=True)),
                ('kpi_2pA', models.FloatField(null=True)),
                ('kpi_2pp', models.FloatField(null=True)),
                ('kpi_3p', models.FloatField(null=True)),
                ('kpi_3pA', models.FloatField(null=True)),
                ('kpi_3pp', models.FloatField(null=True)),
                ('kpi_FGp', models.FloatField(null=True)),
                ('kpi_FT', models.FloatField(null=True)),
                ('kpi_FTA', models.FloatField(null=True)),
                ('kpi_FTp', models.FloatField(null=True)),
                ('kpi_REB_OR', models.FloatField(null=True)),
                ('kpi_REB_DF', models.FloatField(null=True)),
                ('kpi_REB_TOT', models.FloatField(null=True)),
                ('kpi_AS', models.FloatField(null=True)),
                ('kpi_ST', models.FloatField(null=True)),
                ('kpi_GD', models.FloatField(null=True)),
                ('kpi_BS', models.FloatField(null=True)),
                ('kpi_PF_w', models.FloatField(null=True)),
                ('kpi_PF_wo', models.FloatField(null=True)),
                ('kpi_PF_TOT', models.FloatField(null=True)),
                ('kpi_TO', models.FloatField(null=True)),
                ('kpi_TF', models.FloatField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='TEST',
        ),
    ]
