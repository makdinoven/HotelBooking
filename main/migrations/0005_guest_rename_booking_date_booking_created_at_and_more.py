# Generated by Django 5.1.3 on 2024-12-02 21:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_check_in_booking_check_in_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='booking_date',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='email',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='patronymic',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='room',
            name='description',
        ),
        migrations.RemoveField(
            model_name='room',
            name='floor_number',
        ),
        migrations.RemoveField(
            model_name='room',
            name='image',
        ),
        migrations.RemoveField(
            model_name='room',
            name='is_booked',
        ),
        migrations.RemoveField(
            model_name='room',
            name='price',
        ),
        migrations.AddField(
            model_name='room',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='main.room'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_number',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('standard', 'Standard'), ('comfort', 'Comfort'), ('luxury', 'Luxury')], max_length=10),
        ),
        migrations.AddField(
            model_name='booking',
            name='guest',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='main.guest'),
            preserve_default=False,
        ),
    ]
