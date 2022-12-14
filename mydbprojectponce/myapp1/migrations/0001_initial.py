# Generated by Django 3.2.6 on 2021-10-10 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation_Transaction',
            fields=[
                ('dt_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('date_donated', models.DateField()),
                ('blood_type', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Donors',
            fields=[
                ('donor_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('contact_number', models.CharField(max_length=20)),
                ('blood_type', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('patient_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('contact_number', models.CharField(max_length=20)),
                ('blood_type', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Phlebotomists',
            fields=[
                ('pbt_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('contact_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('loc_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=20)),
                ('date_of_transaction', models.DateField()),
                ('dt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp1.donation_transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Donations',
            fields=[
                ('donation_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_of_donation', models.DateField()),
                ('amount', models.IntegerField()),
                ('donor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp1.donors')),
            ],
        ),
        migrations.AddField(
            model_name='donation_transaction',
            name='donation_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp1.donations'),
        ),
        migrations.AddField(
            model_name='donation_transaction',
            name='patient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp1.patients'),
        ),
        migrations.AddField(
            model_name='donation_transaction',
            name='pbt_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp1.phlebotomists'),
        ),
    ]
