# Generated by Django 3.2.4 on 2021-08-06 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('phone_no', models.CharField(max_length=15)),
                ('cnic', models.CharField(max_length=55)),
                ('course_enrolled', models.CharField(max_length=55)),
                ('cgpa', models.FloatField()),
            ],
        ),
    ]
