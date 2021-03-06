# Generated by Django 2.2.7 on 2019-11-17 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('poc_name', models.CharField(max_length=50)),
                ('poc_mobile_no', models.IntegerField()),
                ('date_of_joining', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.URLField(max_length=100)),
                ('date_of_release', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('mobile_no', models.IntegerField()),
                ('nic_no', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('date_of_joining', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='interpreter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('mobile_no', models.IntegerField()),
                ('nic_no', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('calls_served', models.IntegerField()),
                ('average_rating', models.FloatField()),
                ('date_of_joining', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='content',
            name='interpreter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.interpreter'),
        ),
    ]
