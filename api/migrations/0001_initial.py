# Generated by Django 4.2.11 on 2024-03-04 11:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.TextField()),
                ('commercial_registration_number', models.CharField(max_length=255)),
                ('tax_card_number', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('landline', models.CharField(max_length=255)),
                ('fax_number', models.CharField(max_length=255)),
                ('company_type', models.CharField(max_length=255)),
                ('company_capital', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('owner_id', models.CharField(max_length=20)),
                ('onwer_position', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_field', models.CharField(max_length=255)),
                ('secondary_field', models.CharField(max_length=255)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
        migrations.CreateModel(
            name='Branche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=255)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('mobile_number', models.CharField(max_length=15)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]
