# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EJC',
            fields=[
                ('title', models.CharField(max_length=500)),
                ('article_id', models.AutoField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vocab',
            fields=[
                ('word', models.CharField(max_length=50, db_column=b'word')),
                ('definition', models.CharField(max_length=300, db_column=b'definition')),
                ('word_id', models.AutoField(default=uuid.uuid4, unique=True, serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'vocab',
            },
        ),
    ]
