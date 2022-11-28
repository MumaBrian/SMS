from django.urls import path,re_path
from  teacher import views
app_name = "teacher"
urlpatterns = [
    re_path('',views.TeacherFileUploadView.as_view()),
    # path('', views.index, name='index'),
]