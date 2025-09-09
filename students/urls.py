from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.StudentListView.as_view(), name='student_list'),
    path('ajouter/', views.StudentCreateView.as_view(), name='student_create'),
    path('<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('<int:pk>/modifier/', views.StudentUpdateView.as_view(), name='student_update'),
    path('<int:pk>/supprimer/', views.StudentDeleteView.as_view(), name='student_delete'),
]
