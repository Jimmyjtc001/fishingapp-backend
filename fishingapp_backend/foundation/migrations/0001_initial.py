from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FishingSpot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('is_hidden', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SearchElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type_of_fishing_found', models.CharField(max_length=255, blank=True, null=True,)),
                ('kind_of_fishing_gear_to_bring' , models.CharField(max_length=255, blank=True, null=True,)),
                ('adress', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(max_length=255)),
                ('province', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(max_length=255)),
                ('is_hidden', models.BooleanField(blank=True, default=False)),
                ('FishingSpot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foundation.FishingSpot')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('searchelement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foundation.SearchElement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
