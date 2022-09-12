from django.views.generic import TemplateView
from django.shortcuts import render


class FrontendTemplate(TemplateView):
    template_name = 'index.html'

def index (request, path=''):
    """
    The some page. This renders the  container for the single-page app.
    """
    return render(request, 'index.html')