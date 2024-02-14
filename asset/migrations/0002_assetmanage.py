# Generated by Django 4.2.10 on 2024-02-13 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetManage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_name', models.CharField(max_length=120)),
                ('asset_coade', models.CharField(max_length=16, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('image_url', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('asset_catg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.assetcatg')),
            ],
        ),
    ]
