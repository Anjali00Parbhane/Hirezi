# from django.db import models
# from django.contrib.auth.models import User

# class College(models.Model):
#     name = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)
#     year = models.PositiveSmallIntegerField()
#     is_verified = models.BooleanField(default=False)

# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     department = models.CharField(max_length=100)
#     year = models.PositiveSmallIntegerField()
#     college = models.ForeignKey(College, on_delete=models.CASCADE)

# class Mentor(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     department = models.CharField(max_length=100)
#     college = models.ForeignKey(College, on_delete=models.CASCADE)
#     domain = models.CharField(max_length=100)
# from django.db import models
# from django.contrib.auth.models import User

# class College(models.Model):
#     college_id = models.AutoField(primary_key=True)  # Unique ID for each college
#     name = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)
#     year_established = models.PositiveSmallIntegerField()

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     department = models.CharField(max_length=100)
#     year = models.PositiveSmallIntegerField()
#     college = models.ForeignKey(College, on_delete=models.CASCADE)

# class Mentor(models.Model):
#     name = models.CharField(max_length=100)
#     department = models.CharField(max_length=100)
#     college = models.ForeignKey(College, on_delete=models.CASCADE)
#     domain = models.CharField(max_length=100)
# from django.db import models

# class College(models.Model):
#     username = models.CharField(max_length=100,blank=False)
#     password = models.CharField(max_length=100, null=True, default=None)
#     role = models.CharField(max_length=20, default="coordinator")
#     college_name = models.CharField(max_length=100)
#     college_id = models.AutoField(primary_key=True)
#     location = models.CharField(max_length=100)

# class Student(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     role = models.CharField(max_length=20, default='student')
#     name = models.CharField(max_length=100)
#     student_id = models.AutoField(primary_key=True)
#     department = models.CharField(max_length=100)
#     year = models.IntegerField()
#     college = models.ForeignKey(College, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='student_images/', null=True, blank=True)

# class Mentor(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     role = models.CharField(max_length=20, default='mentor')
#     name = models.CharField(max_length=100)
#     mentor_id = models.AutoField(primary_key=True)
#     department = models.CharField(max_length=100)
#     college = models.ForeignKey(College, on_delete=models.CASCADE)
#     domain = models.CharField(max_length=100)

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER = (
        (1,'COORDINATOR'),
        (2,'STUDENT'),
        (3,'MENTOR'),
    ) 

    user_type = models.CharField(choices=USER, max_length=50,default=1)

class College(models.Model):
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()

    def __str__(self):
        return self.admin.first_name
    
class Student(models.Model):
    user_1 = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    college_name = models.ForeignKey(College, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    course_year = models.CharField(max_length=100)
    college_serial_no = models.IntegerField()
    no_of_projects = models.IntegerField(default=0)

    # Other student fields

    # def save(self, *args, **kwargs):
    #     # Set username to college name
    #     self.user_1.username = self.college_name.admin.first_name
    #     super().save(*args, **kwargs)

    # def __str__(self):
    #     return self.admin.first_name
    def __str__(self):
        return self.user_1.first_name
    
class Domain(models.Model):
    domain_name = models.CharField(max_length=100)
    def __str__(self):
        return self.domain_name

class ProjectRegistration(models.Model):
    project_title = models.CharField(max_length=200)
    project_domain = models.ForeignKey(Domain, on_delete=models.DO_NOTHING)
    # support_doc = models.FileField(upload_to='document')

    def __str__(self):
        return self.project_title
    
class Group(models.Model):
    group_name = models.CharField(max_length=200)
    member_details_1 = models.CharField(max_length=100)
    member_details_2 = models.CharField(max_length=100)
    member_details_3 = models.CharField(max_length=100)
    member_details_4 = models.CharField(max_length=100)

    def __str__(self):
        return self.group_name