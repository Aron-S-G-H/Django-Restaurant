# Generated by Django 4.1.3 on 2022-11-27 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_gallery_options_alter_homeslider_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('phone', models.CharField(max_length=11, verbose_name='شماره همراه')),
                ('message', models.TextField(verbose_name='پیام')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
            ],
            options={
                'verbose_name': 'پیام',
                'verbose_name_plural': 'پیام ها',
            },
        ),
    ]
