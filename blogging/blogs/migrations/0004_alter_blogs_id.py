# Generated by Django 5.0.3 on 2024-03-27 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_alter_blogs_desc_alter_blogs_title_alter_blogs_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='id',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False),
        ),
    ]
