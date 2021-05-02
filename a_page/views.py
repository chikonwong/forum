from django.http import HttpResponse
from django.shortcuts import render
from a_page.models import Page

# Create your views here.

# def index(request):
#     latest_page_list = Page.objects.order_by('pub_date')
#     context = {'latest_page_list': latest_page_list}
#     return render(request, 'app.html', context)
def index(request):
    latest_page_list = Page.objects.order_by('page_name')
    context = {'latest_page_list': latest_page_list}
    return render(request, 'app.html', context)
