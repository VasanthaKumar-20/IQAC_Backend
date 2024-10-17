from django.db import models
import os
from django.db.models.signals import post_save
from django.dispatch import receiver

class Department(models.Model):
    deptcode = models.CharField(db_column='DeptCode', max_length=2, blank=True, null=True)  # Field name made lowercase.
    deptid = models.AutoField(db_column='DeptID',primary_key=True)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=150, blank=True, null=True)  # Field name made lowercase.
class Staff(models.Model):  
    staffno = models.AutoField(db_column='StaffID', primary_key=True)  # Field name made lowercase.
    staffname = models.CharField(db_column='StaffName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department') # Field name made lowercase.
    designation = models.CharField(db_column='Designation', max_length=2, blank=True, null=True)  # Field name made lowercase.
    mdept = models.CharField(db_column='MDept', max_length=2, blank=True, null=True)  # Field name made lowercase.
    staffid= models.CharField(db_column='StaffNo',max_length=6,blank=True,null=True)
    password = models.CharField(db_column='Password',max_length=7,blank=True,null=True)
    photo = models.FileField(db_column='photo',upload_to='photo/', null=True,blank=True)
    is_spoc = models.BooleanField(default=False)
    is_hod = models.BooleanField(default=False)
    is_placement_coordinator = models.BooleanField(default=False)
    is_event_coordinator = models.BooleanField(default=False)
class IqacCategory(models.Model):
    mid = models.AutoField(db_column='MID', primary_key=True)  # Field name made lowercase.
    a_name = models.CharField(db_column='A_NAME', max_length=100)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1 , blank=True, null=True)  # Field name made lowercase.
    sysdatetime = models.DateTimeField(db_column='SYSDATETIME',auto_now_add=True)
class IqacCategoryType(models.Model):
    cid = models.AutoField(db_column='CID', primary_key=True)  # Field name made lowercase.
    mid = models.IntegerField(db_column='MID')  # Field name made lowercase.
    sname = models.CharField(db_column='SNAME', max_length=100)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=1)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1)  # Field name made lowercase.
    sysdatetime = models.DateTimeField(db_column='SYSDATETIME', blank=True, null=True)  # Field name made lowercase.
class IqacStatus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=2)  # Field name made lowercase.
    statusname = models.CharField(db_column='StatusName', max_length=30)  # Field name made lowercase.
class IqacTablemapping(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mid = models.ForeignKey(IqacCategory, models.DO_NOTHING, db_column='MID')  # Field name made lowercase.
    cid = models.ForeignKey(IqacCategoryType, models.DO_NOTHING, db_column='CID')  # Field name made lowercase.
    tablename = models.CharField(db_column='TableName', max_length=50, blank=True, null=True)  # Field name made lowercase.
class IqacTarget(models.Model):
    qid = models.AutoField(db_column='QID', primary_key=True)  # Field name made lowercase.
    deptid = models.ForeignKey(Department, models.DO_NOTHING,db_column='DEPTID')  # Field name made lowercase.
    cid = models.ForeignKey(IqacCategoryType, models.DO_NOTHING,db_column='CID')  # Field name made lowercase.
    admid = models.SmallIntegerField(db_column='ADMID',blank=True, null=True)  # Field name made lowercase.
    target = models.SmallIntegerField(db_column='TARGET')  # Field name made lowercase.
    targetcal = models.IntegerField(db_column='TARGETCAL', blank=True, null=True)  # Field name made lowercase.
    student = models.IntegerField(db_column='STUDENT', blank=True, null=True)  # Field name made lowercase.
    faculty = models.IntegerField(db_column='FACULTY', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1,blank=True, null=True)  # Field name made lowercase.
    sdate = models.DateTimeField(db_column='SDATE', blank=True, null=True)  # Field name made lowercase.
    edate = models.DateTimeField(db_column='EDATE', blank=True, null=True)  # Field name made lowercase.
    sysdatetime = models.DateTimeField(db_column='SYSDATETIME', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey(Staff, models.DO_NOTHING, db_column='userid' , blank=True, null=True)  # Field name made lowercase.
    dhod = models.SmallIntegerField(db_column='DHOD', blank=True, null=True)  # Field name made lowercase.
class IqacTargetDetails(models.Model):
    dit = models.AutoField(db_column='DIT', primary_key=True,unique=True)  # Field name made lowercase.
    qid = models.ForeignKey(IqacTarget, models.DO_NOTHING,db_column='QID')
    department = models.ForeignKey(Department, related_name='targets', on_delete=models.CASCADE)
    faculty = models.ForeignKey(Staff, models.DO_NOTHING, db_column='faculty')  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sysdatetime = models.DateTimeField(db_column='SYSDATETIME', blank=True, null=True)  # Field name made lowercase.
    achieved_count = models.PositiveIntegerField(default=0)
    category_main = models.ForeignKey(IqacCategory,models.DO_NOTHING,db_column='category_main')
    category_type = models.ForeignKey(IqacCategoryType,models.DO_NOTHING,db_column='category_type')
    target_count = models.PositiveIntegerField()
    # def update_achieved_count(self):
    #     self.achieved_count = self.faculty.fdps.filter(is_achieved=True).count()
    #     self.save()

    # def __str__(self):
    #     return f"Target for {self.faculty} in {self.department}"
    def update_achieved_count_by_category(self, category_type_id):
        # Filter achieved items based on the specified category type
        self.achieved_count = self.faculty.fdps.filter(is_achieved=True, category_type_id=category_type_id).count()
        self.save()

    def __str__(self):
        return f"Target for {self.faculty} in {self.department}"
    # class Meta:
    #     managed = False
    #     db_table = 'IQAC_TARGET_DETAILS'



   
class OnDuty(models.Model):
    ondutyid = models.AutoField(db_column='OndutyID', primary_key=True)
    staffnos = models.ForeignKey(Staff, models.DO_NOTHING, db_column='FID')
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department')   # Field name made lowercase.
    fdptitle = models.CharField(db_column='FDPTitle', max_length=100)  # Field name made lowercase.
    venue = models.CharField(db_column='Venue', max_length=100)  # Field name made lowercase.
    sdate = models.DateField(db_column='Sdate')  # Field name made lowercase.
    edate = models.DateField(db_column='Edate')  # Field name made lowercase.
    noofdays = models.IntegerField(db_column='NoOfDays')  # Field name made lowercase.
    academicyear = models.CharField(db_column='AcademicYear', max_length=10)  # Field name made lowercase.
    sem = models.CharField(db_column='Sem', max_length=6)  # Field name made lowercase.
    programmetype = models.CharField(db_column='ProgrammeType', max_length=6) 
    is_approved = models.BooleanField(db_column='is_approved', default=False)
    createdtime = models.DateTimeField(db_column='CreatedTime', auto_now_add=True)  # Field name made lowercase.
    is_rejected = models.BooleanField(default=False)
    reject_remarks = models.TextField(blank=True, null=True)

    def approval_letter_path(self, filename):
        ext = filename.split('.')[-1]
        staff_id = self.staffnos.staffid
        staff_name = self.staffnos.staffname
        fdptitles = self.fdptitle
        modified_filename = f'{staff_id}_{staff_name}FDP_onduty_{fdptitles}.{ext}'
        # Uploads to 'approval_letter/department_staffid/<filename>'
        return f'2024-2025/{self.department.deptcode}/Faculty_Detail/FDP/onduty/approval_letter/{modified_filename}'

    def brochure_file_path(self, filename):
        ext = filename.split('.')[-1]
        staff_id = self.staffnos.staffid
        staff_name = self.staffnos.staffname
        fdptitles = self.fdptitle
        modified_filename = f'{staff_id}_{staff_name}FDP_onduty_{fdptitles}.{ext}'
        # Uploads to 'approval_letter/department_staffid/<filename>'
        return f'2024-2025/{self.department.deptcode}/Faculty_Detail/FDP/onduty/brochures/{modified_filename}'
    approval_letter = models.FileField(db_column='approval_letter', upload_to=approval_letter_path, null=True, blank=True)
    brochure_file = models.FileField(db_column='brochure_file', upload_to=brochure_file_path, null=True, blank=True)
class ondutyFdResourceperson(models.Model):
    ondutyid = models.AutoField(db_column='OndutyID', primary_key=True)
    staffnos = models.ForeignKey(Staff, models.DO_NOTHING, db_column='FID')
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department') 
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.
    topicdelivered = models.CharField(db_column='TopicDelivered', max_length=100)  # Field name made lowercase.
    sdate = models.DateTimeField(db_column='Sdate')  # Field name made lowercase.
    edate = models.DateTimeField(db_column='Edate')  # Field name made lowercase.
    members = models.CharField(db_column='Members', max_length=200)  # Field name made lowercase.
    venue = models.CharField(db_column='Venue', max_length=100)  # Field name made lowercase.
    is_approved = models.BooleanField(db_column='is_approved', default=False)
    is_approved_hod = models.BooleanField(default=False)
    createdtime = models.DateTimeField(db_column='CreatedTime', auto_now_add=True)  # Field name made lowercase.
    is_rejected = models.BooleanField(default=False)
    reject_remarks = models.TextField(blank=True, null=True)
    def approval_letter_path(self, filename):
        ext = filename.split('.')[-1]
        staff_id = self.staffnos.staffid
        staff_name = self.staffnos.staffname
        fdptitles = self.title
        modified_filename = f'{staff_id}_{staff_name}Resourceperson_onduty_{fdptitles}.{ext}'
        # Uploads to 'approval_letter/department_staffid/<filename>'
        return f'2024-2025/{self.department.deptcode}/Faculty_Detail/Resourceperson/onduty/approval_letter/{modified_filename}'

    def brochure_file_path(self, filename):
        ext = filename.split('.')[-1]
        staff_id = self.staffnos.staffid
        staff_name = self.staffnos.staffname
        fdptitles = self.title
        modified_filename = f'{staff_id}_{staff_name}FDP_onduty_{fdptitles}.{ext}'
        # Uploads to 'approval_letter/department_staffid/<filename>'
        return f'2024-2025/{self.department.deptcode}/Faculty_Detail/FDP/onduty/brochures/{modified_filename}'
    approval_letter = models.FileField(db_column='approval_letter', upload_to=approval_letter_path, null=True, blank=True)
    brochure_file = models.FileField(db_column='brochure_file', upload_to=brochure_file_path, null=True, blank=True)
class ondutyWorkshop(models.Model):
    ondutyid = models.AutoField(db_column='OndutyID', primary_key=True)
    staffnos = models.ForeignKey(Staff, models.DO_NOTHING, db_column='FID')
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.
    venue = models.CharField(db_column='Venue', max_length=100)  # Field name made lowercase.
    sdate = models.CharField(db_column='Sdate',max_length=100)  # Field name made lowercase.
    edate = models.CharField(db_column='Edate',max_length=100)  # Field name made lowercase.
    programmetype = models.CharField(db_column='ProgrammeType', max_length=100)  # Field name made lowercase.
    is_approved = models.BooleanField(db_column='is_approved', default=False)
    is_approved_hod = models.BooleanField(default=False)
    createdtime = models.DateTimeField(db_column='CreatedTime', auto_now_add=True)  # Field name made lowercase.
    is_rejected = models.BooleanField(default=False)
    reject_remarks = models.TextField(blank=True, null=True)
    def approval_letter_path(self, filename):
        ext = filename.split('.')[-1]
        staff_id = self.staffnos.staffid
        staff_name = self.staffnos.staffname
        fdptitles = self.title
        modified_filename = f'{staff_id}_{staff_name}Workshop_onduty_{fdptitles}.{ext}'
        # Uploads to 'approval_letter/department_staffid/<filename>'
        return f'2024-2025/{self.department.deptcode}/Faculty_Detail/Workshop/onduty/approval_letter/{modified_filename}'

    def brochure_file_path(self, filename):
        ext = filename.split('.')[-1]
        staff_id = self.staffnos.staffid
        staff_name = self.staffnos.staffname
        fdptitles = self.title
        modified_filename = f'{staff_id}_{staff_name}Workshop_onduty_{fdptitles}.{ext}'
        # Uploads to 'approval_letter/department_staffid/<filename>'
        return f'2024-2025/{self.department.deptcode}/Faculty_Detail/FDP/onduty/brochures/{modified_filename}'
    approval_letter = models.FileField(db_column='approval_letter', upload_to=approval_letter_path, null=True, blank=True)
    brochure_file = models.FileField(db_column='brochure_file', upload_to=brochure_file_path, null=True, blank=True)
# class OnDuty(models.Model):
#     ondutyid =models.AutoField(db_column='OndutyID', primary_key=True)
#     staffno = models.CharField(db_column='FID',max_length=7,blank=True,null=True)
#     department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department')   # Field name made lowercase.
#     fdptitle = models.CharField(db_column='FDPTitle', max_length=100)  # Field name made lowercase.
#     venue = models.CharField(db_column='Venue', max_length=100)  # Field name made lowercase.
#     sdate = models.DateField(db_column='Sdate')  # Field name made lowercase.
#     edate = models.DateField(db_column='Edate')  # Field name made lowercase.
#     noofdays = models.IntegerField(db_column='NoOfDays')  # Field name made lowercase.
#     academicyear = models.CharField(db_column='AcademicYear',max_length=10)  # Field name made lowercase.
#     sem = models.CharField(db_column='Sem', max_length=6)  # Field name made lowercase.
#     programmetype = models.CharField(db_column='ProgrammeType', max_length=6) 
#     approval_letter = models.FileField(db_column='approval_letter',upload_to='approval_letter/', null=True,blank=True)
#     brochure_file = models.FileField(db_column='brochure_file',upload_to='brochure_files',null=True,blank=True)
#     is_approved = models.BooleanField(db_column='is_approved',default=False)
#     createdtime = models.DateTimeField(db_column='CreatedTime',auto_now_add=True)  # Field name made lowercase.
#     is_rejected = models.BooleanField(default=False)
#     reject_remarks = models.TextField(blank=True, null=True)

class Course(models.Model):
    ondutyid = models.AutoField(db_column='OndutyID', primary_key=True)
    staffnos = models.ForeignKey(Staff, models.DO_NOTHING, db_column='FID')
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department')
    course_name = models.CharField(max_length=255)
    course_start_date = models.CharField(max_length=255)
    duration_weeks = models.CharField(max_length=255)
    platform = models.CharField(max_length=50)
    recognition = models.CharField(max_length=50)
    is_approved = models.BooleanField(db_column='is_approved', default=False)
    is_approved_hod = models.BooleanField(default=False)
    createdtime = models.DateTimeField(db_column='CreatedTime', auto_now_add=True) 
    def brochure_file_path(self, filename):
        ext = filename.split('.')[-1]
        staff_id = self.staffnos.staffid
        staff_name = self.staffnos.staffname
        fdptitles = self.course_name
        modified_filename = f'{staff_id}_{staff_name}Workshop_onduty_{fdptitles}.{ext}'
        # Uploads to 'approval_letter/department_staffid/<filename>'
        return f'2024-2025/{self.department.deptcode}/Faculty_Detail/FDP/onduty/brochures/{modified_filename}'
    approval_letter = models.FileField(db_column='approval_letter', upload_to=brochure_file_path, null=True, blank=True) 

    def __str__(self):
        return self.course_name   

class IqacFdp(models.Model):
    fdpid= models.AutoField(db_column='ID', primary_key=True)
    onduty = models.ForeignKey(OnDuty, on_delete=models.CASCADE)
    finsupport = models.CharField(db_column='FinSupport', max_length=20,null=True,blank=True) 
    claimamount = models.DecimalField(db_column='ClaimAmount', max_digits=18, decimal_places=2, blank=True, null=True)
    def finacial_files(self, filename):
        ext = filename.split('.')[-1]
        staff_id = self.onduty.staffnos.staffid
        staff_name = self.onduty.staffnos.staffname
        fdptitles = self.onduty.fdptitle
        modified_filename = f'{staff_id}_{staff_name}_FDP_{fdptitles}.{ext}'
        # Uploads to 'approval_letter/department_staffid/<filename>'
        return f'2024-2025/{self.onduty.department.deptcode}/Faculty_Detail/FDP/onduty/consolidated_proof/{modified_filename}'
    ffinpath =  models.FileField(db_column='fincial_file',upload_to=finacial_files,null=True,blank=True) # Field name made lowercase.
    proof = models.FileField(db_column='proof',upload_to=finacial_files)
    createdtime = models.DateTimeField(db_column='CreatedTime',auto_now_add=True)   # Field name made lowercase.
    qid = models.IntegerField(db_column='QID', blank=True, null=True)  # Field name made lowercase.
    did = models.IntegerField(db_column='DID', blank=True, null=True)  # Field name made lowercase.
    is_approved = models.BooleanField(default=False)
    is_approved_hod = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    reject_remarks = models.TextField(blank=True, null=True)
    is_achieved = models.BooleanField(default=False)
    faculty = models.ForeignKey(Staff, related_name='fdps', on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update target's achieved_count when FDP is saved
        targets = IqacTargetDetails.objects.filter(faculty=self.faculty, department=self.faculty.department)
        for target in targets:
            target.update_achieved_count()

    def __str__(self):
        return f"IqacFdp for {self.faculty} on {self.date}"

@receiver(post_save, sender=IqacFdp)
def update_target_achieved_count(sender, instance, **kwargs):
    targets = IqacTargetDetails.objects.filter(faculty=instance.faculty, department=instance.faculty.department)
    for target in targets:
        target.update_achieved_count()
    
class Iqacworkshop(models.Model):
    fdpid= models.AutoField(db_column='ID', primary_key=True)
    onduty = models.ForeignKey(ondutyWorkshop, on_delete=models.CASCADE)
    finsupport = models.CharField(db_column='FinSupport', max_length=20,null=True,blank=True) 
    claimamount = models.DecimalField(db_column='ClaimAmount', max_digits=18, decimal_places=2, blank=True, null=True)
    def finacial_files(self, filename):
        ext = filename.split('.')[-1]
        staff_id = self.onduty.staffnos.staffid
        staff_name = self.onduty.staffnos.staffname
        fdptitles = self.onduty.title
        modified_filename = f'{staff_id}_{staff_name}_FDP_{fdptitles}.{ext}'
        # Uploads to 'approval_letter/department_staffid/<filename>'
        return f'2024-2025/{self.onduty.department.deptcode}/Faculty_Detail/FDP/onduty/consolidated_proof/{modified_filename}'
    ffinpath =  models.FileField(db_column='fincial_file',upload_to=finacial_files,null=True,blank=True) # Field name made lowercase.
    proof = models.FileField(db_column='proof',upload_to=finacial_files)
    createdtime = models.DateTimeField(db_column='CreatedTime',auto_now_add=True)   # Field name made lowercase.
    qid = models.IntegerField(db_column='QID', blank=True, null=True)  # Field name made lowercase.
    did = models.IntegerField(db_column='DID', blank=True, null=True)  # Field name made lowercase.
    is_approved = models.BooleanField(default=False)
    is_approved_hod = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    reject_remarks = models.TextField(blank=True, null=True)
    is_achieved = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update target's achieved_count when FDP is saved
        targets = Target.objects.filter(faculty=self.faculty, department=self.faculty.department)
        for target in targets:
            target.update_achieved_count()

    def __str__(self):
        return f"Iqacworkshop for {self.faculty} on {self.date}"

@receiver(post_save, sender=Iqacworkshop)
def update_target_achieved_count(sender, instance, **kwargs):
    targets = Target.objects.filter(faculty=instance.faculty, department=instance.faculty.department)
    for target in targets:
        target.update_achieved_count()
class Iqacresourceperson(models.Model):
    fdpid= models.AutoField(db_column='ID', primary_key=True)
    onduty = models.ForeignKey(ondutyFdResourceperson, on_delete=models.CASCADE)
    finsupport = models.CharField(db_column='FinSupport', max_length=20,null=True,blank=True) 
    claimamount = models.DecimalField(db_column='ClaimAmount', max_digits=18, decimal_places=2, blank=True, null=True)
    def finacial_files(self, filename):
        ext = filename.split('.')[-1]
        staff_id = self.onduty.staffnos.staffid
        staff_name = self.onduty.staffnos.staffname
        fdptitles = self.onduty.title
        modified_filename = f'{staff_id}_{staff_name}_FDP_{fdptitles}.{ext}'
        # Uploads to 'approval_letter/department_staffid/<filename>'
        return f'2024-2025/{self.onduty.department.deptcode}/Faculty_Detail/FDP/onduty/consolidated_proof/{modified_filename}'
    ffinpath =  models.FileField(db_column='fincial_file',upload_to=finacial_files,null=True,blank=True) # Field name made lowercase.
    proof = models.FileField(db_column='proof',upload_to=finacial_files)
    createdtime = models.DateTimeField(db_column='CreatedTime',auto_now_add=True)   # Field name made lowercase.
    qid = models.IntegerField(db_column='QID', blank=True, null=True)  # Field name made lowercase.
    did = models.IntegerField(db_column='DID', blank=True, null=True)  # Field name made lowercase.
    is_approved = models.BooleanField(default=False)
    is_approved_hod = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    reject_remarks = models.TextField(blank=True, null=True)
    is_achieved = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update target's achieved_count when FDP is saved
        targets = Target.objects.filter(faculty=self.faculty, department=self.faculty.department)
        for target in targets:
            target.update_achieved_count()

    def __str__(self):
        return f"Iqacresourceperson for {self.faculty} on {self.date}"

@receiver(post_save, sender=Iqacresourceperson)
def update_target_achieved_count(sender, instance, **kwargs):
    targets = Target.objects.filter(faculty=instance.faculty, department=instance.faculty.department)
    for target in targets:
        target.update_achieved_count()
class Iqaconline(models.Model):
    fdpid= models.AutoField(db_column='ID', primary_key=True)
    onduty = models.ForeignKey(Course, on_delete=models.CASCADE)
    finsupport = models.CharField(db_column='FinSupport', max_length=20,null=True,blank=True) 
    claimamount = models.DecimalField(db_column='ClaimAmount', max_digits=18, decimal_places=2, blank=True, null=True)
    def finacial_files(self, filename):
        ext = filename.split('.')[-1]
        staff_id = self.onduty.staffnos.staffid
        staff_name = self.onduty.staffnos.staffname
        fdptitles = self.onduty.course_name
        modified_filename = f'{staff_id}_{staff_name}_FDP_{fdptitles}.{ext}'
        # Uploads to 'approval_letter/department_staffid/<filename>'
        return f'2024-2025/{self.onduty.department.deptcode}/Faculty_Detail/FDP/onduty/consolidated_proof/{modified_filename}'
    ffinpath =  models.FileField(db_column='fincial_file',upload_to=finacial_files,null=True,blank=True) # Field name made lowercase.
    proof = models.FileField(db_column='proof',upload_to=finacial_files)
    createdtime = models.DateTimeField(db_column='CreatedTime',auto_now_add=True)   # Field name made lowercase.
    qid = models.IntegerField(db_column='QID', blank=True, null=True)  # Field name made lowercase.
    did = models.IntegerField(db_column='DID', blank=True, null=True)  # Field name made lowercase.
    is_approved = models.BooleanField(default=False)
    is_approved_hod = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    reject_remarks = models.TextField(blank=True, null=True)
    is_achieved = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update target's achieved_count when FDP is saved
        targets = Target.objects.filter(faculty=self.faculty, department=self.faculty.department)
        for target in targets:
            target.update_achieved_count()

    def __str__(self):
        return f"Iqaconline for {self.faculty} on {self.date}"

@receiver(post_save, sender=Iqaconline)
def update_target_achieved_count(sender, instance, **kwargs):
    targets = Target.objects.filter(faculty=instance.faculty, department=instance.faculty.department)
    for target in targets:
        target.update_achieved_count()

class Publication(models.Model):
    staffnoss = models.ForeignKey(Staff, models.DO_NOTHING, db_column='FID')
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department') 
    nameoftheauthor=models.CharField(max_length=100)
    Department_of_author = models.CharField(max_length=100)
    co_authors = models.CharField(max_length=100)
    Department_of_coauthor= models.CharField(max_length=50)
    Tile_of_paper = models.CharField(max_length=100)
    Name_of_journal=models.CharField(max_length=100)
    volume=models.CharField(max_length=100)
    page_no = models.CharField(max_length=100)
    month_of_publication= models.CharField(max_length=100,null=True,blank=True)
    ISSN= models.CharField(max_length=  50)
    impactfactor= models.CharField(max_length=100)
    Indexed_by=models.CharField(max_length=50)
    Journalranking = models.CharField(max_length=50)
    link=models.CharField(max_length=50)
    DOI=models.CharField(max_length=50)
   
    # file = models.FileField(upload_to='fdp_files/', null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    is_approved_hod = models.BooleanField(default=False)
    is_approved_iqac = models.BooleanField(default=False)
    date_field = models.DateField(auto_now_add=True)
    is_achieved = models.BooleanField(default=False)
    def approval_letter_path(self, filename):
        ext = filename.split('.')[-1]
        staff_id = self.staffnoss.staffid
        staff_name = self.staffnoss.staffname
        fdptitles = self.Tile_of_paper
        modified_filename = f'{staff_id}_{staff_name}Journal_Publication_{fdptitles}.{ext}'
        # Uploads to 'approval_letter/department_staffid/<filename>'
        return f'2024-2025/{self.department.deptcode}/Research/Journal_Publication/{modified_filename}'
    pdf_file = models.FileField(db_column='pdf_file', upload_to=approval_letter_path, null=True, blank=True)
    def clean(self):
        # Check for duplicates before saving
        if Publication.objects.filter(
            ISSN=self.ISSN, DOI=self.DOI, Tile_of_paper=self.Tile_of_paper
        ).exclude(id=self.id).exists():
            raise ValidationError("A publication with the same ISSN, DOI, and Title of Paper already exists.")

    def save(self, *args, **kwargs):
        self.clean()  # Ensure clean method is called
        super(Publication, self).save(*args, **kwargs)  # Call the original save method
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update target's achieved_count when FDP is saved
        targets = Target.objects.filter(faculty=self.faculty, department=self.faculty.department)
        for target in targets:
            target.update_achieved_count()

    def __str__(self):
        return f"Publication for {self.faculty} on {self.date}"

@receiver(post_save, sender=Publication)
def update_target_achieved_count(sender, instance, **kwargs):
    targets = Target.objects.filter(faculty=instance.faculty, department=instance.faculty.department)
    for target in targets:
        target.update_achieved_count()



class BookChapter(models.Model):
    staffame = models.ForeignKey(Staff, models.DO_NOTHING, db_column='FID')
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department') 
    name_of_faculty = models.CharField(max_length=255, blank=True)
    position = models.CharField(max_length=100, blank=True)
    page_no = models.CharField(max_length=50, blank=True)
    title_of_book_chapter = models.CharField(max_length=255, blank=True)
    title_of_book = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=100, blank=True)
    month_of_publication = models.CharField(max_length=50, blank=True)
    ISSN = models.CharField(max_length=20, blank=True)
    indexed_by = models.CharField(max_length=255, blank=True)
    name_of_publisher = models.CharField(max_length=255, blank=True)
    link = models.URLField(blank=True)
   
    is_approved = models.BooleanField(default=False)
    is_approved_hod = models.BooleanField(default=False)
    is_approved_iqac = models.BooleanField(default=False)
    date_field = models.DateField(auto_now_add=True)
    def approval_letter_path(self, filename):
        ext = filename.split('.')[-1]
        staff_id = self.staffame.staffid
        staff_name = self.staffame.staffname
        fdptitles = self.title_of_book_chapter
        modified_filename = f'{staff_id}_{staff_name}BookChapter_{fdptitles}.{ext}'
        # Uploads to 'approval_letter/department_staffid/<filename>'
        return f'2024-2025/{self.department.deptcode}/Research/BookChapter/{modified_filename}'
    pdf_file = models.FileField(db_column='pdf_file', upload_to=approval_letter_path, null=True, blank=True)
    
    def __str__(self):
        return self.title_of_book_chapter
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update target's achieved_count when FDP is saved
        targets = Target.objects.filter(faculty=self.faculty, department=self.faculty.department)
        for target in targets:
            target.update_achieved_count()

    def __str__(self):
        return f"BookChapter for {self.faculty} on {self.date}"

@receiver(post_save, sender=BookChapter)
def update_target_achieved_count(sender, instance, **kwargs):
    targets = Target.objects.filter(faculty=instance.faculty, department=instance.faculty.department)
    for target in targets:
        target.update_achieved_count()
class ConsultancyApplication(models.Model):
    staffsame = models.ForeignKey(Staff, models.DO_NOTHING, db_column='FID')
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department')
    nameofthefaculty = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=100)
    name_of_the_consultancy = models.CharField(max_length=100)
    agency_seeking = models.CharField(max_length=100)
    date_of_application = models.CharField(max_length=100)
    number_of_trainees = models.CharField(max_length=100)
    revenue = models.DecimalField(max_digits=10, decimal_places=2)
    pdf_file = models.FileField(upload_to='pdf_files/', blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    is_approved_hod = models.BooleanField(default=False)
    is_approved_iqac = models.BooleanField(default=False)
    date_field = models.DateField(auto_now_add=True)
    def approval_letter_path(self, filename):
        ext = filename.split('.')[-1]
        staff_id = self.staffsame.staffid
        staff_name = self.staffsame.staffname
        fdptitles = self.name_of_the_consultancy
        modified_filename = f'{staff_id}_{staff_name}_Consultancy_{fdptitles}.{ext}'
        # Uploads to 'approval_letter/department_staffid/<filename>'
        return f'2024-2025/{self.department.deptcode}/Research/Consultancy/{modified_filename}'
    pdf_file = models.FileField(db_column='pdf_file', upload_to=approval_letter_path, null=True, blank=True)
    def __str__(self):
        return self.name + ' - ' + self.name_of_the_consultancy
    is_achieved = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update target's achieved_count when FDP is saved
        targets = Target.objects.filter(faculty=self.faculty, department=self.faculty.department)
        for target in targets:
            target.update_achieved_count()

    def __str__(self):
        return f"ConsultancyApplication for {self.faculty} on {self.date}"

@receiver(post_save, sender=ConsultancyApplication)
def update_target_achieved_count(sender, instance, **kwargs):
    targets = Target.objects.filter(faculty=instance.faculty, department=instance.faculty.department)
    for target in targets:
        target.update_achieved_count()
class Innovation(models.Model):
    staffames = models .ForeignKey(Staff, models.DO_NOTHING, db_column='FID')
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department')
    nameofthefaculty = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    innovation_title = models.CharField(max_length=200)
    application_no = models.CharField(max_length=50)
    date_of_application = models.CharField(max_length=200)
    date_of_published = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    link = models.URLField(max_length=200, blank=True)
    file = models.FileField(upload_to='files/', blank=True, null=True)
    date_field = models.DateField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    is_approved_hod = models.BooleanField(default=False)
    is_approved_iqac = models.BooleanField(default=False)
    def approval_letter_path(self, filename):
        ext = filename.split('.')[-1]
        staff_id = self.staffames.staffid
        staff_name = self.staffames.staffname
        fdptitles = self.innovation_title
        modified_filename = f'{staff_id}_{staff_name}_Patent_{fdptitles}.{ext}'
        # Uploads to 'approval_letter/department_staffid/<filename>'
        return f'2024-2025/{self.department.deptcode}/Research/Patent/{modified_filename}'
    pdf_file = models.FileField(db_column='pdf_file', upload_to=approval_letter_path, null=True, blank=True)
    def __str__(self):
        return f'{self.name} - {self.innovation_title}'
        is_achieved = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update target's achieved_count when FDP is saved
        targets = Target.objects.filter(faculty=self.faculty, department=self.faculty.department)
        for target in targets:
            target.update_achieved_count()

    def __str__(self):
        return f"FDP for {self.faculty} on {self.date}"

@receiver(post_save, sender=Innovation)
def update_target_achieved_count(sender, instance, **kwargs):
    targets = Target.objects.filter(faculty=instance.faculty, department=instance.faculty.department)
    for target in targets:
        target.update_achieved_count()

class ResearchProposal(models.Model):
    staffames = models.ForeignKey(Staff, models.DO_NOTHING, db_column='FID')
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department')
    principal_investigator_name = models.CharField(max_length=255)
    principal_investigator_department = models.CharField(max_length=255)

    # Co-Principal Investigators Fields
    co_principal_investigator_1_name = models.CharField(max_length=255, blank=True, null=True)
    co_principal_investigator_1_department = models.CharField(max_length=255, blank=True, null=True)
    co_principal_investigator_2_name = models.CharField(max_length=255, blank=True, null=True)
    co_principal_investigator_2_department = models.CharField(max_length=255, blank=True, null=True)

    # Funding Fields
    funding_agency = models.CharField(max_length=255)
    funding_type = models.CharField(max_length=50)
    proposal_status = models.CharField(max_length=50)

    # Scheme and Sanction Fields
    scheme_name = models.CharField(max_length=255)
    sanction_letter_no_date = models.CharField(max_length=255)
    other_faculty_details = models.TextField(blank=True, null=True)
    supporting_staff_details = models.TextField(blank=True, null=True)

    # Financial Fields
    submission_date = models.CharField(max_length=255)
    funds_provided = models.DecimalField(max_digits=10, decimal_places=2)
    amount_received = models.DecimalField(max_digits=10, decimal_places=2)
    amount_utilized = models.DecimalField(max_digits=10, decimal_places=2)
    utilization_certificate_date = models.CharField(max_length=100)
    seed_money_provided = models.DecimalField(max_digits=10, decimal_places=2)
    grant_receiving_date = models.CharField(max_length=100)

    # Additional Fields
    project_duration = models.CharField(max_length=255)
    policy_document_link = models.URLField(blank=True, null=True)
    sanction_letter_link = models.URLField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    is_approved_hod = models.BooleanField(default=False)
    is_approved_iqac = models.BooleanField(default=False)
    date_field = models.DateField(auto_now_add=True)
    is_achieved = models.BooleanField(default=False)
    def approval_letter_path(self, filename):
        ext = filename.split('.')[-1]
        staff_id = self.staffames.staffid
        staff_name = self.staffames.staffname
        fdptitles = self.scheme_name
        modified_filename = f'{staff_id}_{staff_name}_Research_project_{fdptitles}.{ext}'
        # Uploads to 'approval_letter/department_staffid/<filename>'
        return f'2024-2025/{self.department.deptcode}/Research/Research_project/{modified_filename}'
    file = models.FileField(db_column='file', upload_to=approval_letter_path, null=True, blank=True)
    def __str__(self):
        return f"Project {self.id}: {self.scheme_name} by {self.principal_investigator_name}"
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update target's achieved_count when FDP is saved
        targets = Target.objects.filter(faculty=self.faculty, department=self.faculty.department)
        for target in targets:
            target.update_achieved_count()

    def __str__(self):
        return f"ResearchProposal for {self.faculty} on {self.date}"

@receiver(post_save, sender=ResearchProposal)
def update_target_achieved_count(sender, instance, **kwargs):
    targets = Target.objects.filter(faculty=instance.faculty, department=instance.faculty.department)
    for target in targets:
        target.update_achieved_count()
class PhDRegistration(models.Model):
    staffames = models.ForeignKey(Staff, models.DO_NOTHING, db_column='FID')
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department')
    # Name of the faculty
    faculty_name = models.CharField(max_length=100)

    # Program applied for Ph.D., D.Sc., D.Litt., or LLD
    program_applied = models.CharField(max_length=100)

    # Name of the supervisor and their department
    supervisor_name = models.CharField(max_length=200)

    # Year of registration
    registration_year = models.IntegerField()

    # Status of the registration
    status = models.CharField(max_length=50)
    registration_date = models.CharField(max_length=255)
    part_time_full_time = models.CharField(max_length=50)
    university_name = models.CharField(max_length=200)
    allotment_order_link = models.URLField(max_length=500, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    is_approved_hod = models.BooleanField(default=False)
    is_approved_iqac = models.BooleanField(default=False)
    date_field = models.DateField(auto_now_add=True)
    is_achieved = models.BooleanField(default=False)
    def approval_letter_path(self, filename):
        ext = filename.split('.')[-1]
        staff_id = self.staffames.staffid
        staff_name = self.staffames.staffname
        fdptitles = self.faculty_name
        modified_filename = f'{staff_id}_{staff_name}_PhD_Register_{fdptitles}.{ext}'
        # Uploads to 'approval_letter/department_staffid/<filename>'
        return f'2024-2025/{self.department.deptcode}/Research/Phd_Register/{modified_filename}'
    financial_support = models.FileField(db_column='financial_support', upload_to=approval_letter_path, null=True, blank=True)
    def __str__(self):
        return f'{self.faculty_name} - {self.program_applied}'
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update target's achieved_count when FDP is saved
        targets = Target.objects.filter(faculty=self.faculty, department=self.faculty.department)
        for target in targets:
            target.update_achieved_count()
    def __str__(self):
        return f"PhDRegistration for {self.faculty} on {self.date}"

@receiver(post_save, sender=PhDRegistration)
def update_target_achieved_count(sender, instance, **kwargs):
    targets = Target.objects.filter(faculty=instance.faculty, department=instance.faculty.department)
    for target in targets:
        target.update_achieved_count()
class ConferenceOnDuty(models.Model):
    staffames = models.ForeignKey(Staff, models.DO_NOTHING, db_column='FID')
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department')
    faculty_name = models.CharField(max_length=100)
    conference_title = models.CharField(max_length=200)
    paper_title = models.CharField(max_length=200)
    author_position = models.CharField(max_length=100)
    participation_type = models.CharField(max_length=20)
    conference_level = models.CharField(max_length=20)
    conference_venue = models.CharField(max_length=200)
    organised_by = models.CharField(max_length=200)
    proceedings_title = models.CharField(max_length=200)
    proceedings_page = models.CharField(max_length=20)
    proceedings_isbn = models.CharField(max_length=20)
    publication_date = models.CharField(max_length=20)
    teacher_affiliation = models.CharField(max_length=200)
    publisher_name = models.CharField(max_length=200)
    approval_letter = models.FileField(upload_to='approval_letters/',null=True)
    is_approved = models.BooleanField(default=False)
    is_approved_hod = models.BooleanField(default=False)
    is_approved_iqac = models.BooleanField(default=False)
    date_field = models.DateField(auto_now_add=True)
    def approval_letter_path(self, filename):
        ext = filename.split('.')[-1]
        staff_id = self.staffames.staffid
        staff_name = self.staffames.staffname
        fdptitles = self.faculty_name
        modified_filename = f'{staff_id}_{staff_name}_Conference_{fdptitles}.{ext}'
        # Uploads to 'approval_letter/department_staffid/<filename>'
        return f'2024-2025/{self.department.deptcode}/Faculty_Detail/Conference/onduty/{modified_filename}'
    proof_file = models.FileField(db_column='proof_file', upload_to=approval_letter_path, null=True, blank=True)
    def __str__(self):
        return f"{self.faculty_name} - {self.conference_title}"

class Iqaconference(models.Model):
    fdpid= models.AutoField(db_column='ID', primary_key=True)
    onduty = models.ForeignKey(ConferenceOnDuty, on_delete=models.CASCADE)
    finsupport = models.CharField(db_column='FinSupport', max_length=20,null=True,blank=True) 
    claimamount = models.DecimalField(db_column='ClaimAmount', max_digits=18, decimal_places=2, blank=True, null=True)
    def finacial_files(self, filename):
        ext = filename.split('.')[-1]
        staff_id = self.onduty.staffnos.staffid
        staff_name = self.onduty.staffnos.staffname
        fdptitles = self.onduty.conference_title
        modified_filename = f'{staff_id}_{staff_name}_FDP_{fdptitles}.{ext}'
        # Uploads to 'approval_letter/department_staffid/<filename>'
        return f'2024-2025/{self.onduty.department.deptcode}/Faculty_Detail/FDP/onduty/consolidated_proof/{modified_filename}'
    ffinpath =  models.FileField(db_column='fincial_file',upload_to=finacial_files,null=True,blank=True) # Field name made lowercase.
    proof = models.FileField(db_column='proof',upload_to=finacial_files)
    createdtime = models.DateTimeField(db_column='CreatedTime',auto_now_add=True)   # Field name made lowercase.
    qid = models.IntegerField(db_column='QID', blank=True, null=True)  # Field name made lowercase.
    did = models.IntegerField(db_column='DID', blank=True, null=True)  # Field name made lowercase.
    is_approved = models.BooleanField(default=False)
    is_approved_hod = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    reject_remarks = models.TextField(blank=True, null=True)
    is_achieved = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update target's achieved_count when FDP is saved
        targets = Target.objects.filter(faculty=self.faculty, department=self.faculty.department)
        for target in targets:
            target.update_achieved_count()
    def __str__(self):
        return f"Iqaconference for {self.faculty} on {self.date}"
@receiver(post_save, sender=Iqaconference)
def update_target_achieved_count(sender, instance, **kwargs):
    targets = Target.objects.filter(faculty=instance.faculty, department=instance.faculty.department)
    for target in targets:
        target.update_achieved_count()
class Students(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Mentor(models.Model):
    user = models.OneToOneField(Staff, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Mentorship(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    user = models.ForeignKey(Staff, on_delete=models.CASCADE)  # Added for authentication

    def __str__(self):
        return f"{self.student.name} - {self.mentor.name}"
class StudentParticipation(models.Model):
    staffames = models.ForeignKey(Staff, models.DO_NOTHING, db_column='FID')
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department')
    student_name = models.CharField(max_length=100)
    participation_type = models.CharField(max_length=100)
    event_name = models.CharField(max_length=200)
    event_type = models.CharField(max_length=100)
    event_type_detail = models.CharField(max_length=200)
    number_of_participations = models.IntegerField(default=0)
    participation_achievement = models.TextField()
    date_of_participation = models.DateField()
    consultants_involved = models.CharField(max_length=200)
    year_of_implementation = models.CharField(max_length=4)
    award_name = models.CharField(max_length=200)
    team_or_individual = models.CharField(max_length=100)
    students = models.JSONField()

    def __str__(self):
        return f'{self.student_name} - {self.event_name}'
class studentevent(models.Model):
    staffames = models.ForeignKey(Staff, models.DO_NOTHING, db_column='FID')
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department')
    programme_title = models.CharField(max_length=200)
    programme_type = models.CharField(max_length=100)
    number_of_participants = models.IntegerField(default=0)
    duration = models.CharField(max_length=100)
    venue = models.CharField(max_length=200)
    level = models.CharField(max_length=100)
    feedback_collected = models.BooleanField(default=False)
    resource_person = models.CharField(max_length=200)
    coordinators = models.JSONField(default=list)

    def __str__(self):
        return self.programme_title
class facultyevents(models.Model):
    staffames = models.ForeignKey(Staff, models.DO_NOTHING, db_column='FID')
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department')
    programme_title = models.CharField(max_length=200)
    programme_type = models.CharField(max_length=100)
    number_of_participants = models.IntegerField(default=0)
    duration = models.CharField(max_length=100)
    venue = models.CharField(max_length=200)
    level = models.CharField(max_length=100)
    feedback_collected = models.BooleanField(default=False)
    resource_person = models.CharField(max_length=200)

    def __str__(self):
        return self.programme_title
class ConferencePaper(models.Model):
    staffames = models.ForeignKey(Staff, models.DO_NOTHING, db_column='FID')
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department')
    conference_title = models.CharField(max_length=200)
    paper_title = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    participation_type = models.CharField(max_length=100)
    conference_level = models.CharField(max_length=100)
    venue = models.CharField(max_length=200)
    organised_by = models.CharField(max_length=200)
    proceedings_title = models.CharField(max_length=200)
    page_no = models.CharField(max_length=50)
    isbn = models.CharField(max_length=20)
    publication_date = models.DateField()
    affiliating_institute = models.CharField(max_length=200)
    publisher_name = models.CharField(max_length=200)
    project_outcome = models.TextField()
    support_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.paper_title

class Student(models.Model):
    conference_paper = models.ForeignKey(ConferencePaper, on_delete=models.CASCADE, related_name='students')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class outreachActivity(models.Model):
    staffames = models.ForeignKey(Staff, models.DO_NOTHING, db_column='FID')
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department')
    activity_name = models.CharField(max_length=200)
    organising_unit = models.CharField(max_length=200)
    scheme_name = models.CharField(max_length=200)
    activity_date = models.DateField()
    venue = models.CharField(max_length=200)
    participants_count = models.IntegerField(default=0)

    def __str__(self):
        return self.activity_name
class OCCCourse(models.Model):
    staffames = models.ForeignKey(Staff, models.DO_NOTHING, db_column='FID')
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department')
    course_name = models.CharField(max_length=200)
    course_code = models.CharField(max_length=20)
    course_type = models.CharField(max_length=100)
    course_activities = models.TextField()
    activity_date = models.DateField()
    course_duration = models.CharField(max_length=100)
    year_of_offering = models.IntegerField()
    times_offered = models.IntegerField()
    students_enrolled = models.IntegerField()
    students_completed = models.IntegerField()
    feedback_collected = models.BooleanField(default=False)

    def __str__(self):
        return self.course_name
class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


def get_upload_path(instance, filename):
    # Customize this function to generate the folder path dynamically
    # For example, you can use the user's ID, username, or any other attribute
    # Here, we're using the current date to create a folder structure
    return os.path.join(
        'uploads',
        instance.user.username,  # Assuming there's a user attribute in your model
        filename
    )
