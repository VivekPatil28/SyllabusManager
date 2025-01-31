from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import *
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import pickle

@login_required
def homepage(request):
    completed_subtopics = user_completed.objects.filter(user=request.user).values_list('created_at',flat=True)
    # for i in completed_subtopics:
    #     print(i.date)
    
    semester=Semester.objects.all()
    if 'sem_id' in request.session:
        current_sem = Semester.objects.get(id=request.session['sem_id'])
    else:
        current_sem = Semester.objects.get(id=1)
    Subjects = Subject.objects.filter(sem=current_sem)
    check=None
    if 'check' in request.session:
        check = request.session['check']
    params = {
        "is_checked": check,
        "Subjects": Subjects,
        "quote": Quote,
        "semester":semester,
        "current_sem":current_sem,
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
    else:
        return render(request, "sign_in_up.html",{"error":"Inalid Credientials"})
    return redirect("/")



def signup(request):
    if request.method != "POST":
        return render(request, "signup.html")
    fname = request.POST["fname"]
    lname = request.POST["lname"]
    username = request.POST["username"]
    password = request.POST["password"]
    # profile = request.POST.get("profile")
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
def predict_job(request):
    user_score,is_created = UserScore.objects.get_or_create(user=request.user)
    return render(request,"test_types.html",{"user_score":user_score})
    
    
@login_required  
def test_skills(request):
    test_type  = dict(request.POST.items())["Submit"]
    if(test_type == "Coding Skills"):
        test_id = 44
    elif(test_type == "Aptitude Skills"):
        test_id= 45
    elif(test_type == "Technical Skills"):
        test_id= 46
    elif(test_type == "Verbal Skills"):
        test_id= 47
    elif(test_type == "Academic Skills"):
        return render(request,'academic_skills.html')
    
    test = Test.objects.get(id = test_id)
    questions = Question.objects.filter(test=test)
    
    params={"questions":questions,"test_type":test_type}
    
    return render(request,"prediction_test.html",params)

def save_academic(request):
    if(request.method=="POST"):
        ssc = float(request.POST["ssc"])
        hsc = float(request.POST["hsc"])
        degree = float(request.POST["degree"])
        backlogs = float(request.POST["backlogs"])
        user_score,is_created = UserScore.objects.get_or_create(user=request.user)
        user_score.academic_skills = (ssc+hsc+degree)/3
        user_score.backlogs = backlogs
        user_score.save()
        return redirect("/predict_job")
        
def delete_pred_data(request):
    if(request.method=="POST"):
        user_score = UserScore.objects.get(user=request.user)
        user_score.delete()
    return redirect('/')
        
def calc_score(request):
    if(request.method == "POST"):
        marks=0
        answers={}
        for key, value in request.POST.items():
            if(key.startswith("csrf")):
                pass
            elif(key.startswith("c")):
                answers[key[1:]]=value
        
        for question_id,answer_id in answers.items():
            choice = Choice.objects.get(id = answer_id)
            if(choice.is_correct):
                marks+=1
        
        user_score,is_created = UserScore.objects.get_or_create(user=request.user)
        
        test_type = request.POST["test_type"]
        if(test_type == "Coding Skills"):
            user_score.coding_skills = (marks/15) *100
        elif(test_type == "Aptitude Skills"):
            user_score.aptitude_skills = (marks/15) *100
        elif(test_type == "Technical Skills"):
            user_score.technical_skills = (marks/15) *100
        elif(test_type == "Verbal Skills"):
            user_score.verbal_skills = (marks/15) *100
        user_score.save()
        
        # print(user_score.coding_skills)
        # print(user_score.technical_skills)
        # print(user_score.verbal_skills)
        # print(user_score.aptitude_skills)
        return redirect("/predict_job")
    


def show_prediction(request):
    params={}
    user_score = UserScore.objects.get(user=request.user)
    params["user_score"]=user_score
    if(user_score == None):
        return render(request,'show_prediction.html',{"result":"All tests Are not Completed"})
    #model import
    model = pickle.load (open('Model/model.pkl', 'rb')) 
    
    res = model.predict([[user_score.coding_skills,
                          user_score.aptitude_skills, 
                          user_score.technical_skills,
                          user_score.verbal_skills,
                          user_score.academic_skills,
                          user_score.backlogs,
                          ]])
    params["result"] = res[0]
    user_score.placement_pred=True if res[0]>70 else False
    user_score.save()
    
    
    return render(request,'show_prediction.html',params)
    
    
    
    
    
@login_required
def roadmap(request, str):
    sub = Subject.objects.get(name=str)
    Topics = Topic.objects.filter(subject=sub)
    completed_subtopics = user_completed.objects.filter(user=request.user).values_list('sub_topic_id',flat=True)
    params = {
        "is_checked":request.session['check'],
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
    #Return to the homepage if the user already given that Test
    if quiz_attempt.is_ended:
        return redirect('/')
    return render(request,'readytostartTest.html',params)

@login_required
def starttest(request):
    if request.method != "POST":
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    test_id = request.session.get('test_id')
    test = Test.objects.get(id=test_id)
    #Return to the homepage if the user already given that Test
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



@login_required
def showResult(request):
    if not request.session.get('test_id'):
        return redirect('/')
    quiz=UserQuizAttempt.objects.get(user=request.user,test=request.session.get('test_id'))
    questions_len=Question.objects.filter(test=request.session.get('test_id')).count()
    res = UserAnswer.objects.filter(user=request.user)
    counter = sum(bool(i.is_correct) for i in res)
    quiz.score=counter
    quiz.percentage=round(counter/questions_len*100,2)
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

def changeSem(request):
    sem_id=request.POST.get('sem_id')
    request.session['sem_id'] = sem_id
    return redirect('/')