from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse

from .models import Techniques, Belt_group

def index(request):
    latest_technic_list = Techniques.objects.order_by('-id')[:5]
    template = loader.get_template('quiz/index.html')
    context = {
        'latest_technic_list': latest_technic_list,
    }

    return HttpResponse(template.render(context, request))

def detail(request, techniques_id):
    try:
        technic = Techniques.objects.get(pk=techniques_id)
        belts = Belt_group.objects.all()
    except Techniques.DoesNotExist:
        raise Http404("technic does not exist")
    return render(request, 'quiz/detail.html', {'technic': technic, 'belts': belts})

def results(request, techniques_id):
    response = "You are looking at the result of question %s."
    return HttpResponse(response % techniques_id)

def vote(request, techniques_id):
    print("question")
    # print(request)



    technic = Techniques.objects.get(pk=techniques_id)
    right_belt_color = get_object_or_404(Belt_group, pk=technic.belt_group_id)


    response = "No, it was technic from: %s belt."
    if str(request.POST['selected_belt']) == str(right_belt_color):
        response = "Nice! That's right it is %s"
    return HttpResponse(response % right_belt_color)

