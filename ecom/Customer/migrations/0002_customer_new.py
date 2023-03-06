# Generated by Django 4.1.6 on 2023-03-05 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer_new',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('contact', models.IntegerField()),
                ('adhar_no', models.TextField(max_length=200)),
                ('pan_no', models.TextField(max_length=200)),
            ],
        ),
    ]
