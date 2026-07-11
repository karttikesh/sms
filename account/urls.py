from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/super/admin/", views.super_admin_dashboard, name="super_admin_dashboard"),
    path("dashboard/admin/", views.admin_dashboard, name="admin_dashboard"),
    path("dashboard/principal/", views.principal_dashboard, name="principal_dashboard"),
    path("dashboard/accountant/", views.accountant_dashboard, name="accountant_dashboard"),
    path("dashboard/teacher/", views.teacher_dashboard, name="teacher_dashboard"),
    path("dashboard/class/teacher/", views.class_teacher_dashboard, name="class_teacher_dashboard"),
    path("dashboard/transporter/", views.transporter_dashboard, name="transporter_dashboard"),
    path("dashboard/cundoctor/", views.cundoctor_dashboard, name="cundoctor_dashboard"),
    path("dashboard/parent/", views.parent_dashboard, name="parent_dashboard"),
]