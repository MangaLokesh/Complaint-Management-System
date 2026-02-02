from django.urls import path
from . import views

urlpatterns = [
    path("raisecomplaint/", views.raise_complaint,name="raise_complaint"),
    path("my_complaints_page/", views.my_complaints_page,name="my_complaints_page"),
    path("my_complaints/",views.my_complaints,name="my_complaints"),
     path("delete/<int:id>/", views.delete_complaint, name="delete_complaint"),
     path("update/<int:id>/", views.update_complaint, name="update_complaint"),
     path("resolvecomplaintapi/<int:id>/",views.resolve_complaint_api,name="resove_complaint_api"),
     path("updatecomplaintapi/<int:id>/",views.update_complaint_api,name="update_complaint_api"),
     path("deleteuserapi/<int:id>/",views.delete_user_api,name="delete_user_api"),
    path("raisecomplaintsapi/",views.raise_complaint_api,name="raise_complaint_api"),
    # path("admin/complaints/", views.all_complaints_admin),
]
