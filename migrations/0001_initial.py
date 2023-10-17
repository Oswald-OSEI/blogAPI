# Generated by Django 4.2.4 on 2023-10-16 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Content', models.TextField()),
                ('Images', models.ImageField(upload_to='Blog/Images')),
                ('Date_Uploaded', models.DateTimeField(auto_now_add=True)),
                ('Upload_by', models.CharField(max_length=100)),
            ],
        ),
    ]
