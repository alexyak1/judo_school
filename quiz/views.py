from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic

from .models import Techniques, Belt_group

class IndexView(generic.ListView):
    template_name = 'quiz/index.html'
    context_object_name = 'latest_technic_list'

    def get_queryset(self):
        """Return the last five technics"""
        return Techniques.objects.order_by('belt_group')



def detail(request, techniques_id):
    try:
        technic = Techniques.objects.get(pk=techniques_id)
        belts = Belt_group.objects.all()
    except Techniques.DoesNotExist:
        raise Http404("technic does not exist")
    return render(request, 'quiz/detail.html', {'technic': technic, 'belts': belts})


def vote(request, techniques_id):

    technic = Techniques.objects.get(pk=techniques_id)
    right_belt_color = get_object_or_404(Belt_group, pk=technic.belt_group_id)

    response = "No, it was technic from: %s belt."
    if str(request.POST['selected_belt']) == str(right_belt_color):
        response = "Nice! That's right it is %s"
    return HttpResponse(response % right_belt_color)

