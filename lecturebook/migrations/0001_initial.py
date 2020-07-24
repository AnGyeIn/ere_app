# Generated by Django 3.0.8 on 2020-07-24 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('sNum', models.TextField()),
                ('pNum', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LectureBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('author', models.TextField()),
                ('lecture', models.TextField()),
                ('option', models.TextField()),
                ('isAvailable', models.BooleanField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owningbooks', to='lecturebook.Student')),
            ],
        ),
    ]
