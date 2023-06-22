from django.urls import path
from .views import  HomeView,StudentCreateView
from . import views

urlpatterns = [
    path('student_login/', StudentCreateView.as_view(), name='student_login'),
    path('home/', HomeView, name='home'),
    path('student_list/', views.student_list, name='student_list'),
    path('student_detail/<int:student_id>/', views.student_detail, name='student_detail'),
    path('update/<int:student_id>/', views.student_update, name='student_update'),
    path('delete/<int:student_id>/', views.student_delete, name='student_delete'),
    path('success/', views.success_view, name='success'),
    path('updated_vew/', views.update_view, name='update_view'),
    path('delete_view/',views.delete_view,name='delete_view'),
     path('total_student_list/', views.TotalStudents, name='total'),


]
