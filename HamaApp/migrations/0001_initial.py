# Generated by Django 4.0.5 on 2022-07-08 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titre', models.CharField(max_length=100, null=True)),
                ('Description', models.TextField(max_length=10000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Prenom', models.CharField(max_length=100, null=True)),
                ('Nom', models.CharField(max_length=100)),
                ('Mail', models.CharField(max_length=100, null=True)),
                ('Telephone', models.CharField(max_length=100, null=True)),
                ('Societe', models.CharField(max_length=100, null=True)),
                ('Adresse', models.CharField(max_length=100, null=True)),
                ('CodePostale', models.CharField(max_length=100, null=True)),
                ('Ville', models.CharField(max_length=100, null=True)),
                ('Statut', models.CharField(max_length=100, null=True)),
                ('CapitalSocial', models.CharField(max_length=100, null=True)),
                ('NumRCS', models.CharField(max_length=100, null=True)),
                ('VilleRCS', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.FileField(upload_to='')),
                ('nom', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mandat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Produit', models.CharField(max_length=100, null=True)),
                ('Prix', models.CharField(max_length=100)),
                ('Date', models.CharField(max_length=100, null=True)),
                ('Honoraires', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('nom', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
