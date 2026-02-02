from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from complaints.models import Complaint
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# def superuser_check(user):
#     return user.is_superuser

# @user_passes_test(superuser_check)
def dashboard(request):
    users = User.objects.filter(is_superuser=False)#[<>,<>]
    complaints= Complaint.objects.all()
    return render(request,"dashboard.html",{"users":users,"complaints":complaints})

