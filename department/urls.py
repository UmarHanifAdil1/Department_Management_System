from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('login/', views.user_login, name="login_page"),
    path('logout/', views.user_logout, name='logout_page'),
    path('register/', views.register_user, name='registration_page'),
    path('students_form/', views.create_student, name="students_form"),
    path('students_record/', views.read_students, name="students_record"),
    path('students_record/update/<int:id>/', views.update_student, name="update_student"),
    path('students_record/delete/<int:id>/', views.delete_student, name="delete_student"),
    path('search/', views.search_student, name="search"),
    path('searchResult/<str:s>', views.search_result, name="search_result"),
]