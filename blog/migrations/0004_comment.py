# Generated by Django 3.1 on 2020-10-03 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20200930_2326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('S_No', models.AutoField(primary_key=True, serialize=False)),
                ('comments', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('blog_c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
