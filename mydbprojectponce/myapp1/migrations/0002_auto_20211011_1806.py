# Generated by Django 3.2.6 on 2021-10-11 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='location',
            name='loc_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='patients',
            name='username',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='myapp1.users', to_field='username'),
            preserve_default=False,
        ),
    ]
