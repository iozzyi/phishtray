# Generated by Django 2.0.5 on 2018-05-24 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0008_auto_20180524_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseURL',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(blank=True, max_length=250, null=True)),
                ('actual_url', models.CharField(blank=True, max_length=250, null=True)),
                ('real_url', models.CharField(blank=True, max_length=250, null=True)),
                ('type', models.IntegerField(choices=[(0, 'phishing'), (1, 'regular'), (1, 'etray')])),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseWebPages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(blank=True, max_length=250, null=True)),
                ('url', models.CharField(blank=True, max_length=250, null=True)),
                ('type', models.IntegerField(choices=[(0, 'phishing'), (1, 'regular'), (1, 'etray')])),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='exerciseemail',
            name='type',
            field=models.IntegerField(choices=[(0, 'phishing'), (1, 'regular'), (1, 'etray')]),
        ),
        migrations.AddField(
            model_name='exerciseurl',
            name='web_page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercise.ExerciseWebPages'),
        ),
    ]