from django.views.generic import TemplateView
from django.shortcuts import render


class FrontendTemplate(TemplateView):
    # def get(self,request):
    #     print(type(request))
    template_name='index.html'



 
def index(request, path=''):
    """
    The home page. This renders the container for the single-page app.
    """
    return render(request, 'index.html')