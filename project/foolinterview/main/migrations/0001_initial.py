# Generated by Django 2.2.1 on 2019-05-15 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article_Comments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('article_reference', models.UUIDField()),
                ('comment', models.TextField(max_length=1000)),
            ],
        ),
    ]