# Generated by Django 4.1.1 on 2023-05-09 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ang', '0003_alter_consumer_adhar_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=100)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=25)),
                ('produck_name', models.CharField(max_length=100)),
            ],
        ),
    ]
