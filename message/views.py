from django.views.generic import TemplateView
# Create your views here.
# def massageView (request):
#     return render( request,'home.html')
class MessageView(TemplateView):
    template_name = 'home.html'