# Generated by Django 3.0.5 on 2020-04-10 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=40)),
                ('contact_no', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('proof_id_no', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('contact_no', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('address', models.CharField(max_length=100)),
                ('gym_name', models.CharField(max_length=30)),
                ('gym_address', models.CharField(max_length=100)),
                ('gym_contact_no', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(default='<function uuid4 at 0x0000016BB58EC280>', editable=False, max_length=36)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('total_fees', models.IntegerField()),
                ('fees_paid', models.IntegerField()),
                ('fees_remaining', models.IntegerField()),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive')])),
                ('customer', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='users.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
    ]
