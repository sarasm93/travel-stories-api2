# Generated by Django 3.2.20 on 2023-08-12 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=50)),
                ('activities', models.TextField(blank=True, max_length=800)),
                ('priority', models.IntegerField(choices=[(1, 'Now'), (2, 'Soon'), (3, 'Within 3 years'), (4, 'Within 5 years'), (5, 'Might happen')], default=1)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
            options={
                'ordering': ['-priority'],
            },
        ),
    ]
