from django.views.generic import TemplateView
from django.shortcuts import render
from ..data_service import RequestService

class FrontendTemplate(TemplateView):
    # def get(self,request):
    #     print(type(request))
    template_name='index.html'



 
def index(request, path=''):
    print('-----=======++++++++  request.META ++++++++========---------')
    # print(request.META)
    print(request.user)
    # [print(f'{k}: {v}') for k,v in request.META.items()]
    try:
        request_dict = request.META
        request_dict['username'] = str(request.user)
        RequestService.post(request_dict=request_dict)
    except:
        pass

    """
    The home page. This renders the container for the single-page app.
    """
    return render(request, 'index.html')