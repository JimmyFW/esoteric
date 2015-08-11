from django.db import models
import uuid

# Create your models here.
class Vocab(models.Model):
	word = models.CharField(
		max_length=50,
		db_column='word'
	)
	definition = models.CharField(
		max_length=300,
		db_column='definition'
	)

	word_id = models.AutoField(
		primary_key=True,
		default=uuid.uuid4,
		unique=True
	)

	class Meta:
		db_table = 'vocab'

class EJC(models.Model):
	title = models.CharField(
		max_length=500,
	)
	article_id = models.AutoField(primary_key=True)