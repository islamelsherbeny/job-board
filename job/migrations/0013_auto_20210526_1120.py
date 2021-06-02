# Generated by Django 3.2 on 2021-05-26 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0012_job_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apply',
            old_name='job',
            new_name='Job',
        ),
        migrations.RenameField(
            model_name='apply',
            old_name='webiste',
            new_name='website',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='salary',
            new_name='sallary',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='Vacancy',
            new_name='vacuncy',
        ),
        migrations.RemoveField(
            model_name='job',
            name='owner',
        ),
        migrations.AlterField(
            model_name='apply',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='job',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Full time', 'full time'), ('Part time', 'part time')], max_length=15),
        ),
    ]