# Generated by Django 4.1.7 on 2023-03-19 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='services',
            field=models.CharField(choices=[('Web Development', 'Web Development'), ('Software Development', 'Software Development'), ('App Development', 'App Development'), ('Graphic Design', 'Graphic Design'), ('Video Editing', 'Video Editing'), ('IT Consultation', 'IT Consultation'), ('Data Entry', 'Data Entry'), ('Photography', 'Photography'), ('Software Installation', 'Software Installation'), ('Cybersecurity service', 'Cybersecurity service'), ('Hardware Configuration', 'Hardware Configuration'), ('Database Development', 'Database Development'), ('Videography', 'Videography'), ('Digital Marketing', 'Digital Marketing'), ('Writing', 'Writing'), ('Other', 'Other')], max_length=50),
        ),
    ]
