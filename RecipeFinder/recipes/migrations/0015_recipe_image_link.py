# Generated by Django 5.0.4 on 2024-05-05 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0014_alter_category_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image_link',
            field=models.CharField(default=2, max_length=1000),
            preserve_default=False,
        ),
    ]