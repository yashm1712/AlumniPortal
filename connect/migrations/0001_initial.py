# Generated by Django 3.1 on 2020-09-25 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reunion',
            fields=[
                ('Sr_No', models.AutoField(primary_key=True, serialize=False)),
                ('Date', models.DateTimeField(blank=True)),
                ('Title', models.CharField(blank=True, max_length=20, null=True)),
                ('Memo', models.TextField(blank=True, null=True)),
                ('Place', models.CharField(blank=True, max_length=50, null=True)),
                ('Batch', models.CharField(blank=True, max_length=7, null=True)),
                ('Participants', models.ManyToManyField(blank=True, default=None, related_name='Participants', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participants', models.CharField(choices=[("I'm In", "I'm In"), ("I'm Out", "I'm Out")], default=None, max_length=10)),
                ('reunion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='connect.reunion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]