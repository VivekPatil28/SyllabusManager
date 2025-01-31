from django.contrib import admin
from .models import *


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display =('name','id')
    

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display =('name','subject','id',)
    list_filter = ( 'subject',)
    
    

admin.site.register(Semester)
admin.site.register(Quote)
admin.site.register(UserScore)


admin.site.register(Choice)
admin.site.register(UserQuizAttempt)
admin.site.register(UserAnswer)
admin.site.register(user_completed)

@admin.register(SubTopic)
class SubTopicAdmin(admin.ModelAdmin):
    list_display =('name','topic')
    
    # to make a filter sidebar for filtering Posts
    list_filter = ('topic', )
    
    # To Add a search field in the admin site
    
    search_fields = ('name', 'body')
    
    # #to	prepopulate	the	slug field with the input of the title field
    prepopulated_fields = {'slug': ('name',)}
    
    raw_id_fields = ('topic',)
    
    # To add a ordering functionality on the admin site
    # ordering = (,)

class SubtopicAdmin(admin.StackedInline):
    model = SubTopic
    
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display =('name','id','subject')
    list_filter = ( 'subject','subtopic',)
    inlines=[SubtopicAdmin]
    
    
class ChoiceAdmin(admin.StackedInline):
    model = Choice
    
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display =('question','test','id',)
    list_filter = ( 'test',)
    search_fields = ('question',)
    
    inlines = [ChoiceAdmin]

    class Meta:
        model = Question
    