# Generated by Django 3.2.12 on 2022-08-25 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servables', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servable',
            name='content_type',
            field=models.CharField(choices=[('text/css', 'CSS (text/css)'), ('text/csv', 'CSV (text/csv)'), ('text/html', 'HTML (text/html)'), ('text/plain', 'Plain Text (text/plain)'), ('text/xml', 'XML (text/xml)'), ('application/javascript', 'JavaScript (application/javascript)'), ('application/xml', 'XML (application/xml)'), ('application/json', 'JSON (application/json)')], max_length=150),
        ),
    ]
