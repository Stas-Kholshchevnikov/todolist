# Generated by Django 4.2.3 on 2023-08-11 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0006_alter_goalcategory_board'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='board',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='goalcategory',
            name='board',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='categories', to='goals.board'),
        ),
    ]