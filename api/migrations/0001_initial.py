# Generated by Django 2.2.4 on 2019-09-01 04:41

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('title', models.CharField(max_length=128)),
                ('avatar_url', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=256)),
                ('total_posts', models.PositiveIntegerField(default=0)),
                ('is_banned', models.BooleanField(default=False)),
                ('last_active', models.DateTimeField()),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'voz_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'voz_box',
            },
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='forums', to='api.Box')),
            ],
            options={
                'db_table': 'voz_forum',
            },
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('rating', models.PositiveIntegerField(default=0)),
                ('views', models.PositiveIntegerField(default=0)),
                ('replies', models.PositiveIntegerField(default=0)),
                ('visible', models.BooleanField(default=True)),
                ('is_sticky', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('delete_reason', models.CharField(max_length=128)),
                ('last_post_data', django.contrib.postgres.fields.jsonb.JSONField(default=None)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='threads', to=settings.AUTH_USER_MODEL)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='threads', to='api.Forum')),
            ],
            options={
                'db_table': 'voz_thread',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('raw', models.TextField()),
                ('content_format', models.PositiveSmallIntegerField(choices=[(1, 'bbcode'), (2, 'markdown')])),
                ('order_number', models.PositiveIntegerField()),
                ('upvotes', models.PositiveIntegerField(default=0)),
                ('visible', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=True)),
                ('delete_reason', models.CharField(max_length=128)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='replies', to='api.Post')),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='api.Thread')),
            ],
            options={
                'db_table': 'voz_post',
                'unique_together': {('thread', 'order_number')},
            },
        ),
    ]
