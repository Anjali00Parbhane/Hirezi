from django.shortcuts import render, redirect, HttpResponse
# from django.contrib.auth.models import User
from college.EmailBackend import EmailBackend
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from college.forms import ProjectRegistrationForm
from college.models import College, CustomUser, Student

# from .forms import CollegeRegistrationForm
#  


# def register_college(request):
#     if request.method == 'POST':
#         form = CollegeRegistrationForm(request.POST)
#         if form.is_valid():
#             college = form.save()
#             # Create a user for the college and log in
#             username = form.cleaned_data['college_id']
#             password = User.objects.make_random_password()
#             user = User.objects.create_user(username=username, password=password)
#             college.user = user  # Associate user with college
#             college.save()
#             login(request, user)
#             return redirect('college_dashboard')
#     else:
#         form = CollegeRegistrationForm()
#     return render(request, 'register_college.html', {'form': form})

# def login_page(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         role = request.POST['role']
        
#         # Authenticate user
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             if role == 'student':
#                 if Student.objects.filter(user=user).exists():
#                     login(request, user)
#                     return redirect('student_dashboard')
#             elif role == 'mentor':
#                 if Mentor.objects.filter(user=user).exists():
#                     login(request, user)
#                     return redirect('mentor_dashboard')
#             else:
#                 # Invalid role
#                 return render(request, 'login.html', {'error_message': 'Invalid role'})
        
#         # Authentication failed
#         return render(request, 'login.html', {'error_message': 'Invalid username or password'})
#     else:
#         return render(request, 'login.html')

# from django.shortcuts import render, redirect
# from django import forms
# # from .models import College, Student, Mentor
# from .forms import CollegeRegistrationForm, LoginForm, StudentUploadForm, MentorUploadForm
# # from django.forms import ModelForm

# def welcome_page(request):
#     if request.method == 'POST':
#         login_form = LoginForm(request.POST)
#         if login_form.is_valid():
#             username = login_form.cleaned_data['username']
#             password = login_form.cleaned_data['password']
#             role = login_form.cleaned_data['role']
#             if role == 'coordinator':
#                 # Handle coordinator login
#                 render(request,'welcome_page')
#             elif role == 'student':
#                 # Redirect to student dashboard
#                 pass
#             elif role == 'mentor':
#                 # Redirect to mentor dashboard
#                 pass
#     else:
#         login_form = LoginForm()
#     college_registration_form = CollegeRegistrationForm()
#     return render(request, 'welcome.html', {'login_form': login_form, 'college_registration_form': college_registration_form})

# def register_college(request):
#     if request.method == 'POST':
#         college_registration_form = CollegeRegistrationForm(request.POST)
#         if college_registration_form.is_valid():
#             college_registration_form.save()
#             return redirect('welcome-page')
#     else:
#         college_registration_form = CollegeRegistrationForm()
#     return render(request, 'register_college.html', {'college_registration_form': college_registration_form})
# class CollegeRegistrationForm(forms.ModelForm):
#     class Meta:
#         model = College
#         fields = ['username', 'password', 'college_name', 'location']

#     def __init__(self, *args, **kwargs):
#         super(CollegeRegistrationForm, self).__init__(*args, **kwargs)
#         # Set default role to 'coordinator'
#         self.fields['role'].initial = 'coordinator'
#         # Hide role field from the form
#         self.fields['role'].widget = forms.HiddenInput()

# def import_student_data(request):
#     if request.method == 'POST':
#         form = StudentUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             # Handle student data import from Excel
#             pass
#     else:
#         form = StudentUploadForm()
#     return render(request, 'import_student_data.html', {'form': form})

# def import_mentor_data(request):
#     if request.method == 'POST':
#         form = MentorUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             # Handle mentor data import from Excel
#             pass
#     else:
#         form = MentorUploadForm()
#     return render(request, 'import_mentor_data.html', {'form': form})

def all_login(request):
    if request.method == "POST":
        user = EmailBackend.authenticate(request,
                                           username=request.POST.get('email'),
                                           password=request.POST.get('password'),)
        if user!=None:
          login(request,user)
          user_type = user.user_type
          if user_type == '1':
               return render(request,'Coordinator/index.html')
          elif user_type == '2':
               return HttpResponse('stu')
          elif user_type == '3':
               return HttpResponse('men')
          else:
               messages.error(request,'Email and password are invalid')
               # return redirect('login')
               return HttpResponse('error')
     
    else:
        messages.error(request,'Email and password are invalid')
        return render(request,'login.html')

def welcome_page(request):
     return render(request,'welcome_page.html')

def logout(request):
     logout(request)
     return redirect('login')

def register_college(request):

     if request.method == "POST":
        first_name = request.POST.get('first_name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if CustomUser.objects.filter(email=email).exists():
          messages.warning(request, 'Email already exist') 
          return redirect('register_college')
        
        if CustomUser.objects.filter(username=username).exists():
          messages.warning(request, 'Username already exist') 
          return redirect('register_college')
        else:
          user = CustomUser(
             first_name = first_name,
             email = email,
             username = username,
             password = password,
             user_type = 1,
          )

          user.set_password(password)
          user.save()

          college = College(
              admin = user,
              address = address,
          ) 
          college.save()
          messages.success(request, 'College registered successfully')
          return redirect('login')
     
     return render(request,'register_college.html') 

def register_student(request):
     if request.method == "POST":
        first_name = request.POST.get('first_name')
        department = request.POST.get('department')
        course_year = request.POST.get('course_year')
        college_serial_no = request.POST.get('college_serial_no')
        no_of_projects = request.POST.get('no_of_projects')
        email = request.POST.get('email')
     #    username = request.POST.get('username')
        password = request.POST.get('password')

     #    college_name = request.user.first_name
        college_obj = College.objects.filter(admin=request.user)[0]
   
        
        if CustomUser.objects.filter(email=email).exists():
          print('email',email)
          messages.warning(request, 'Email already exist') 
          return redirect('register_student')
        
        else:
          user = CustomUser(
             first_name = first_name,
             email = email,
             username = email,
             password = password,
             user_type = 2,
          )

          user.set_password(password)
          user.save()

          student = Student(
              user_1 = user,
              college_name = college_obj,
              department = department,
              course_year = course_year,
              college_serial_no = college_serial_no,
              no_of_projects = no_of_projects,
          ) 
          student.save()
          print(student.id)
          print("student regi succ")
          messages.success(request, 'College registered successfully')
          return redirect('register_student')
     
     return render(request,'Coordinator/register_student.html') 

    

def register_mentor(request):
    return render(request,'Coordinator/register_mentor.html')

# def register_project(request):
#     if request.method == 'POST':
#         form = ProjectRegistrationForm(request.POST)
#         if form.is_valid():
#             # Process the form data
#             project_title = form.cleaned_data['project_title']
#             choose_domains = form.cleaned_data['choose_domains']
#             member_details_1 = form.cleaned_data['member_details_1']
#             member_details_2 = form.cleaned_data['member_details_2']
#             member_details_3 = form.cleaned_data['member_details_3']
#             # Perform any further processing or save the data to the database
#             # Redirect to a success page or any other appropriate page
#             project = Project.objects.create(
#                 project_title=project_title,
#                 project_domain=choose_domains,
#                 member_details_1=member_details_1,
#                 member_details_2=member_details_2,
#                 member_details_3=member_details_3
#             )
#             project.save()
#             return redirect('student_dashboard')  # Change 'success_page' to your actual URL name
#     else:
#         form = ProjectRegistrationForm()
#     return render(request, 'new_project.html', {'form': form})


    