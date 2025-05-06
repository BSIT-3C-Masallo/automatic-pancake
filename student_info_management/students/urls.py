from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list_view, name='student_list'),
    path('create/', views.student_info_view, name='student_create'),
    path('update/<int:pk>/', views.student_info_view, name='student_update'),  # Use the same view for both create and update
    path('delete/<int:pk>/', views.student_delete_view, name='student_delete'),
    path('view/<int:pk>/', views.student_view, name='student_view'),
    path('success/', views.student_success_view, name='student_success'),
]
