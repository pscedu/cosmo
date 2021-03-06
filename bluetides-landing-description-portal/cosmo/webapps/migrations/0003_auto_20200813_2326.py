# Generated by Django 2.2.5 on 2020-08-13 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapps', '0002_auto_20200731_1849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Argument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('restriction', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='endpoint',
            name='arguments',
            field=models.ManyToManyField(to='webapps.Argument'),
        ),
    ]
