from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Message
# Create your views here.
# def massageView (request):
#     return render( request,'home.html')
class MessageView(TemplateView):

    def get_template_names (self):
        key = self.request.resolver_match.url_name 
        if key =='events':
                return ['events.html']
        elif key == 'participants':
                return ['participants.html']

        


# class MessageView(ListView):
#     model =Message
#     # نشان میدهد که از کدام مدل دیتا بیس باید برود بخواند 
#     template_name = 'home.html'
# # دیتا های خوانده شده را به سمت فایل اچ تی ام ال مان میفرستد !