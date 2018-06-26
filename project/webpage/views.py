from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'webpage/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'webpage/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question {}.".format(question_id)
    return HttpResponse(response.encode())


def vote(request, question_id):
    response = "You're voting on question {}.".format(question_id)
    return HttpResponse(response.encode())