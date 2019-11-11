from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('add', views.AddAPIView.as_view()),
    path('students', views.StudentListAPIView.as_view()),
    path('student/<id>', views.StudentDetailAPIView.as_view()),
    path('students/<id>', views.StudentUpdateAPIView.as_view()),
    path('clear', views.ClearStudentRecordsAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
