from django.contrib import admin
from .models import (
    Department, IqacCategory, IqacCategoryType, OnDuty, IqacFdp, 
    Iqacworkshop, Iqacresourceperson, IqacStatus, IqacTablemapping, 
    IqacTarget, IqacTargetDetails, Staff, Publication, BookChapter, 
    ConsultancyApplication, Innovation, ResearchProposal, StudentParticipation, 
    Student, outreachActivity, OCCCourse, 
    ConferenceOnDuty,  Course
)

# Register models with the admin site
admin.site.register(Department)
admin.site.register(IqacCategory)
admin.site.register(IqacCategoryType)
admin.site.register(OnDuty)
admin.site.register(IqacFdp)
admin.site.register(Iqacworkshop)
admin.site.register(Iqacresourceperson)
admin.site.register(IqacStatus)
admin.site.register(IqacTablemapping)
admin.site.register(IqacTarget)
admin.site.register(IqacTargetDetails)
admin.site.register(Staff)
admin.site.register(Publication)
admin.site.register(BookChapter)
admin.site.register(ConsultancyApplication)
admin.site.register(Innovation)
admin.site.register(ResearchProposal)
admin.site.register(StudentParticipation)
admin.site.register(Student)
admin.site.register(outreachActivity)
admin.site.register(OCCCourse)
admin.site.register(ConferenceOnDuty)
admin.site.register(Course)

