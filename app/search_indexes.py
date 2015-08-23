from haystack import indexes
from models import Vocab

class VocabIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, model_attr='definition')
	word = indexes.CharField(model_attr='word')

	def get_model(self):
		return Vocab

	def index_queryset(self, using=None):
		return self.get_model().objects.all()