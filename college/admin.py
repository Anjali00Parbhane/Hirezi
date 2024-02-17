from django.contrib import admin

# Register your models here.
from.models import *
from django.contrib.auth.admin import UserAdmin

# admin.site.register(College)
# admin.site.register(Student)
# admin.site.register(Mentor)
class UserModel(UserAdmin):
    list_display = ['username', 'user_type']

admin.site.register(CustomUser,UserModel)
admin.site.register(College)
admin.site.register(Student)
admin.site.register(Domain)
admin.site.register(ProjectRegistration)
admin.site.register(Group)


