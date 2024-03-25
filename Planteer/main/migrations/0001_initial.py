# Generated by Django 5.0.3 on 2024-03-24 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2048)),
                ('content', models.TextField()),
                ('is_published', models.BooleanField()),
                ('published_at', models.DateTimeField(auto_now_add=True)),
                ('poster', models.ImageField(default='images/def.jpg', upload_to='images/')),
                ('category', models.CharField(choices=[('Tree', 'Tree'), ('Fruit', 'Fruit'), ('Vegetables', 'Vegetables')], max_length=30)),
            ],
        ),
    ]