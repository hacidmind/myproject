from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Topic, Webpage, AccessRecord
# Create your views here.

# class IndexView(TemplateView):
#     template_name = "index.html"

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request,'index.html', context=date_dict)