# Generated by Django 4.2.4 on 2023-11-30 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('CentroDeBowling', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='cliente_groups', to='auth.group'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='password',
            field=models.CharField(default=None, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='cliente_user_permissions', to='auth.permission'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='username',
            field=models.CharField(default=None, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='num_cliente',
            field=models.IntegerField(unique=True),
        ),
    ]
