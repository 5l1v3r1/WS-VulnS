# Generated by Django 2.1.7 on 2019-07-02 12:33

from django.db import migrations, models
import django.db.models.deletion
import picklefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('XMLb', 'XML Bomb'), ('OVSXML', 'Oversized XML'), ('OVSPYLD', 'Oversized Payload'), ('SQLi', 'SQL Injection'), ('XMLi', 'XML Injection')], max_length=18)),
                ('family', models.CharField(choices=[('DoS', 'Denial Of Service'), ('Inj', 'Injection')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='DosAttack',
            fields=[
                ('attack_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Attacks.Attack')),
                ('payload', models.TextField(blank=True)),
                ('average_reponse_delay', models.PositiveIntegerField(null=True)),
            ],
            bases=('Attacks.attack',),
        ),
        migrations.CreateModel(
            name='InjAttack',
            fields=[
                ('attack_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Attacks.Attack')),
                ('patterns', picklefield.fields.PickledObjectField(editable=False, null=True)),
            ],
            bases=('Attacks.attack',),
        ),
        migrations.CreateModel(
            name='OversizedPayloadAttack',
            fields=[
                ('dosattack_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Attacks.DosAttack')),
                ('type', models.CharField(blank=True, choices=[('Header', 'SOAP Header'), ('Body', 'SOAP Body'), ('Envelope', 'SOAP Envelope')], max_length=35)),
            ],
            bases=('Attacks.dosattack',),
        ),
        migrations.CreateModel(
            name='OversizedXMLAttack',
            fields=[
                ('dosattack_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Attacks.DosAttack')),
                ('type', models.CharField(blank=True, choices=[('OverAttrContent', 'XML Oversized Attribute Content'), ('LongNames', 'XML Extra Long Names')], max_length=35)),
            ],
            bases=('Attacks.dosattack',),
        ),
        migrations.CreateModel(
            name='SQLiAttack',
            fields=[
                ('injattack_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Attacks.InjAttack')),
                ('type', models.CharField(blank=True, choices=[('Taut', 'Tautology'), ('Union', 'Union'), ('PiggyB', 'Piggy Backed'), ('IncQ', 'Illegal_logically incorrect queries')], max_length=35)),
            ],
            bases=('Attacks.injattack',),
        ),
        migrations.CreateModel(
            name='XMLBombAttack',
            fields=[
                ('dosattack_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Attacks.DosAttack')),
                ('type', models.CharField(blank=True, choices=[('BIL', 'Billion Laughs'), ('ExtEnt', 'External Entity'), ('IntEnt', 'Internal Entity')], max_length=35, null=True)),
            ],
            bases=('Attacks.dosattack',),
        ),
        migrations.CreateModel(
            name='XMLiAttack',
            fields=[
                ('injattack_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Attacks.InjAttack')),
                ('type', models.CharField(blank=True, choices=[('Malformed', 'Malformed'), ('Replicating', 'Replicating'), ('XPath', 'XPath')], max_length=35)),
            ],
            bases=('Attacks.injattack',),
        ),
    ]
