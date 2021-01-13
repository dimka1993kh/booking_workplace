# Generated by Django 3.1.5 on 2021-01-11 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workplace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Номер рабочего места')),
                ('free_time_for_booking', models.JSONField(default={'id_1': {'status_free': True, 'title': '8:00 - 9:00'}, 'id_10': {'status_free': True, 'title': '17:00 - 18:00'}, 'id_2': {'status_free': True, 'title': '9:00 - 10:00'}, 'id_3': {'status_free': True, 'title': '10:00 - 11:00'}, 'id_4': {'status_free': True, 'title': '11:00 - 12:00'}, 'id_5': {'status_free': True, 'title': '12:00 - 13:00'}, 'id_6': {'status_free': True, 'title': '13:00 - 14:00'}, 'id_7': {'status_free': True, 'title': '14:00 - 15:00'}, 'id_8': {'status_free': True, 'title': '15:00 - 16:00'}, 'id_9': {'status_free': True, 'title': '16:00 - 17:00'}}, verbose_name='Свободное время для записи')),
            ],
            options={
                'verbose_name': 'Рабочее место',
                'verbose_name_plural': 'Рабочие места',
            },
        ),
        migrations.AlterField(
            model_name='booking',
            name='datetime_from',
            field=models.IntegerField(choices=[(8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], max_length=20, verbose_name='Со скольки хотите работать'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='datetime_to',
            field=models.IntegerField(choices=[(8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], max_length=20, verbose_name='До скольки хотите работать'),
        ),
    ]
