# Generated by Django 4.2.3 on 2023-08-21 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUploadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='uploads/')),
                ('image2', models.ImageField(upload_to='uploads/')),
                ('result_word', models.CharField(max_length=50)),
            ],
        ),
    ]