from django.contrib import admin
from django.urls import path ,include


admin.site.site_header = 'Syllabus Manager'
admin.site.index_title = 'Welcome User'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("Main.urls")),
    
]
