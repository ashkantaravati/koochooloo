# Generated by Django 3.2.12 on 2022-06-02 14:46

from django.db import migrations, models
import django.db.models.deletion
import hashid_field.field


class Migration(migrations.Migration):

    replaces = [('redirect', '0003_visit'), ('redirect', '0004_alter_visit_reference'), ('redirect', '0005_visit_http_response_code')]

    dependencies = [
        ('redirect', '0002_alter_reference_destination'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7, prefix='', primary_key=True, serialize=False)),
                ('ip', models.GenericIPAddressField()),
                ('user_agent', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('reference', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='redirect.reference')),
                ('http_response_code', models.IntegerField(default=200)),
            ],
        ),
    ]
