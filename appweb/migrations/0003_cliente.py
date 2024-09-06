# Generated by Django 5.0.4 on 2024-09-02 04:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0002_alter_categorias_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=8)),
                ('sexo', models.CharField(choices=[('M', 'M'), ('F', 'F')], default='M', max_length=1)),
                ('telefono', models.CharField(max_length=20)),
                ('fehca_nacimiento', models.DateField(null=True)),
                ('direccion', models.TextField()),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
