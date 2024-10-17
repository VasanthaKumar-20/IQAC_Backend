from rest_framework import viewsets,permissions
from .models import Department, IqacCategory, IqacCategoryType, IqacFdp,ondutyFdResourceperson,ondutyWorkshop, IqacStatus, IqacTablemapping, IqacTarget, IqacTargetDetails, Staff,OnDuty,Publication,BookChapter, ConsultancyApplication, Innovation,ResearchProposal, StudentParticipation, Student, outreachActivity,OCCCourse,Students, Mentor, Mentorship,PhDRegistration,ConferenceOnDuty,Course,Iqacworkshop, Iqacresourceperson, Iqaconline, Iqaconference
from .serializers import DepartmentSerializer, IqacCategorySerializer, IqacCategoryTypeSerializer, IqacFdpSerializer, IqacFdWorkshopSerializer, IqacFdResourcepersonSerializer, IqacStatusSerializer, IqacTablemappingSerializer, IqacTargetSerializer, IqacTargetDetailsSerializer, StaffSerializer,ondutySerializer,PublicationSerializer, BookChapterSerializer, ConsultancyApplicationSerializer,InnovationSerializer, ResearchProposalSerializer, StudentParticipationSerializer,StudentSerializer, OutreachActivitySerializer, OCCCourseSerializer,StudentsSerializer, MentorSerializer, MentorshipSerializer,phdSerializer,conferenceondutySerializer,CourseSerializer,IqacworkshopSerializer, IqacresourcepersonSerializer, IqaconlineSerializer, IqaconferenceSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .models import Staff ,Department
import json
from rest_framework import generics
# import pandas as pd
from io import BytesIO
from django.apps import apps
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils.dateparse import parse_datetime
from .models import OnDuty, IqacFdp, Staff, Department, IqacTarget, IqacTargetDetails, Iqacworkshop
# from openpyxl import load_workbook
# from openpyxl.worksheet.hyperlink import Hyperlink
# from openpyxl.styles import Font
def iqacfdp_list(request):
     department_id = request.GET.get('department')
    
     if department_id:
        try:
            iqacfdps = IqacFdp.objects.filter(onduty__department=department_id)
            data = list(iqacfdps.values())  # Serialize queryset to JSON-serializable format
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
     else:
        return JsonResponse({'error': 'Department ID is required'}, status=400)
def iqacwork_list(request):
     department_id = request.GET.get('department')
    
     if department_id:
        try:
            iqacfdps = Iqacworkshop.objects.filter(onduty__department=department_id)
            data = list(iqacfdps.values())  # Serialize queryset to JSON-serializable format
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
     else:
        return JsonResponse({'error': 'Department ID is required'}, status=400)
def iqacresource_list(request):
     department_id = request.GET.get('department')
    
     if department_id:
        try:
            iqacfdps = Iqacresourceperson.objects.filter(onduty__department=department_id)
            data = list(iqacfdps.values())  # Serialize queryset to JSON-serializable format
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
     else:
        return JsonResponse({'error': 'Department ID is required'}, status=400)
def iqaconline_list(request):
     department_id = request.GET.get('department')
    
     if department_id:
        try:
            iqacfdps = Iqaconline.objects.filter(onduty__department=department_id)
            data = list(iqacfdps.values())  # Serialize queryset to JSON-serializable format
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
     else:
        return JsonResponse({'error': 'Department ID is required'}, status=400)
def iqaconference_list(request):
     department_id = request.GET.get('department')
    
     if department_id:
        try:
            iqacfdps = Iqaconference.objects.filter(onduty__department=department_id)
            data = list(iqacfdps.values())  # Serialize queryset to JSON-serializable format
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
     else:
        return JsonResponse({'error': 'Department ID is required'}, status=400)
@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        staffid = data.get('staffid')
        password = data.get('password')

        try:
            user = Staff.objects.get(staffid=staffid, password=password)
            
            if user.is_spoc:
                return JsonResponse({
                    'success': True,
                    'role': 'SPOC',
                    'staffid': user.staffid,
                    'staffno': user.staffno,
                    'department': user.department.deptid
                })
            elif user.is_hod:
                return JsonResponse({
                    'success': True,
                    'role': 'HOD',
                    'staffid': user.staffid,
                    'staffno': user.staffno,
                    'department': user.department.deptid
                })
            elif user.is_placement_coordinator:
                return JsonResponse({
                    'success': True,
                    'role': 'PlacementCoordinator',
                    'staffid': user.staffid,
                    'staffno': user.staffno
                })
            elif user.is_event_coordinator:
                return JsonResponse({
                    'success': True,
                    'role': 'EventCoordinator',
                    'staffid': user.staffid,
                    'staffno': user.staffno
                })
            else:
                return JsonResponse({
                    'success': True,
                    'role': 'Faculty',
                    'staffid': user.staffid,
                    'staffno': user.staffno
                })

        except Staff.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Invalid credentials'}, status=400)

    else:
        return JsonResponse({'success': False, 'message': 'Method Not Allowed'}, status=405)
# @csrf_exempt
# def login(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         staffid = data.get('staffid')
#         password = data.get('password')

#         # Query the Staff model to check if staffid and password match
#         try:
#             user = Staff.objects.get(staffid=staffid, password=password)
#             department_name = user.department.deptname
#             # Check user permissions to determine if SPOC or HOD
#             if user.is_spoc:
#                 # User is SPOC
#                 return JsonResponse({'success': True, 'role': 'SPOC', 'staffid': user.staffid, 'staffno': user.staffno,'department':user.department.deptid})
#             elif user.is_hod:
#                 # User is HOD
#                 return JsonResponse({'success': True, 'role': 'HOD', 'staffid': user.staffid, 'staffno': user.staffno, 'department':user.department.deptid})
#             else:
#                 # Regular faculty member
#                 return JsonResponse({'success': True, 'role': 'Faculty', 'staffid': user.staffid, 'staffno': user.staffno})
#         except Staff.DoesNotExist:
#             # Authentication failed
#             return JsonResponse({'success': False, 'message': 'Invalid credentials'}, status=400)
#     else:
#         # Return a 405 Method Not Allowed for GET requests
#         return JsonResponse({'success': False, 'message': 'Method Not Allowed'}, status=405)

# def login(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         staffid = data.get('staffid')
#         password = data.get('password')

#         # Query the Staff model to check if staffid and password match
#         try:
#             user = Staff.objects.get(staffid=staffid, password=password)
#             department_name = user.department.deptname
#             # Check user permissions to determine if SPOC or HOD
#             if user.is_spoc:
#                 # User is SPOC
#                 return JsonResponse({'success': True, 'role': 'SPOC', 'staffid': user.staffid})
#             elif user.is_hod:
#                 # User is HOD
#                 return JsonResponse({'success': True, 'role': 'HOD', 'staffid': user.staffid})
#             else:
#                 # Regular faculty member
#                 return JsonResponse({'success': True, 'role': 'Faculty', 'staffid': user.staffid})
#         except Staff.DoesNotExist:
#             # Authentication failed
#             return JsonResponse({'success': False, 'message': 'Invalid credentials'}, status=400)
#     else:
#         # Return a 405 Method Not Allowed for GET requests
#         return JsonResponse({'success': False, 'message': 'Method Not Allowed'}, status=405)
@csrf_exempt  # Disable CSRF protection for this view (for demonstration purposes only; use proper CSRF protection in production)
def reject_fdp(request, onduty_id):
    if request.method == 'PATCH':
        remarks = request.POST.get('reject_remarks', '')  # Get rejection remarks from request
        try:
            instance = OnDuty.objects.get(ondutyid=onduty_id)
            instance.is_rejected = True
            instance.reject_remarks = remarks
            instance.save()
            return JsonResponse({'message': 'FDP rejected successfully.'})
        except OnDuty.DoesNotExist:
            return JsonResponse({'error': 'FDP not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)
def get_staff_in_department(request, department_code):
    try:
        # Get the department object with the given department code
        department = Department.objects.get(deptcode=department_code)
        
        # Filter staff members by department
        staff = Staff.objects.filter(department=department)
        
        # Serialize the data
        data = [
            {
                'staffno': member.staffno,
                'staffname': member.staffname,
                'designation': member.designation,
                'photo': member.photo.url if member.photo else None
            } 
            for member in staff
        ]
        
        # Return JSON response
        return JsonResponse(data, safe=False)
    
    except Department.DoesNotExist:
        return JsonResponse({'error': 'Department not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
# @csrf_exempt
# def login(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         staffid = data.get('staffid')
#         password = data.get('password')

#         # Query the Staff model to check if staffid and password match
#         try:
#             user = Staff.objects.get(staffid=staffid, password=password)
#             # User authenticated successfully
#             return JsonResponse({'success': True, 'staffid': user.staffid})
#         except Staff.DoesNotExist:
#             # Authentication failed
#             return JsonResponse({'success': False, 'message': 'Invalid credentials'}, status=400)
#     else:
#         # Return a 405 Method Not Allowed for GET requests
#         return JsonResponse({'success': False, 'message': 'Method Not Allowed'}, status=405)

# def export_department_wise(request):
#     # Get the department ID from query parameters
#     department_id = request.GET.get('deptid')

#     # Initialize a BytesIO buffer to hold the Excel file
#     output = BytesIO()

#     # Create an Excel writer object
#     with pd.ExcelWriter(output, engine='openpyxl') as writer:
#         sheets_written = False
        
#         # Get the specific department based on the ID
#         if department_id:
#             try:
#                 department = Department.objects.get(deptid=department_id)
#                 departments = [department]
#             except Department.DoesNotExist:
#                 departments = []
#         else:
#             # Get all departments if no specific ID is provided
#             departments = Department.objects.all()
        
#         # If there are no departments, add a default sheet
#         if not departments:
#             df = pd.DataFrame({"Message": ["No departments available"]})
#             df.to_excel(writer, index=False, sheet_name="NoDepartments")
#             sheets_written = True
#         else:
#             # Iterate over all departments
#             for department in departments:
#                 department_name = department.deptname
#                 try:
#                     # Query all related data for this department
#                     related_models = [model for model in apps.get_models() if hasattr(model, 'department')]
                    
#                     # Iterate over each related model
#                     for model in related_models:
#                         queryset = model.objects.filter(department=department)
                        
#                         # Convert queryset to DataFrame
#                         df = pd.DataFrame(list(queryset.values()))
                        
#                         # Write DataFrame to a new sheet in the Excel file
#                         if not df.empty:
#                             sheet_name = f'{department_name}_{model.__name__}'[:31]  # Excel sheet names have a max length of 31 characters
#                             df.to_excel(writer, index=False, sheet_name=sheet_name)
                            
#                             # Access the workbook and sheet
#                             workbook = writer.book
#                             sheet = workbook[sheet_name]
                            
#                             # Add hyperlinks to FileField URLs
#                             for row_num in range(2, len(df) + 2):  # Starting from row 2 to skip header
#                                 for col_num, col_name in enumerate(df.columns):
#                                     cell_value = df.iloc[row_num - 2, col_num]
#                                     # Check if the cell value is a URL
#                                     if isinstance(cell_value, str) and cell_value.startswith('http'):
#                                         cell = sheet.cell(row=row_num, column=col_num + 1)
#                                         cell.hyperlink = Hyperlink(cell_value, "Download")
#                                         cell.style = 'Hyperlink'
                            
#                             sheets_written = True  # Update the flag
#                         else:
#                             print(f"Empty DataFrame for {department_name} - {model.__name__}")
#                 except Exception as e:
#                     print(f"Error exporting department {department_name}: {e}")

#         # If no sheets were written, create a default sheet
#         if not sheets_written:
#             df = pd.DataFrame({"Message": ["No data available"]})
#             df.to_excel(writer, index=False, sheet_name="NoData")

#     # Ensure the buffer is rewound to the beginning
#     output.seek(0)
    
#     # Create HTTP response with the Excel file
#     response = HttpResponse(output.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
#     response['Content-Disposition'] = 'attachment; filename="department_wise_data.xlsx"'
#     return response
# def export_department_wise(request):
#     # Get the department ID from query parameters
#     department_id = request.GET.get('deptid')

#     # Initialize a BytesIO buffer to hold the Excel file
#     output = BytesIO()

#     # Create an Excel writer object
#     with pd.ExcelWriter(output, engine='openpyxl') as writer:
#         sheets_written = False
        
#         # Get the specific department based on the ID
#         if department_id:
#             try:
#                 department = Department.objects.get(deptid=department_id)
#                 departments = [department]
#             except Department.DoesNotExist:
#                 departments = []
#         else:
#             # Get all departments if no specific ID is provided
#             departments = Department.objects.all()
        
#         # If there are no departments, add a default sheet
#         if not departments:
#             df = pd.DataFrame({"Message": ["No departments available"]})
#             df.to_excel(writer, index=False, sheet_name="NoDepartments")
#             sheets_written = True
#         else:
#             # Iterate over all departments
#             for department in departments:
#                 department_name = department.deptname
#                 try:
#                     # Query all related data for this department
#                     related_models = [model for model in apps.get_models() if hasattr(model, 'department')]
                    
#                     # Iterate over each related model
#                     for model in related_models:
#                         queryset = model.objects.filter(department=department)
                        
#                         # Convert queryset to DataFrame
#                         df = pd.DataFrame(list(queryset.values()))
                        
#                         # Write DataFrame to a new sheet in the Excel file
#                         if not df.empty:
#                             sheet_name = f'{department_name}_{model.__name__}'[:31]  # Excel sheet names have a max length of 31 characters
#                             df.to_excel(writer, index=False, sheet_name=sheet_name)
                            
#                             # Access the workbook and sheet
#                             workbook = writer.book
#                             sheet = workbook[sheet_name]
                            
#                             # Add hyperlinks to FileField URLs
#                             for row_num in range(2, len(df) + 2):  # Starting from row 2 to skip header
#                                 for col_num, col_name in enumerate(df.columns):
#                                     cell_value = df.iloc[row_num - 2, col_num]
#                                     # Check if the cell value is a URL
#                                     if isinstance(cell_value, str) and cell_value.startswith('http'):
#                                         cell = sheet.cell(row=row_num, column=col_num + 1)
#                                         cell.hyperlink = Hyperlink(cell_value, "Download")
#                                         cell.font = Font(color="0000FF", underline="single")  # Style as hyperlink
                            
#                             sheets_written = True  # Update the flag
#                         else:
#                             print(f"Empty DataFrame for {department_name} - {model.__name__}")
#                 except Exception as e:
#                     print(f"Error exporting department {department_name}: {e}")

#         # If no sheets were written, create a default sheet
#         if not sheets_written:
#             df = pd.DataFrame({"Message": ["No data available"]})
#             df.to_excel(writer, index=False, sheet_name="NoData")

#     # Ensure the buffer is rewound to the beginning
#     output.seek(0)
    
#     # Create HTTP response with the Excel file
#     response = HttpResponse(output.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
#     response['Content-Disposition'] = 'attachment; filename="department_wise_data.xlsx"'
#     return response
    
class DepartmentDetailAPIView(generics.RetrieveAPIView):
    serializer_class = DepartmentSerializer
    def get_queryset(self):
        queryset = Department.objects.all()
        deptcode = self.request.query_params.get('deptcode', None)
        deptname = self.request.query_params.get('deptname', None)

        if deptcode:
            queryset = queryset.filter(deptcode=deptcode)
        if deptname:
            queryset = queryset.filter(deptname__icontains=deptname)
        
        return queryse

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    def get_queryset(self):
        queryset = Course.objects.all()
        department_id = self.request.query_params.get('department', None)

        if department_id is not None:
            try:
                # Convert department_id to integer
                department_id = int(department_id)
                queryset = queryset.filter(department_id=department_id)
            except ValueError:
                # Handle case where department_id is not a valid integer
                queryset = queryset.none()
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
class IqacCategoryViewSet(viewsets.ModelViewSet):
    queryset = IqacCategory.objects.all()
    serializer_class = IqacCategorySerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        mid = self.request.query_params.get('mid')
        if mid:
            queryset = queryset.filter(mid=mid)
        return queryset
class IqacCategoryTypeViewSet(viewsets.ModelViewSet):
    queryset = IqacCategoryType.objects.all()
    serializer_class = IqacCategoryTypeSerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        mid = self.request.query_params.get('mid')
        if mid:
            queryset = queryset.filter(mid=mid)
        return queryset
class OndutyViewSet(viewsets.ModelViewSet):
    queryset = OnDuty.objects.all()
    serializer_class = ondutySerializer
    def get_queryset(self):
        queryset = OnDuty.objects.all()
        department = self.request.query_params.get('department', None)
        
        if department is not None:
            queryset = queryset.filter(department_id=department)
        
        return queryset
class IqacFdpViewSet(viewsets.ModelViewSet):
    queryset = IqacFdp.objects.all()
    serializer_class = IqacFdpSerializer
    
class IqacFdWorkshopViewSet(viewsets.ModelViewSet):
    queryset = ondutyWorkshop.objects.all()
    serializer_class = IqacFdWorkshopSerializer
    def get_queryset(self):
        queryset = ondutyWorkshop.objects.all()
        department_id = self.request.query_params.get('department', None)

        if department_id is not None:
            try:
                # Convert department_id to integer
                department_id = int(department_id)
                queryset = queryset.filter(department_id=department_id)
            except ValueError:
                # Handle case where department_id is not a valid integer
                queryset = queryset.none()

        return queryset
class IqacFdResourcepersonViewSet(viewsets.ModelViewSet):
    queryset = ondutyFdResourceperson.objects.all()
    serializer_class = IqacFdResourcepersonSerializer
    def get_queryset(self):
        queryset = ondutyFdResourceperson.objects.all()
        department_id = self.request.query_params.get('department', None)

        if department_id is not None:
            try:
                # Convert department_id to integer
                department_id = int(department_id)
                queryset = queryset.filter(department_id=department_id)
            except ValueError:
                # Handle case where department_id is not a valid integer
                queryset = queryset.none()
class IqacworkshopViewSet(viewsets.ModelViewSet):
    queryset = Iqacworkshop.objects.all()
    serializer_class = IqacworkshopSerializer

class IqacresourcepersonViewSet(viewsets.ModelViewSet):
    queryset = Iqacresourceperson.objects.all()
    serializer_class = IqacresourcepersonSerializer

class IqaconlineViewSet(viewsets.ModelViewSet):
    queryset = Iqaconline.objects.all()
    serializer_class = IqaconlineSerializer

class IqaconferenceViewSet(viewsets.ModelViewSet):
    queryset = Iqaconference.objects.all()
    serializer_class = IqaconferenceSerializer
class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    def get_queryset(self):
        queryset = Publication.objects.all()
        department_id = self.request.query_params.get('department', None)

        if department_id is not None:
            try:
                # Convert department_id to integer
                department_id = int(department_id)
                queryset = queryset.filter(department_id=department_id)
            except ValueError:
                # Handle case where department_id is not a valid integer
                queryset = queryset.none()

        return queryset

class BookChapterViewSet(viewsets.ModelViewSet):
    queryset = BookChapter.objects.all()
    serializer_class = BookChapterSerializer
    def get_queryset(self):
        queryset = BookChapter.objects.all()
        department_id = self.request.query_params.get('department', None)

        if department_id is not None:
            try:
                # Convert department_id to integer
                department_id = int(department_id)
                queryset = queryset.filter(department_id=department_id)
            except ValueError:
                # Handle case where department_id is not a valid integer
                queryset = queryset.none()

        return queryset
    def get_bookchapters(request):
        is_approved_str = request.GET.get('is_approved', 'true')
        is_approved = is_approved_str.lower() == 'true'  # Convert to boolean
        chapters = BookChapter.objects.filter(is_approved=is_approved)
        data = list(chapters.values())
        return JsonResponse(data, safe=False)
class ConsultancyApplicationViewSet(viewsets.ModelViewSet):
    queryset = ConsultancyApplication.objects.all()
    serializer_class = ConsultancyApplicationSerializer
    def get_queryset(self):
        queryset = ConsultancyApplication.objects.all()
        department_id = self.request.query_params.get('department', None)

        if department_id is not None:
            try:
                # Convert department_id to integer
                department_id = int(department_id)
                queryset = queryset.filter(department_id=department_id)
            except ValueError:
                # Handle case where department_id is not a valid integer
                queryset = queryset.none()

        return queryset

class InnovationViewSet(viewsets.ModelViewSet):
    queryset = Innovation.objects.all()
    serializer_class = InnovationSerializer
    def get_queryset(self):
        queryset = Innovation.objects.all()
        department_id = self.request.query_params.get('department', None)

        if department_id is not None:
            try:
                # Convert department_id to integer
                department_id = int(department_id)
                queryset = queryset.filter(department_id=department_id)
            except ValueError:
                # Handle case where department_id is not a valid integer
                queryset = queryset.none()

        return queryset

class ResearchProposalViewSet(viewsets.ModelViewSet):
    queryset = ResearchProposal.objects.all()
    serializer_class = ResearchProposalSerializer
    def get_queryset(self):
        queryset = ResearchProposal.objects.all()
        department_id = self.request.query_params.get('department', None)

        if department_id is not None:
            try:
                # Convert department_id to integer
                department_id = int(department_id)
                queryset = queryset.filter(department_id=department_id)
            except ValueError:
                # Handle case where department_id is not a valid integer
                queryset = queryset.none()

        return queryset

class conferenceondutyViewSet(viewsets.ModelViewSet):
    queryset = ConferenceOnDuty.objects.all()
    serializer_class = conferenceondutySerializer
    def get_queryset(self):
        queryset = ConferenceOnDuty.objects.all()
        department_id = self.request.query_params.get('department', None)

        if department_id is not None:
            try:
                # Convert department_id to integer
                department_id = int(department_id)
                queryset = queryset.filter(department_id=department_id)
            except ValueError:
                # Handle case where department_id is not a valid integer
                queryset = queryset.none()

        return queryset


class phdViewSet(viewsets.ModelViewSet):
    queryset = PhDRegistration.objects.all()
    serializer_class = phdSerializer
    def get_queryset(self):
        queryset = PhDRegistration.objects.all()
        department_id = self.request.query_params.get('department', None)

        if department_id is not None:
            try:
                # Convert department_id to integer
                department_id = int(department_id)
                queryset = queryset.filter(department_id=department_id)
            except ValueError:
                # Handle case where department_id is not a valid integer
                queryset = queryset.none()

        return queryset
class StudentParticipationViewSet(viewsets.ModelViewSet):
    queryset = StudentParticipation.objects.all()
    serializer_class = StudentParticipationSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class OutreachActivityViewSet(viewsets.ModelViewSet):
    queryset = outreachActivity.objects.all()
    serializer_class = OutreachActivitySerializer

class OCCCourseViewSet(viewsets.ModelViewSet):
    queryset = OCCCourse.objects.all()
    serializer_class = OCCCourseSerializer

class IqacStatusViewSet(viewsets.ModelViewSet):
    queryset = IqacStatus.objects.all()
    serializer_class = IqacStatusSerializer

class IqacTablemappingViewSet(viewsets.ModelViewSet):
    queryset = IqacTablemapping.objects.all()
    serializer_class = IqacTablemappingSerializer

class IqacTargetViewSet(viewsets.ModelViewSet):
    queryset = IqacTarget.objects.all()
    serializer_class = IqacTargetSerializer
    def get_queryset(self):
        queryset = IqacTarget.objects.all()
        department_id = self.request.query_params.get('deptid', None)

        if department_id is not None:
            try:
                # Convert department_id to integer
                department_id = int(department_id)
                queryset = queryset.filter(deptid=department_id)
            except ValueError:
                # Handle case where department_id is not a valid integer
                queryset = queryset.none()

        return queryset

class IqacTargetDetailsViewSet(viewsets.ModelViewSet):
    queryset = IqacTargetDetails.objects.all()
    serializer_class = IqacTargetDetailsSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    def get_queryset(self):
        queryset = Staff.objects.all()
        department_id = self.request.query_params.get('department', None)

        if department_id is not None:
            try:
                # Convert department_id to integer
                department_id = int(department_id)
                queryset = queryset.filter(department_id=department_id)
            except ValueError:
                # Handle case where department_id is not a valid integer
                queryset = queryset.none()

        return queryset
class StudViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class MentorViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

class MentorshipViewSet(viewsets.ModelViewSet):
    queryset = Mentorship.objects.all()
    serializer_class = MentorshipSerializer
    permission_classes = []  # No specific permissions required

    def get_queryset(self):
        mentor_id = self.request.query_params.get('mentor')
        if mentor_id:
            return Mentorship.objects.filter(mentor_id=mentor_id)
        return Mentorship.objects.none()

    def perform_create(self, serializer):
        serializer.save()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

