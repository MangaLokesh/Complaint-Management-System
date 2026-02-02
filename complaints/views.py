from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Complaint
from rest_framework import status
from .serializers import ComplaintSerializer
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser

@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def resolve_complaint_api(request, id):
    if not request.user.is_staff:
        return Response(
            {"error": "Permission denied"},
            status=403
        )
    complaint = get_object_or_404(Complaint, id=id)
    complaint.status = "resolved"
    complaint.save()
    return Response({"message": "Resolved"})
@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def delete_user_api(request,id):
    user=get_object_or_404(User,id=id)
    user.delete()
    return Response({"message":"Deleted Successfully"})
def raise_complaint(request):
    return render(request,"raisecomplaint.html")

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def raise_complaint_api(request):
    serializer = ComplaintSerializer(data=request.data)
    if serializer.is_valid():
        complaint=Complaint.objects.create(
            user=request.user,
            title=serializer.validated_data["title"],
            description=serializer.validated_data["description"],
            room_no=serializer.validated_data["room_no"],
            
        )
        return Response(ComplaintSerializer(complaint).data, status=201)
    return Response(serializer.errors, status=400)

def my_complaints_page(request):
    return render(request, "mycomplaints.html")


# @login_required -->session login
def update_complaint(request, id):
    complaint = get_object_or_404(Complaint, id=id)
    return render(
        request,
        "updateraisecomplaint.html",
        {"complaint": complaint}
    )
    
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_complaint_api(request, id):
    complaint = get_object_or_404(Complaint, id=id, user=request.user)
    serializer = ComplaintSerializer(
        complaint,
        data=request.data,
        partial=True
    )
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Complaint updated successfully"},
            status=200
        )

    return Response(serializer.errors, status=400)    
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_complaint(request, id):
        complaint = Complaint.objects.get(id=id, user=request.user)
        complaint.delete()
        return Response(
           {"message": "Complaint is Going to Delete Permently!"},
        status=200
        )
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def my_complaints(request):
    complaints = Complaint.objects.filter(user=request.user)  
    serializer = ComplaintSerializer(complaints, many=True)
    return Response(serializer.data,status=200)
