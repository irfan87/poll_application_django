from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }

    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}

    return HttpResponse(render(request, 'polls/detail.html', context))

def results(request, question_id):
    message = "You are looking for a result of question %s"
    return HttpResponse(message % question_id)

def vote(request, question_id):
    message = "You are voting on question %s" % question_id
    return HttpResponse(message)