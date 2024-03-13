from django import template
from Main.models import *

register = template.Library()

@register.simple_tag
def calculate_syllabus_coverage(subject, user):
    total_subtopics = SubTopic.objects.filter(topic__subject=subject).count()
    completed_subtopics = user_completed.objects.filter(
        sub_topic__topic__subject=subject, user=user
    ).count()
    if total_subtopics > 0:
        percentage_covered = (completed_subtopics / total_subtopics) * 100
    else:
        percentage_covered = 0
    return round(percentage_covered, 2)

@register.filter
def is_attempted_test(test,user):
    return UserQuizAttempt.objects.filter(user=user, test=test).exists()

@register.filter
def get_all_UserQuizAttempt_per_subject(subject):
    return UserQuizAttempt.objects.filter(test__subject=subject).order_by('-percentage')

