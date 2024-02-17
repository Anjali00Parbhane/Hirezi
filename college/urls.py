# from django.urls import path
# from .views import register_college, all_login_page

# urlpatterns = [
#     path('', register_college, name='register_college'),
#     path('all_login/', all_login_page, name='all_login'),
#     # Add other URLs for student and mentor dashboards
# ]

from django.urls import path
from .import views

urlpatterns = [
    path('', views.welcome_page, name='welcome_page'),
    path('login/', views.all_login, name='login'),
    path('register_college/', views.register_college, name='register_college'),
    path('register_student/', views.register_student, name='register_student'),
    path('register_mentor/', views.register_mentor, name='register_mentor'),

#     path('register-college/', views.CollegeRegistrationForm, name='register-college'),
#     path('import-student-data/', views.import_student_data, name='import-student-data'),
#     path('import-mentor-data/', views.import_mentor_data, name='import-mentor-data'),
 ]

