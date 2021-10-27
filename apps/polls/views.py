from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from .models import Question


@login_required
def dashboard(request):
    label = []

    data = []
    count = Question.objects.filter(user=request.user).count()
    questions = Question.objects.filter(user=request.user).annotate(month=TruncMonth('pub_date'))\
        .values('month').annotate(total=Count('id'))

    for question in questions:
        label.append(question['month'].strftime('%B'))
        data.append(question['total'])
    context = {
        'label': label,
        'data': data,
        'count': count,
        'segment': ["dashboard"]
    }

    return render(request, 'polls/dashboard.html', context)


@login_required()
def profile(request):
    segment = ["profile"]
    if request.method == "GET":
        return render(request, "polls/profile.html", context={"segment": segment})
    elif request.method == "POST":
        messages.success(request, "Profile updated successfully")
        return redirect('/polls/profile/')
