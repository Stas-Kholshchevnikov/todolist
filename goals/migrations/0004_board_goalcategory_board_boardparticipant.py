# Generated by Django 4.2.3 on 2023-08-09 04:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goals', '0003_alter_goalcomment_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалена')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='goalcategory',
            name='board',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='categories', to='goals.board'),
        ),
        migrations.CreateModel(
            name='BoardParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')),
                ('role', models.PositiveSmallIntegerField(choices=[(1, 'Владелец'), (2, 'Редактор'), (3, 'Читатель')], default=1)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='participants', to='goals.board')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='participants', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('board', 'user')},
            },
        ),
    ]
