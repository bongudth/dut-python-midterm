from django.urls import path
from .views import student_create_view, student_delete_view, student_list_view, student_detail_view, student_update_view

urlpatterns = [
    path('create/', student_create_view, name='create'),
    path('', student_list_view, name='list'),
    path('<int:id>', student_detail_view, name='detail'),
    path('<int:id>/update/', student_update_view, name='update'),
    path('<int:id>/delete/', student_delete_view, name='delete'),
]
