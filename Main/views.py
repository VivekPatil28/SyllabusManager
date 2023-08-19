from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import *
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

@login_required
def homepage(request):
    Subjects = Subject.objects.filter(sem=1)
    params = {
        "Subjects": Subjects,
        "quote": Quote,
    }
    return render(request, "homepage.html", params)


def signin(request):
    if request.method != "POST":
        return render(request, "sign_in_up.html")
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("/")


def signup(request):
    if request.method != "POST":
        return render(request, "sign_in_up.html")
    fname = request.POST["fname"]
    lname = request.POST["lname"]
    username = request.POST["username"]
    password = request.POST["password"]
    profile = request.POST.get("profile")
    user = User.objects.create_user(
        first_name=fname, last_name=lname, username=username, password=password
    )
    user.save()
    if user is not None:
        login(request, user)
        return redirect("/")


@login_required
def signout(request):
    logout(request)
    return render(request, "sign_in_up.html")


@login_required
def roadmap(request, str):
    sub = Subject.objects.get(name=str)
    Topics = Topic.objects.filter(subject=sub)
    completed_subtopics = user_completed.objects.filter(user=request.user).values_list('sub_topic_id', flat=True)
    params = {
        "Topics": Topics,
        "completed_subtopics":completed_subtopics,
    }

    return render(request, "roadmap.html", params)


@login_required
def checked(request):
    if request.method == "POST":
        data = json.loads(request.body)
        topic = SubTopic.objects.get(id=data["id"])
        checked = data["checked"]
        if checked:
            t,is_created=user_completed.objects.get_or_create(user=request.user,sub_topic=topic)
            t.save()
        else:
            t=user_completed.objects.get(user=request.user,sub_topic=topic)
            t.delete()
        response_data = {"message": "Data received successfully"}
    else:
        response_data = {"message": "Some Error Occured"}
    return JsonResponse(response_data)
    
@login_required
def readyToStartTest(request):
    request.session.pop("test_id",None)
    UserAnswer.objects.filter(user=request.user).delete()
    request.session['test_id'] = request.POST.get("test_id")
    test = Test.objects.get(id=request.session.get('test_id'))
    quiz_attempt,is_created = UserQuizAttempt.objects.get_or_create(user=request.user,test=test)
    params={
        'test':test,
    }
    if quiz_attempt.is_ended:
        return redirect('/')
    return render(request,'readytostartTest.html',params)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def starttest(request):
    if request.method != "POST":
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    test_id = request.session.get('test_id')
    test = Test.objects.get(id=test_id)
    if UserQuizAttempt.objects.get(user=request.user,test=test).is_ended:
        return redirect('/')
    questions = Question.objects.filter(test=test)
    page_number = request.POST.get("page")
    paginator = Paginator(questions, 1)
    page_obj = paginator.get_page(page_number)

    if page_obj.number-1:
        question = Question.objects.get(id=request.POST.get("question"))
        if not UserAnswer.objects.filter(user=request.user,question=question):
            userans, is_created = UserAnswer.objects.get_or_create(
                user=request.user,
                question=question,
                selected_choice=Choice.objects.get(id=request.POST.get("ans")) if request.POST.get("ans") else None,
                is_correct=Choice.objects.get(id=request.POST.get("ans")).is_correct if request.POST.get("ans") else False,
            )
    
    if request.POST.get("is_submitted"):
        return redirect('/showResult')
    
    params = {"page_obj": page_obj, "test_id": test_id}
    return render(request, "test.html", params)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def showResult(request):
    if not request.session.get('test_id'):
        return redirect('/')
    quiz=UserQuizAttempt.objects.get(user=request.user,test=request.session.get('test_id'))
    res = UserAnswer.objects.filter(user=request.user)
    counter = sum(bool(i.is_correct) for i in res)
    quiz.score=counter
    quiz.is_ended=True
    quiz.save()
    
    params={
            'testresult':quiz,
            'quiz_answers':res,
        }
    
    return render(request,'test_results.html',params)
    
    
def subtopicdesc(request, str):
    subtopic = SubTopic.objects.get(slug=str)
    tests = Test.objects.all()
    params = {
        "subtopic": subtopic,
    }
    return render(request, "subtopicdesc.html", params)
