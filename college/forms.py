from django import forms
# from .models import College

# class CollegeRegistrationForm(forms.ModelForm):
#     class Meta:
#         model = College
#         fields = ['name', 'location', 'year_established']

# from django import forms
# from .models import College, Student, Mentor
# from django.forms import ModelForm


# class CollegeRegistrationForm(ModelForm):
#     class Meta:
#         model = College
#         fields = ['username', 'password', 'college_name', 'location']

#     def __init__(self, *args, **kwargs):
#         super(CollegeRegistrationForm, self).__init__(*args, **kwargs)
#         # Set default role to 'coordinator'
#         self.fields['role'].initial = 'coordinator'
#         # Hide role field from the form
#         self.fields['role'].widget = forms.HiddenInput()


# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=100)
#     password = forms.CharField(widget=forms.PasswordInput())
#     role = forms.ChoiceField(choices=[('coordinator', 'Coordinator'), ('student', 'Student'), ('mentor', 'Mentor')])

# class StudentUploadForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ['username', 'password', 'name', 'department', 'year', 'college', 'image']

# class MentorUploadForm(forms.ModelForm):
#     class Meta:
#         model = Mentor
#         fields = ['username', 'password', 'name', 'department', 'college', 'domain']

# class ProjectRegistrationForm(forms.Form):
#     project_title = forms.CharField(label='Project Title', max_length=100)
#     choose_domains = forms.ChoiceField(label='Choose Domains', choices=(
#         ('web', 'Web Development'),
#         ('mobile', 'Mobile App Development'),
#         ('design', 'Graphic Design'),
#         # Add more choices as needed
#     ))
#     member_details_1 = forms.CharField(label='Member Details (Student 1)', max_length=100)
#     member_details_2 = forms.CharField(label='Member Details (Student 2)', max_length=100)
#     member_details_3 = forms.CharField(label='Member Details (Student 3)', max_length=100)
