# Generated by Django 4.0.5 on 2022-06-21 20:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={},
        ),
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.FileField(blank=True, upload_to='avatars/'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='room_image',
            field=models.FileField(blank=True, upload_to='rooms/'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AddIndex(
            model_name='customuser',
            index=models.Index(fields=['id'], name='id_index'),
        ),
    ]
