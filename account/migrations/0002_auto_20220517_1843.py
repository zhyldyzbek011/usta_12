# Generated by Django 3.2.7 on 2022-05-17 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker_card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('body', models.TextField(blank=True)),
                ('images', models.ImageField(blank=True, upload_to='images/')),
                ('phone_number', models.CharField(max_length=13)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card', to='account.category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Worker_cardImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card', to='account.worker_card')),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
            },
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.DeleteModel(
            name='PostImages',
        ),
        migrations.AddField(
            model_name='comment',
            name='card',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='account.worker_card'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='likes',
            name='card',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='account.worker_card'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='likes',
            unique_together={('card', 'user')},
        ),
        migrations.RemoveField(
            model_name='likes',
            name='post',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]