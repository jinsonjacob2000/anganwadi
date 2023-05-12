# Generated by Django 4.1.1 on 2023-05-09 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ang', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(max_length=20)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('anganawadi_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ang.anganwadi')),
                ('stock_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ang.admin_stock')),
            ],
        ),
    ]
