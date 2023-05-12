# Generated by Django 4.0.9 on 2023-03-28 17:47

from django.db import migrations, models
import django.db.models.deletion
import documents.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('docID', models.UUIDField(default=documents.models.generate_uuid, editable=False, unique=True)),
                ('docPath', models.TextField(blank=True, null=True)),
                ('metadataID', models.UUIDField(blank=True, null=True)),
                ('metadataPath', models.TextField(blank=True, null=True)),
                ('eof', models.BooleanField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(blank=True, max_length=200, null=True)),
                ('resultDocID', models.UUIDField(blank=True, null=True)),
                ('resultDocPath', models.TextField(blank=True, null=True)),
                ('resultTotalObject', models.IntegerField(blank=True, null=True)),
                ('resultTotalImage', models.IntegerField(blank=True, null=True)),
                ('resultTotalPage', models.IntegerField(blank=True, null=True)),
                ('resultPageList', models.TextField(blank=True, null=True)),
                ('resultMessage', models.TextField(blank=True, max_length=250, null=True)),
                ('isAdvancedSearch', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documents.documents')),
            ],
        ),
    ]