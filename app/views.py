from django.shortcuts import render
from django.views.generic import TemplateView

from models import Vocab

# Create your views here.

class IndexView(TemplateView):
	template_name = "paginate.html"

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['vocab'] = Vocab.objects.all()
		return context
