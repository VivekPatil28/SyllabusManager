from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import random
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


class Semester(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Subject(models.Model):
    name = models.CharField(max_length=500, default="")
    sem=models.ForeignKey(Semester,on_delete=models.CASCADE,blank=True,null=True,default=None,related_name='subjects')

    def __str__(self) -> str:
        return self.name

class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True,related_name='topics')
    name = models.TextField(max_length=100, default="")
    is_started = models.BooleanField(default=False)
    weightage =  models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name



class SubTopic(models.Model):
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, null=True, related_name="subtopic"
    )
    name = models.CharField(max_length=500)
    body = RichTextField(null=True,blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name
    


class user_completed(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_completed_user')
    sub_topic=models.ForeignKey(SubTopic,on_delete=models.CASCADE,related_name='all_topics')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} : {self.sub_topic.name}"


class Test(models.Model):
    name = models.CharField(max_length=255, default="Test")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,null=True,default=None,blank=True, related_name="Subject")
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, related_name="Topics", null=True, default=None,blank=True
    )
    def __str__(self) -> str:
        return self.name


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="Test")
    question = models.TextField()

    def __str__(self):
        return self.question
    
class UserScore(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="UserScore")
    coding_skills=models.FloatField(null=True,blank=True)
    aptitude_skills = models.FloatField(null=True,blank=True)
    technical_skills=models.FloatField(null=True,blank=True)
    verbal_skills = models.FloatField(null=True,blank=True)
    academic_skills = models.FloatField(null=True,blank=True)
    backlogs = models.IntegerField(null=True,blank=True)
    placement_pred = models.BooleanField(null=True,blank=True)
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name='choices')
    choice = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice


class UserQuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE,related_name="user_attempted_test")
    date_attempted = models.DateTimeField(auto_now_add=True)
    score = models.PositiveIntegerField(default=0)
    percentage=models.PositiveIntegerField(default=0)
    is_ended=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user.username} - {self.test.name} ({self.date_attempted})"



class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE,null=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - Q{self.question.id}: {None if self.selected_choice is None else self.selected_choice.choice}"

class user_stats(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_stats')
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='subject_stats')
    syllabus_coverage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    syllabus_coverage_time =models.DecimalField(max_digits=7, decimal_places=5, default=0)
    test_score = models.PositiveIntegerField(default=0)

    def update_syllabus_coverage(self):
        self.syllabus_coverage = self.subject.syllabus_covered()
        self.save()

    def update_test_score(self):
        user_attempt = UserQuizAttempt.objects.filter(user=self.user, test__subject=self.subject)
        if user_attempt.exists():
            self.test_score = user_attempt.aggregate(models.Avg('score'))['score__avg']
        self.save()
    

class Quote(models.Model):
    quote = models.TextField(max_length=500, default="")

    @classmethod
    def get_random_quote(cls):
        total_quotes = cls.objects.count()
        if total_quotes == 0:
            return None
        random_index = random.randint(0, total_quotes - 1)
        return cls.objects.all()[random_index]

    def __str__(self) -> str:
        return self.quote
