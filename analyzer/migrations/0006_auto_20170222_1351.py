# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0005_auto_20170222_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='query',
            field=models.CharField(choices=[(b'cell_count', b'number of cells'), (b'error_count', b'error count'), (b'finished_normally', b'finished normally'), (b'gas_in_place', b'gas-in-place'), (b'oil_in_place', b'oil-in-place'), (b'processor_count', b'number of processors'), (b'run_time', b'running time'), (b'show_plot_pressure', b'show plot pressure'), (b'show_plot_oil_production', b'show plot oil production'), (b'show_plot_gas_production', b'show plot gas production'), (b'show_plot_water_production', b'show plot water production'), (b'show_plot_water_cut', b'show plot water cut'), (b'show_plot_gas_oil_ratio', b'show plot gas oil ratio'), (b'simulation_time', b'simulation duration'), (b'warning_count', b'warning count'), (b'water_in_place', b'water-in-place')], max_length=200),
        ),
        migrations.AlterField(
            model_name='supportedquery',
            name='query',
            field=models.CharField(choices=[(b'cell_count', b'number of cells'), (b'error_count', b'error count'), (b'finished_normally', b'finished normally'), (b'gas_in_place', b'gas-in-place'), (b'oil_in_place', b'oil-in-place'), (b'processor_count', b'number of processors'), (b'run_time', b'running time'), (b'show_plot_pressure', b'show plot pressure'), (b'show_plot_oil_production', b'show plot oil production'), (b'show_plot_gas_production', b'show plot gas production'), (b'show_plot_water_production', b'show plot water production'), (b'show_plot_water_cut', b'show plot water cut'), (b'show_plot_gas_oil_ratio', b'show plot gas oil ratio'), (b'simulation_time', b'simulation duration'), (b'warning_count', b'warning count'), (b'water_in_place', b'water-in-place')], max_length=200),
        ),
    ]
