from django.urls import path, include, re_path
from . import views
from .models import Elective
from .views import (
    ElectiveListView, 
    ElectiveDetailView, 
    CommentCreateView
)
# import csv

urlpatterns = [
    path('', ElectiveListView.as_view(), name='electives-home'),
    path('about/', views.about, name='electives-about'),
    path('elective/<int:pk>/', ElectiveDetailView.as_view(), name='electives-detail'),
    re_path(r'^comments/', include('django_comments.urls')),
    path('elective/<int:pk>/comment/', views.add_comment_to_elective,
         name='add_comment_to_elective'),
]

