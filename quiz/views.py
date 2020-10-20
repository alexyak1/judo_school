from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Techniques

def index(request):
    latest_technic_list = Techniques.objects.order_by('-id')[:5]
    template = loader.get_template('quiz/index.html')
    context = {
        'latest_technic_list': latest_technic_list,
    }

    return HttpResponse(template.render(context, request))

def delail(request, techniques_id):
    try:
        technic = Techniques.objects.get(pk=techniques_id)
    except Techniques.DoesNotExist:
        raise Http404("technic does not exist")
    return HttpResponse("You are looking at techniq %s." % techniques_id)

def results(request, techniques_id):
    response = "You are looking at the result of question %s."
    return HttpResponse(response % techniques_id)

def vote(request, techniques_id):
    return HttpResponse("You are voting on techniq %s." % techniques_id)
