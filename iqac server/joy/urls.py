"""joy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static
from . import views
from django.conf import settings  
# from .views import DepartmentViewSet, IqacCategoryViewSet, IqacCategoryTypeViewSet, IqacFdpViewSet, IqacFdWorkshopViewSet, IqacFdResourcepersonViewSet, IqacStatusViewSet, IqacTablemappingViewSet, IqacTargetViewSet, IqacTargetDetailsViewSet, StaffViewSet,OndutyViewSet,login
# Create a router and register viewsets with it
router = routers.DefaultRouter()
router.register(r'departments', views.DepartmentViewSet)
router.register(r'iqac-categories', views.IqacCategoryViewSet)
router.register(r'iqac-category-types', views.IqacCategoryTypeViewSet)
router.register(r'onduty', views.OndutyViewSet)
router.register(r'iqac-fdps', views.IqacFdpViewSet)
router.register(r'iqac-fd-workshops', views.IqacFdWorkshopViewSet)
router.register(r'iqac-fd-resourcepersons', views.IqacFdResourcepersonViewSet)
router.register(r'iqac-statuses', views.IqacStatusViewSet)
router.register(r'iqac-tablemappings', views.IqacTablemappingViewSet)
router.register(r'iqac-targets', views.IqacTargetViewSet)
router.register(r'iqac-target-details', views.IqacTargetDetailsViewSet)
router.register(r'staff', views.StaffViewSet)
router.register(r'publications', views.PublicationViewSet)
router.register(r'bookchapters', views.BookChapterViewSet)
router.register(r'consultancyapplications', views.ConsultancyApplicationViewSet)
router.register(r'innovations', views.InnovationViewSet)
router.register(r'researchproposals', views.ResearchProposalViewSet)
router.register(r'studentparticipations', views.StudentParticipationViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'outreachactivities', views.OutreachActivityViewSet)
router.register(r'occcourses', views.OCCCourseViewSet)
router.register(r'stud', views.StudViewSet)
router.register(r'mentors', views.MentorViewSet)
router.register(r'mentorships', views.MentorshipViewSet)
router.register(r'conferenceonduty', views.conferenceondutyViewSet)
router.register(r'pdfregister', views.phdViewSet)
router.register(r'onlinecourse', views.CourseViewSet)
router.register(r'iqacworkshops', views.IqacworkshopViewSet)
router.register(r'iqacresourcepersons', views.IqacresourcepersonViewSet)
router.register(r'iqaconlines', views.IqaconlineViewSet)
router.register(r'iqaconferences', views.IqaconferenceViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('login/', views.login, name='login'),
    path('get_staff_in_department/', views.get_staff_in_department, name='get_staff_in_department'),
    path('departments/<int:pk>/', views.DepartmentDetailAPIView.as_view(), name='department-detail'),
    path('reject-fdp/<int:onduty_id>/', views.reject_fdp, name='reject_fdp'),
    # path('export-department-wise/', views.export_department_wise, name='export_department_wise'),
    path('jiqac-fdps/', views.iqacfdp_list, name='iqacfdp_list'),
    path('jiqac-work/', views.iqacwork_list, name='iqacwork_list'),
    path('jiqac-resource/', views.iqacresource_list, name='iqacresource_list'),
    path('jiqac-online/', views.iqaconline_list, name='iqaconline_list'),
    path('jiqac-conference/', views.iqaconference_list, name='iqaconference_list'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
