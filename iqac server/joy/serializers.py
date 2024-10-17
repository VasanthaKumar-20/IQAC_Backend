from rest_framework import serializers
from .models import Department,IqacCategory,IqacCategoryType,IqacFdp,ondutyFdResourceperson,ondutyWorkshop,IqacStatus,IqacTablemapping,IqacTarget,IqacTargetDetails,Staff,OnDuty,Publication,BookChapter,ConsultancyApplication,Innovation,ResearchProposal,StudentParticipation,studentevent,facultyevents,ConferencePaper,outreachActivity,Student,outreachActivity,OCCCourse,Students, Mentor, Mentorship,PhDRegistration,ConferenceOnDuty,Course,Iqacworkshop, Iqacresourceperson, Iqaconline, Iqaconference
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
class DepartmentSerializer(serializers.ModelSerializer):
    staff_set = StaffSerializer(many=True, read_only=True)
    class Meta:
        model = Department
        fields = ['deptid', 'deptcode', 'deptname','staff_set']
class IqacCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IqacCategory
        fields = ['mid', 'a_name', 'status', 'sysdatetime']
class IqacCategoryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IqacCategoryType
        fields = ['cid', 'mid', 'sname', 'type', 'status', 'sysdatetime']
class ondutySerializer(serializers.ModelSerializer):
    class Meta:
        model = OnDuty
        fields = '__all__'
class IqacFdpSerializer(serializers.ModelSerializer):
    class Meta:
        model = IqacFdp
        fields = '__all__'
class IqacFdWorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = ondutyWorkshop
        fields = '__all__'
class IqacFdResourcepersonSerializer(serializers.ModelSerializer):
    class Meta:
        model =ondutyFdResourceperson 
        fields = '__all__'
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
class IqacworkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iqacworkshop
        fields = '__all__'
class IqacresourcepersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iqacresourceperson
        fields = '__all__'

class IqaconlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iqaconline
        fields = '__all__'

class IqaconferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iqaconference
        fields = '__all__'
class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'
class BookChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookChapter
        fields = '__all__'
class ConsultancyApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultancyApplication
        fields = '__all__'
class InnovationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Innovation
        fields = '__all__'
class ResearchProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchProposal
        fields = '__all__'
class phdSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhDRegistration
        fields = '__all__'
class conferenceondutySerializer(serializers.ModelSerializer):
    class Meta:
        model = ConferenceOnDuty
        fields = '__all__'
class StudentParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentParticipation
        fields = '__all__'
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
class OutreachActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = outreachActivity
        fields = '__all__'
class OCCCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OCCCourse
        fields = '__all__'
class IqacStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = IqacStatus
        fields = '__all__'
class IqacTablemappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = IqacTablemapping
        fields = '__all__'
class IqacTargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = IqacTarget
        fields = '__all__'
class IqacTargetDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IqacTargetDetails
        fields = '__all__'
class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'

class MentorshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentorship
        fields = '__all__'
