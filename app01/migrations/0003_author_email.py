# Generated by Django 2.0.5 on 2018-08-14 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20180813_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.EmailField(default='414804000@qq.com', max_length=254),
        ),
    ]
