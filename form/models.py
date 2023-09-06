from django.db import models
from . import utils  # utils.py file
from django.utils.html import mark_safe




#Login Credentials Model
class Login(models.Model):
    # application id (auto generated)
    application_id = models.CharField(max_length=100, unique=True)
    ipu_registration = models.PositiveBigIntegerField(unique=True)   
    password = models.CharField(max_length=25)
    candidate_name = models.CharField(max_length=100)
    candidate_email = models.EmailField(max_length=100, unique=False)
    candidate_mobile = models.PositiveBigIntegerField(unique=False)     
    ip_address = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name_plural = "Login"    #so that Django doesnt add the default 's' for plural in table name
        db_table = "login"


# Because the same user can apply for multiple course (for eg ballb/bballb , eco/bba/bcom, etc.)
# So taking seperate table for ipu_registration and course
class CoursesLogin(models.Model):
    ipu_registration = models.PositiveBigIntegerField()  
    course = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = "Login with Courses"   
        db_table = "course_login"


# Allowed IP addresses
class AllowedIP(models.Model):
    ip_address = models.CharField(max_length=100)

    def __str__(self):         # for showing record by ip in admin panel
        return (self.ip_address)
    class Meta:
        verbose_name_plural = "Allowed IP Addresses"    #so that Django doesnt add the default 's' for plural in table name
        db_table = "allowed_ip_addresses"



# For storing bank details
class BankDetails(models.Model):
    ipu_registration = models.PositiveBigIntegerField(unique=True)
    course = models.CharField(max_length=25)
    account_holder_name = models.CharField(max_length=75)
    account_number = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=50)
    cheque_copy = models.FileField(upload_to=utils.cheque_rename, blank=True)

    class Meta:
        verbose_name_plural = "Bank Details"    #so that Django doesnt add the default 's' for plural in table name
        db_table = "bank_details"



# BBA Temporary Records Model:
class BbaTemp(models.Model):
    # application id (auto generated)
    application_id = models.CharField(max_length=100, unique=True)
    #GGSIPU registration no.
    ipu_registration = models.PositiveBigIntegerField(blank=True, unique=True)
    #candidate details
    candidate_first_name = models.CharField(max_length=100, blank=True)
    candidate_middle_name = models.CharField(max_length=100, blank=True)
    candidate_last_name = models.CharField(max_length=100, blank=True)
    #other candidate details
    dob = models.DateField()
    complete_address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True, unique=False)
    candidate_number = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    #father mother details
    father_first_name = models.CharField(max_length=100, blank=True)
    father_middle_name = models.CharField(max_length=100, blank=True)
    father_last_name = models.CharField(max_length=100, blank=True)
    mother_first_name = models.CharField(max_length=100, blank=True)
    mother_middle_name = models.CharField(max_length=100, blank=True)
    mother_last_name = models.CharField(max_length=100, blank=True)
    father_qualification = models.CharField(max_length=100, blank=True)
    mother_qualification = models.CharField(max_length=100, blank=True)
    father_job = models.CharField(max_length=100, blank=True)
    mother_job = models.CharField(max_length=100, blank=True)
    father_job_designation = models.CharField(max_length=100, blank=True)
    mother_job_designation = models.CharField(max_length=100, blank=True)
    father_business_type = models.CharField(max_length=100, blank=True)
    mother_business_type = models.CharField(max_length=100, blank=True)
    father_number = models.CharField(max_length=100, blank=True)
    mother_number = models.CharField(max_length=100, blank=True)
    father_office_address = models.CharField(max_length=100, blank=True)
    mother_office_address = models.CharField(max_length=100, blank=True)
    #guardian details
    guardian_name = models.CharField(max_length=75, blank=True)
    #12th class details
    board_12th = models.CharField(max_length=255, blank=True)
    year_of_12th = models.PositiveIntegerField(blank=True, null=True)
    rollno_12th = models.PositiveBigIntegerField(blank=True, null=True)
    school_12th = models.CharField(max_length=255, blank=True)
    aggregate_12th = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    first_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    second_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    third_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    fourth_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_12th = models.CharField(max_length=10, blank=True)     # because integer field was giving error even with null=True and Blank=True
    other_subject_2_12th =  models.CharField(max_length=10, blank=True)
    #10th class details
    board_10th = models.CharField(max_length=255, blank=True)
    year_of_10th = models.PositiveIntegerField(blank=True, null=True)
    rollno_10th = models.PositiveBigIntegerField(blank=True, null=True)
    school_10th = models.CharField(max_length=255, blank=True)
    aggregate_10th = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    maths_10th = models.PositiveIntegerField(blank=True, null=True)
    science_10th = models.PositiveIntegerField(blank=True, null=True)
    english_10th = models.PositiveIntegerField(blank=True, null=True)
    sst_10th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_10th = models.CharField(max_length=100, blank=True)   # because integer field was giving error even with null=True and Blank=True
    other_subject_2_10th =  models.CharField(max_length=100, blank=True)
    #CET details
    cet_or_cuet = models.CharField(max_length=10)    # to ask user which paper did he/she appear for
    cet_rank = models.PositiveIntegerField(blank=True, null=True)
    cet_rollno = models.CharField(max_length=100, blank=True)
    #special acheivements
    special_achievements = models.CharField(max_length=255, blank=True)
    #images and files
    passport_photo = models.ImageField(upload_to=utils.bba_photo_rename, blank=True)
    cet_result = models.FileField(upload_to=utils.bba_cetresult_rename, blank=True)
    marksheet_10th = models.FileField(upload_to=utils.bba_10thmarksheet_rename, blank=True)
    marksheet_12th = models.FileField(upload_to=utils.bba_12thmarksheet_rename, blank=True)
    aadhaar = models.FileField(upload_to=utils.bba_aadhar_rename, blank=True)
    pancard = models.FileField(upload_to=utils.bba_pancard_rename, blank=True)
    ipuregistrationproof = models.FileField(upload_to=utils.bba_ipuregistration_rename, blank=True)
    # Transaction Details
    transaction_id = models.CharField(max_length=255, blank=True)
    transaction_proof = models.FileField(upload_to=utils.bba_transaction_rename, blank=True)
    # Counselling Fee Details
    counselling_transaction_id = models.CharField(max_length=255, blank=True)
    counselling_transaction_proof = models.FileField(upload_to=utils.bba_counselling_transaction_rename, blank=True)
    # To track IP address and other information of users
    ip_address = models.CharField(max_length=100, blank=True, null=True)
    forwarded_address = models.CharField(max_length=255, blank=True ,null=True)
    browser_info = models.CharField(max_length=1000, blank=True ,null=True)
    created_at = models.CharField(max_length=255, blank=True ,null=True)

    def __str__(self):         # for showing record by name in admin panel
        return (self.candidate_first_name+' '+self.candidate_last_name)

    def photograph_preview(self):   #for previewing photo in admin panel
        return mark_safe(f'<img src = "{self.passport_photo.url}" width = "100"/>')

    class Meta:
        verbose_name_plural = "BBA Temporary"    # to show table by this name in admin panel
        db_table = "bba_temp"             # to use the name "bba" instead of "form_bba" in db 


# bba Model:
class Bba(models.Model):
    # application id (auto generated)
    application_id = models.CharField(max_length=100, unique=True)
    #GGSIPU registration no.
    ipu_registration = models.PositiveBigIntegerField(blank=True, unique=True)
    # allowed for counselling
    allow_for_counselling = models.BooleanField(default=False)
    # allow for editing of record
    allow_editing = models.BooleanField(default=False)
    #candidate details
    candidate_first_name = models.CharField(max_length=100, blank=True)
    candidate_middle_name = models.CharField(max_length=100, blank=True)
    candidate_last_name = models.CharField(max_length=100, blank=True)
    #other candidate details
    dob = models.DateField()
    complete_address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True, unique=False)
    candidate_number = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    #father mother details
    father_first_name = models.CharField(max_length=100, blank=True)
    father_middle_name = models.CharField(max_length=100, blank=True)
    father_last_name = models.CharField(max_length=100, blank=True)
    mother_first_name = models.CharField(max_length=100, blank=True)
    mother_middle_name = models.CharField(max_length=100, blank=True)
    mother_last_name = models.CharField(max_length=100, blank=True)
    father_qualification = models.CharField(max_length=100, blank=True)
    mother_qualification = models.CharField(max_length=100, blank=True)
    father_job = models.CharField(max_length=100, blank=True)
    mother_job = models.CharField(max_length=100, blank=True)
    father_job_designation = models.CharField(max_length=100, blank=True)
    mother_job_designation = models.CharField(max_length=100, blank=True)
    father_business_type = models.CharField(max_length=100, blank=True)
    mother_business_type = models.CharField(max_length=100, blank=True)
    father_number = models.CharField(max_length=100, blank=True)
    mother_number = models.CharField(max_length=100, blank=True)
    father_office_address = models.CharField(max_length=100, blank=True)
    mother_office_address = models.CharField(max_length=100, blank=True)
    #guardian details
    guardian_name = models.CharField(max_length=75, blank=True)
    #12th class details
    board_12th = models.CharField(max_length=255, blank=True)
    year_of_12th = models.PositiveIntegerField(blank=True)
    rollno_12th = models.PositiveBigIntegerField(blank=True)
    school_12th = models.CharField(max_length=255, blank=True)
    aggregate_12th = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    first_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    second_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    third_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    fourth_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_12th = models.CharField(max_length=10, blank=True)     # because integer field was giving error even with null=True and Blank=True
    other_subject_2_12th =  models.CharField(max_length=10, blank=True)
    #10th class details
    board_10th = models.CharField(max_length=255, blank=True)
    year_of_10th = models.PositiveIntegerField(blank=True)
    rollno_10th = models.PositiveBigIntegerField(blank=True)
    school_10th = models.CharField(max_length=255, blank=True)
    aggregate_10th = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    maths_10th = models.PositiveIntegerField(blank=True)
    science_10th = models.PositiveIntegerField(blank=True)
    english_10th = models.PositiveIntegerField(blank=True)
    sst_10th = models.PositiveIntegerField(blank=True)
    other_subject_10th = models.CharField(max_length=100, blank=True)   # because integer field was giving error even with null=True and Blank=True
    other_subject_2_10th =  models.CharField(max_length=100, blank=True)
    #CET details
    cet_or_cuet = models.CharField(max_length=10)    # to ask user which paper did he/she appear for
    cet_rank = models.PositiveIntegerField(blank=True, null=True)
    cet_rollno = models.CharField(max_length=255, blank=True)
    #special acheivements
    special_achievements = models.CharField(max_length=255, blank=True)
    #images and files
    passport_photo = models.ImageField(upload_to=utils.bba_photo_rename, blank=True)
    cet_result = models.FileField(upload_to=utils.bba_cetresult_rename, blank=True)
    marksheet_10th = models.FileField(upload_to=utils.bba_10thmarksheet_rename, blank=True)
    marksheet_12th = models.FileField(upload_to=utils.bba_12thmarksheet_rename, blank=True)
    aadhaar = models.FileField(upload_to=utils.bba_aadhar_rename, blank=True)
    pancard = models.FileField(upload_to=utils.bba_pancard_rename, blank=True)
    ipuregistrationproof = models.FileField(upload_to=utils.bba_ipuregistration_rename, blank=True)
    # Transaction Details
    transaction_id = models.CharField(max_length=255, blank=True)
    transaction_proof = models.FileField(upload_to=utils.bba_transaction_rename, blank=True)
    # Counselling Fee Details
    counselling_transaction_id = models.CharField(max_length=255, blank=True)
    counselling_transaction_proof = models.FileField(upload_to=utils.bba_counselling_transaction_rename, blank=True)
    # To track IP address and other information of users
    ip_address = models.CharField(max_length=100, blank=True, null=True)
    forwarded_address = models.CharField(max_length=255, blank=True ,null=True)
    browser_info = models.CharField(max_length=1000, blank=True ,null=True)
    created_at = models.CharField(max_length=255, blank=True ,null=True)

    def __str__(self):         # for showing record by name in admin panel
        return (self.candidate_first_name+' '+self.candidate_last_name)

    def photograph_preview(self):   #for previewing photo in admin panel
        return mark_safe(f'<img src = "{self.passport_photo.url}" width = "100"/>')

    class Meta:
        verbose_name_plural = "BBA"    # to show table by this name in admin panel
        db_table = "bba"             # to use the name "bba" instead of "form_bba" in db




# Bcom Temporary Records Model:
class BcomTemp(models.Model):
    # application id (auto generated)
    application_id = models.CharField(max_length=100, unique=True)
    #GGSIPU registration no.
    ipu_registration = models.PositiveBigIntegerField(blank=True, unique=True)
    #candidate details
    candidate_first_name = models.CharField(max_length=100, blank=True)
    candidate_middle_name = models.CharField(max_length=100, blank=True)
    candidate_last_name = models.CharField(max_length=100, blank=True)
    #other candidate details
    dob = models.DateField()
    complete_address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True, unique=False)
    candidate_number = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    #father mother details
    father_first_name = models.CharField(max_length=100, blank=True)
    father_middle_name = models.CharField(max_length=100, blank=True)
    father_last_name = models.CharField(max_length=100, blank=True)
    mother_first_name = models.CharField(max_length=100, blank=True)
    mother_middle_name = models.CharField(max_length=100, blank=True)
    mother_last_name = models.CharField(max_length=100, blank=True)
    father_qualification = models.CharField(max_length=100, blank=True)
    mother_qualification = models.CharField(max_length=100, blank=True)
    father_job = models.CharField(max_length=100, blank=True)
    mother_job = models.CharField(max_length=100, blank=True)
    father_job_designation = models.CharField(max_length=100, blank=True)
    mother_job_designation = models.CharField(max_length=100, blank=True)
    father_business_type = models.CharField(max_length=100, blank=True)
    mother_business_type = models.CharField(max_length=100, blank=True)
    father_number = models.CharField(max_length=100, blank=True)
    mother_number = models.CharField(max_length=100, blank=True)
    father_office_address = models.CharField(max_length=100, blank=True)
    mother_office_address = models.CharField(max_length=100, blank=True)
    #guardian details
    guardian_name = models.CharField(max_length=75, blank=True)
    #12th class details
    board_12th = models.CharField(max_length=255, blank=True)
    year_of_12th = models.PositiveIntegerField(blank=True, null=True)
    rollno_12th = models.PositiveBigIntegerField(blank=True, null=True)
    school_12th = models.CharField(max_length=255, blank=True)
    aggregate_12th = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    first_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    second_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    third_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    fourth_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_12th = models.CharField(max_length=10, blank=True)     # because integer field was giving error even with null=True and Blank=True
    other_subject_2_12th =  models.CharField(max_length=10, blank=True)
    #10th class details
    board_10th = models.CharField(max_length=255, blank=True)
    year_of_10th = models.PositiveIntegerField(blank=True, null=True)
    rollno_10th = models.PositiveBigIntegerField(blank=True, null=True)
    school_10th = models.CharField(max_length=255, blank=True)
    aggregate_10th = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    maths_10th = models.PositiveIntegerField(blank=True, null=True)
    science_10th = models.PositiveIntegerField(blank=True, null=True)
    english_10th = models.PositiveIntegerField(blank=True, null=True)
    sst_10th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_10th = models.CharField(max_length=100, blank=True)   # because integer field was giving error even with null=True and Blank=True
    other_subject_2_10th =  models.CharField(max_length=100, blank=True)
    #CET details
    cet_or_cuet = models.CharField(max_length=10)    # to ask user which paper did he/she appear for
    cet_rank = models.PositiveIntegerField(blank=True, null=True)
    cet_rollno = models.CharField(max_length=100, blank=True)
    #special acheivements
    special_achievements = models.CharField(max_length=255, blank=True)
    #images and files
    passport_photo = models.ImageField(upload_to=utils.bcom_photo_rename, blank=True)
    cet_result = models.FileField(upload_to=utils.bcom_cetresult_rename, blank=True)
    marksheet_10th = models.FileField(upload_to=utils.bcom_10thmarksheet_rename, blank=True)
    marksheet_12th = models.FileField(upload_to=utils.bcom_12thmarksheet_rename, blank=True)
    aadhaar = models.FileField(upload_to=utils.bcom_aadhar_rename, blank=True)
    pancard = models.FileField(upload_to=utils.bcom_pancard_rename, blank=True)
    ipuregistrationproof = models.FileField(upload_to=utils.bcom_ipuregistration_rename, blank=True)
    # Transaction Details
    transaction_id = models.CharField(max_length=255, blank=True)
    transaction_proof = models.FileField(upload_to=utils.bcom_transaction_rename, blank=True)
    # Counselling Fee Details
    counselling_transaction_id = models.CharField(max_length=255, blank=True)
    counselling_transaction_proof = models.FileField(upload_to=utils.bcom_counselling_transaction_rename, blank=True)
    # To track IP address and other information of users
    ip_address = models.CharField(max_length=100, blank=True, null=True)
    forwarded_address = models.CharField(max_length=255, blank=True ,null=True)
    browser_info = models.CharField(max_length=1000, blank=True ,null=True)
    created_at = models.CharField(max_length=255, blank=True ,null=True)

    def __str__(self):         # for showing record by name in admin panel
        return (self.candidate_first_name+' '+self.candidate_last_name)

    def photograph_preview(self):   #for previewing photo in admin panel
        return mark_safe(f'<img src = "{self.passport_photo.url}" width = "100"/>')

    class Meta:
        verbose_name_plural = "B. Com. Temporary"    # to show table by this name in admin panel
        db_table = "bcom_temp"             # to use the name "bcom_temp" instead of "form_bcom_temp" in db 


# bcom Model:
class Bcom(models.Model):
    # application id (auto generated)
    application_id = models.CharField(max_length=100, unique=True)
    #GGSIPU registration no.
    ipu_registration = models.PositiveBigIntegerField(blank=True, unique=True)
    # allowed for counselling
    allow_for_counselling = models.BooleanField(default=False)
    # allow for editing of record
    allow_editing = models.BooleanField(default=False)
    #candidate details
    candidate_first_name = models.CharField(max_length=100, blank=True)
    candidate_middle_name = models.CharField(max_length=100, blank=True)
    candidate_last_name = models.CharField(max_length=100, blank=True)
    #other candidate details
    dob = models.DateField()
    complete_address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True, unique=False)
    candidate_number = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    #father mother details
    father_first_name = models.CharField(max_length=100, blank=True)
    father_middle_name = models.CharField(max_length=100, blank=True)
    father_last_name = models.CharField(max_length=100, blank=True)
    mother_first_name = models.CharField(max_length=100, blank=True)
    mother_middle_name = models.CharField(max_length=100, blank=True)
    mother_last_name = models.CharField(max_length=100, blank=True)
    father_qualification = models.CharField(max_length=100, blank=True)
    mother_qualification = models.CharField(max_length=100, blank=True)
    father_job = models.CharField(max_length=100, blank=True)
    mother_job = models.CharField(max_length=100, blank=True)
    father_job_designation = models.CharField(max_length=100, blank=True)
    mother_job_designation = models.CharField(max_length=100, blank=True)
    father_business_type = models.CharField(max_length=100, blank=True)
    mother_business_type = models.CharField(max_length=100, blank=True)
    father_number = models.CharField(max_length=100, blank=True)
    mother_number = models.CharField(max_length=100, blank=True)
    father_office_address = models.CharField(max_length=100, blank=True)
    mother_office_address = models.CharField(max_length=100, blank=True)
    #guardian details
    guardian_name = models.CharField(max_length=75, blank=True)
    #12th class details
    board_12th = models.CharField(max_length=255, blank=True)
    year_of_12th = models.PositiveIntegerField(blank=True)
    rollno_12th = models.PositiveBigIntegerField(blank=True)
    school_12th = models.CharField(max_length=255, blank=True)
    aggregate_12th = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    first_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    second_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    third_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    fourth_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_12th = models.CharField(max_length=10, blank=True)     # because integer field was giving error even with null=True and Blank=True
    other_subject_2_12th =  models.CharField(max_length=10, blank=True)
    #10th class details
    board_10th = models.CharField(max_length=255, blank=True)
    year_of_10th = models.PositiveIntegerField(blank=True)
    rollno_10th = models.PositiveBigIntegerField(blank=True)
    school_10th = models.CharField(max_length=255, blank=True)
    aggregate_10th = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    maths_10th = models.PositiveIntegerField(blank=True)
    science_10th = models.PositiveIntegerField(blank=True)
    english_10th = models.PositiveIntegerField(blank=True)
    sst_10th = models.PositiveIntegerField(blank=True)
    other_subject_10th = models.CharField(max_length=100, blank=True)   # because integer field was giving error even with null=True and Blank=True
    other_subject_2_10th =  models.CharField(max_length=100, blank=True)
    #CET details
    cet_or_cuet = models.CharField(max_length=10)    # to ask user which paper did he/she appear for
    cet_rank = models.PositiveIntegerField(blank=True, null=True)
    cet_rollno = models.CharField(max_length=255, blank=True)
    #special acheivements
    special_achievements = models.CharField(max_length=255, blank=True)
    #images and files
    passport_photo = models.ImageField(upload_to=utils.bcom_photo_rename, blank=True)
    cet_result = models.FileField(upload_to=utils.bcom_cetresult_rename, blank=True)
    marksheet_10th = models.FileField(upload_to=utils.bcom_10thmarksheet_rename, blank=True)
    marksheet_12th = models.FileField(upload_to=utils.bcom_12thmarksheet_rename, blank=True)
    aadhaar = models.FileField(upload_to=utils.bcom_aadhar_rename, blank=True)
    pancard = models.FileField(upload_to=utils.bcom_pancard_rename, blank=True)
    ipuregistrationproof = models.FileField(upload_to=utils.bcom_ipuregistration_rename, blank=True)
    # Transaction Details
    transaction_id = models.CharField(max_length=255, blank=True)
    transaction_proof = models.FileField(upload_to=utils.bcom_transaction_rename, blank=True)
    # Counselling Fee Details
    counselling_transaction_id = models.CharField(max_length=255, blank=True)
    counselling_transaction_proof = models.FileField(upload_to=utils.bcom_counselling_transaction_rename, blank=True)
    # To track IP address and other information of users
    ip_address = models.CharField(max_length=100, blank=True, null=True)
    forwarded_address = models.CharField(max_length=255, blank=True ,null=True)
    browser_info = models.CharField(max_length=1000, blank=True ,null=True)
    created_at = models.CharField(max_length=255, blank=True ,null=True)

    def __str__(self):         # for showing record by name in admin panel
        return (self.candidate_first_name+' '+self.candidate_last_name)

    def photograph_preview(self):   #for previewing photo in admin panel
        return mark_safe(f'<img src = "{self.passport_photo.url}" width = "100"/>')

    class Meta:
        verbose_name_plural = "B. Com."    # to show table by this name in admin panel
        db_table = "bcom"             # to use the name "bcom" instead of "form_bcom" in db





# Bjmc Temporary Records Model:
class BjmcTemp(models.Model):
    # application id (auto generated)
    application_id = models.CharField(max_length=100, unique=True)
    #GGSIPU registration no.
    ipu_registration = models.PositiveBigIntegerField(blank=True, unique=True)
    #candidate details
    candidate_first_name = models.CharField(max_length=100, blank=True)
    candidate_middle_name = models.CharField(max_length=100, blank=True)
    candidate_last_name = models.CharField(max_length=100, blank=True)
    #other candidate details
    dob = models.DateField()
    complete_address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True, unique=False)
    candidate_number = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    #father mother details
    father_first_name = models.CharField(max_length=100, blank=True)
    father_middle_name = models.CharField(max_length=100, blank=True)
    father_last_name = models.CharField(max_length=100, blank=True)
    mother_first_name = models.CharField(max_length=100, blank=True)
    mother_middle_name = models.CharField(max_length=100, blank=True)
    mother_last_name = models.CharField(max_length=100, blank=True)
    father_qualification = models.CharField(max_length=100, blank=True)
    mother_qualification = models.CharField(max_length=100, blank=True)
    father_job = models.CharField(max_length=100, blank=True)
    mother_job = models.CharField(max_length=100, blank=True)
    father_job_designation = models.CharField(max_length=100, blank=True)
    mother_job_designation = models.CharField(max_length=100, blank=True)
    father_business_type = models.CharField(max_length=100, blank=True)
    mother_business_type = models.CharField(max_length=100, blank=True)
    father_number = models.CharField(max_length=100, blank=True)
    mother_number = models.CharField(max_length=100, blank=True)
    father_office_address = models.CharField(max_length=100, blank=True)
    mother_office_address = models.CharField(max_length=100, blank=True)
    #guardian details
    guardian_name = models.CharField(max_length=75, blank=True)
    #12th class details
    board_12th = models.CharField(max_length=255, blank=True)
    year_of_12th = models.PositiveIntegerField(blank=True, null=True)
    rollno_12th = models.PositiveBigIntegerField(blank=True, null=True)
    school_12th = models.CharField(max_length=255, blank=True)
    aggregate_12th = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    first_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    second_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    third_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    fourth_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_12th = models.CharField(max_length=10, blank=True)     # because integer field was giving error even with null=True and Blank=True
    other_subject_2_12th =  models.CharField(max_length=10, blank=True)
    #10th class details
    board_10th = models.CharField(max_length=255, blank=True)
    year_of_10th = models.PositiveIntegerField(blank=True, null=True)
    rollno_10th = models.PositiveBigIntegerField(blank=True, null=True)
    school_10th = models.CharField(max_length=255, blank=True)
    aggregate_10th = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    maths_10th = models.PositiveIntegerField(blank=True, null=True)
    science_10th = models.PositiveIntegerField(blank=True, null=True)
    english_10th = models.PositiveIntegerField(blank=True, null=True)
    sst_10th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_10th = models.CharField(max_length=100, blank=True)   # because integer field was giving error even with null=True and Blank=True
    other_subject_2_10th =  models.CharField(max_length=100, blank=True)
    #CET details
    cet_or_cuet = models.CharField(max_length=10)    # to ask user which paper did he/she appear for
    cet_rank = models.PositiveIntegerField(blank=True, null=True)
    cet_rollno = models.CharField(max_length=100, blank=True)
    #special acheivements
    special_achievements = models.CharField(max_length=255, blank=True)
    #images and files
    passport_photo = models.ImageField(upload_to=utils.bjmc_photo_rename, blank=True)
    cet_result = models.FileField(upload_to=utils.bjmc_cetresult_rename, blank=True)
    marksheet_10th = models.FileField(upload_to=utils.bjmc_10thmarksheet_rename, blank=True)
    marksheet_12th = models.FileField(upload_to=utils.bjmc_12thmarksheet_rename, blank=True)
    aadhaar = models.FileField(upload_to=utils.bjmc_aadhar_rename, blank=True)
    pancard = models.FileField(upload_to=utils.bjmc_pancard_rename, blank=True)
    ipuregistrationproof = models.FileField(upload_to=utils.bjmc_ipuregistration_rename, blank=True)
    # Transaction Details
    transaction_id = models.CharField(max_length=255, blank=True)
    transaction_proof = models.FileField(upload_to=utils.bjmc_transaction_rename, blank=True)
    # Counselling Fee Details
    counselling_transaction_id = models.CharField(max_length=255, blank=True)
    counselling_transaction_proof = models.FileField(upload_to=utils.bjmc_counselling_transaction_rename, blank=True)
    # To track IP address and other information of users
    ip_address = models.CharField(max_length=100, blank=True, null=True)
    forwarded_address = models.CharField(max_length=255, blank=True ,null=True)
    browser_info = models.CharField(max_length=1000, blank=True ,null=True)
    created_at = models.CharField(max_length=255, blank=True ,null=True)

    def __str__(self):         # for showing record by name in admin panel
        return (self.candidate_first_name+' '+self.candidate_last_name)

    def photograph_preview(self):   #for previewing photo in admin panel
        return mark_safe(f'<img src = "{self.passport_photo.url}" width = "100"/>')

    class Meta:
        verbose_name_plural = "BA(JMC) Temporary"    # to show table by this name in admin panel
        db_table = "bjmc_temp"             # to use the name "bjmc_temp" instead of "form_bjmc_temp" in db 


# Bjmc Model:
class Bjmc(models.Model):
    # application id (auto generated)
    application_id = models.CharField(max_length=100, unique=True)
    #GGSIPU registration no.
    ipu_registration = models.PositiveBigIntegerField(blank=True, unique=True)
    # allowed for counselling
    allow_for_counselling = models.BooleanField(default=False)
    # allow for editing of record
    allow_editing = models.BooleanField(default=False)
    #candidate details
    candidate_first_name = models.CharField(max_length=100, blank=True)
    candidate_middle_name = models.CharField(max_length=100, blank=True)
    candidate_last_name = models.CharField(max_length=100, blank=True)
    #other candidate details
    dob = models.DateField()
    complete_address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True, unique=False)
    candidate_number = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    #father mother details
    father_first_name = models.CharField(max_length=100, blank=True)
    father_middle_name = models.CharField(max_length=100, blank=True)
    father_last_name = models.CharField(max_length=100, blank=True)
    mother_first_name = models.CharField(max_length=100, blank=True)
    mother_middle_name = models.CharField(max_length=100, blank=True)
    mother_last_name = models.CharField(max_length=100, blank=True)
    father_qualification = models.CharField(max_length=100, blank=True)
    mother_qualification = models.CharField(max_length=100, blank=True)
    father_job = models.CharField(max_length=100, blank=True)
    mother_job = models.CharField(max_length=100, blank=True)
    father_job_designation = models.CharField(max_length=100, blank=True)
    mother_job_designation = models.CharField(max_length=100, blank=True)
    father_business_type = models.CharField(max_length=100, blank=True)
    mother_business_type = models.CharField(max_length=100, blank=True)
    father_number = models.CharField(max_length=100, blank=True)
    mother_number = models.CharField(max_length=100, blank=True)
    father_office_address = models.CharField(max_length=100, blank=True)
    mother_office_address = models.CharField(max_length=100, blank=True)
    #guardian details
    guardian_name = models.CharField(max_length=75, blank=True)
    #12th class details
    board_12th = models.CharField(max_length=255, blank=True)
    year_of_12th = models.PositiveIntegerField(blank=True)
    rollno_12th = models.PositiveBigIntegerField(blank=True)
    school_12th = models.CharField(max_length=255, blank=True)
    aggregate_12th = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    first_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    second_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    third_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    fourth_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_12th = models.CharField(max_length=10, blank=True)     # because integer field was giving error even with null=True and Blank=True
    other_subject_2_12th =  models.CharField(max_length=10, blank=True)
    #10th class details
    board_10th = models.CharField(max_length=255, blank=True)
    year_of_10th = models.PositiveIntegerField(blank=True)
    rollno_10th = models.PositiveBigIntegerField(blank=True)
    school_10th = models.CharField(max_length=255, blank=True)
    aggregate_10th = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    maths_10th = models.PositiveIntegerField(blank=True)
    science_10th = models.PositiveIntegerField(blank=True)
    english_10th = models.PositiveIntegerField(blank=True)
    sst_10th = models.PositiveIntegerField(blank=True)
    other_subject_10th = models.CharField(max_length=100, blank=True)   # because integer field was giving error even with null=True and Blank=True
    other_subject_2_10th =  models.CharField(max_length=100, blank=True)
    #CET details
    cet_or_cuet = models.CharField(max_length=10)    # to ask user which paper did he/she appear for
    cet_rank = models.PositiveIntegerField(blank=True, null=True)
    cet_rollno = models.CharField(max_length=255, blank=True)
    #special acheivements
    special_achievements = models.CharField(max_length=255, blank=True)
    #images and files
    passport_photo = models.ImageField(upload_to=utils.bjmc_photo_rename, blank=True)
    cet_result = models.FileField(upload_to=utils.bjmc_cetresult_rename, blank=True)
    marksheet_10th = models.FileField(upload_to=utils.bjmc_10thmarksheet_rename, blank=True)
    marksheet_12th = models.FileField(upload_to=utils.bjmc_12thmarksheet_rename, blank=True)
    aadhaar = models.FileField(upload_to=utils.bjmc_aadhar_rename, blank=True)
    pancard = models.FileField(upload_to=utils.bjmc_pancard_rename, blank=True)
    ipuregistrationproof = models.FileField(upload_to=utils.bjmc_ipuregistration_rename, blank=True)
    # Transaction Details
    transaction_id = models.CharField(max_length=255, blank=True)
    transaction_proof = models.FileField(upload_to=utils.bjmc_transaction_rename, blank=True)
    # Counselling Fee Details
    counselling_transaction_id = models.CharField(max_length=255, blank=True)
    counselling_transaction_proof = models.FileField(upload_to=utils.bjmc_counselling_transaction_rename, blank=True)
    # To track IP address and other information of users
    ip_address = models.CharField(max_length=100, blank=True, null=True)
    forwarded_address = models.CharField(max_length=255, blank=True ,null=True)
    browser_info = models.CharField(max_length=1000, blank=True ,null=True)
    created_at = models.CharField(max_length=255, blank=True ,null=True)

    def __str__(self):         # for showing record by name in admin panel
        return (self.candidate_first_name+' '+self.candidate_last_name)

    def photograph_preview(self):   #for previewing photo in admin panel
        return mark_safe(f'<img src = "{self.passport_photo.url}" width = "100"/>')

    class Meta:
        verbose_name_plural = "BA(JMC)"    # to show table by this name in admin panel
        db_table = "bjmc"             # to use the name "bjmc" instead of "form_bjmc" in db




# BaLLB Temporary Records Model:
class BallbTemp(models.Model):
    # application id (auto generated)
    application_id = models.CharField(max_length=100, unique=True)
    #GGSIPU registration no.
    ipu_registration = models.PositiveBigIntegerField(blank=True, unique=True)
    #candidate details
    candidate_first_name = models.CharField(max_length=100, blank=True)
    candidate_middle_name = models.CharField(max_length=100, blank=True)
    candidate_last_name = models.CharField(max_length=100, blank=True)
    #other candidate details
    dob = models.DateField()
    complete_address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True, unique=False)
    candidate_number = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    #father mother details
    father_first_name = models.CharField(max_length=100, blank=True)
    father_middle_name = models.CharField(max_length=100, blank=True)
    father_last_name = models.CharField(max_length=100, blank=True)
    mother_first_name = models.CharField(max_length=100, blank=True)
    mother_middle_name = models.CharField(max_length=100, blank=True)
    mother_last_name = models.CharField(max_length=100, blank=True)
    father_qualification = models.CharField(max_length=100, blank=True)
    mother_qualification = models.CharField(max_length=100, blank=True)
    father_job = models.CharField(max_length=100, blank=True)
    mother_job = models.CharField(max_length=100, blank=True)
    father_job_designation = models.CharField(max_length=100, blank=True)
    mother_job_designation = models.CharField(max_length=100, blank=True)
    father_business_type = models.CharField(max_length=100, blank=True)
    mother_business_type = models.CharField(max_length=100, blank=True)
    father_number = models.CharField(max_length=100, blank=True)
    mother_number = models.CharField(max_length=100, blank=True)
    father_office_address = models.CharField(max_length=100, blank=True)
    mother_office_address = models.CharField(max_length=100, blank=True)
    #guardian details
    guardian_name = models.CharField(max_length=75, blank=True)
    #12th class details
    board_12th = models.CharField(max_length=255, blank=True)
    year_of_12th = models.PositiveIntegerField(blank=True, null=True)
    rollno_12th = models.PositiveBigIntegerField(blank=True, null=True)
    school_12th = models.CharField(max_length=255, blank=True)
    aggregate_12th = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    first_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    second_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    third_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    fourth_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_12th = models.CharField(max_length=10, blank=True)     # because integer field was giving error even with null=True and Blank=True
    other_subject_2_12th =  models.CharField(max_length=10, blank=True)
    #10th class details
    board_10th = models.CharField(max_length=255, blank=True)
    year_of_10th = models.PositiveIntegerField(blank=True, null=True)
    rollno_10th = models.PositiveBigIntegerField(blank=True, null=True)
    school_10th = models.CharField(max_length=255, blank=True)
    aggregate_10th = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    maths_10th = models.PositiveIntegerField(blank=True, null=True)
    science_10th = models.PositiveIntegerField(blank=True, null=True)
    english_10th = models.PositiveIntegerField(blank=True, null=True)
    sst_10th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_10th = models.CharField(max_length=100, blank=True)   # because integer field was giving error even with null=True and Blank=True
    other_subject_2_10th =  models.CharField(max_length=100, blank=True)
    #CET details
    cet_or_cuet = models.CharField(max_length=10)    # to ask user which paper did he/she appear for
    cet_rank = models.PositiveIntegerField(blank=True, null=True)
    cet_rollno = models.CharField(max_length=100, blank=True)
    #special acheivements
    special_achievements = models.CharField(max_length=255, blank=True)
    #images and files
    passport_photo = models.ImageField(upload_to=utils.ballb_photo_rename, blank=True)
    cet_result = models.FileField(upload_to=utils.ballb_cetresult_rename, blank=True)
    marksheet_10th = models.FileField(upload_to=utils.ballb_10thmarksheet_rename, blank=True)
    marksheet_12th = models.FileField(upload_to=utils.ballb_12thmarksheet_rename, blank=True)
    aadhaar = models.FileField(upload_to=utils.ballb_aadhar_rename, blank=True)
    pancard = models.FileField(upload_to=utils.ballb_pancard_rename, blank=True)
    ipuregistrationproof = models.FileField(upload_to=utils.ballb_ipuregistration_rename, blank=True)
    # Transaction Details
    transaction_id = models.CharField(max_length=255, blank=True)
    transaction_proof = models.FileField(upload_to=utils.ballb_transaction_rename, blank=True)
    # Counselling Fee Details
    counselling_transaction_id = models.CharField(max_length=255, blank=True)
    counselling_transaction_proof = models.FileField(upload_to=utils.ballb_counselling_transaction_rename, blank=True)
    # To track IP address and other information of users
    ip_address = models.CharField(max_length=100, blank=True, null=True)
    forwarded_address = models.CharField(max_length=255, blank=True ,null=True)
    browser_info = models.CharField(max_length=1000, blank=True ,null=True)
    created_at = models.CharField(max_length=255, blank=True ,null=True)

    def __str__(self):         # for showing record by name in admin panel
        return (self.candidate_first_name+' '+self.candidate_last_name)

    def photograph_preview(self):   #for previewing photo in admin panel
        return mark_safe(f'<img src = "{self.passport_photo.url}" width = "100"/>')

    class Meta:
        verbose_name_plural = "B.A. LLB Temporary"    # to show table by this name in admin panel
        db_table = "ballb_temp"             # to use the name "ballb_temp" instead of "form_ballb_temp" in db 


# ballb Model:
class Ballb(models.Model):
    # application id (auto generated)
    application_id = models.CharField(max_length=100, unique=True)
    #GGSIPU registration no.
    ipu_registration = models.PositiveBigIntegerField(blank=True, unique=True)
    # allowed for counselling
    allow_for_counselling = models.BooleanField(default=False)
    # allow for editing of record
    allow_editing = models.BooleanField(default=False)
    #candidate details
    candidate_first_name = models.CharField(max_length=100, blank=True)
    candidate_middle_name = models.CharField(max_length=100, blank=True)
    candidate_last_name = models.CharField(max_length=100, blank=True)
    #other candidate details
    dob = models.DateField()
    complete_address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True, unique=False)
    candidate_number = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    #father mother details
    father_first_name = models.CharField(max_length=100, blank=True)
    father_middle_name = models.CharField(max_length=100, blank=True)
    father_last_name = models.CharField(max_length=100, blank=True)
    mother_first_name = models.CharField(max_length=100, blank=True)
    mother_middle_name = models.CharField(max_length=100, blank=True)
    mother_last_name = models.CharField(max_length=100, blank=True)
    father_qualification = models.CharField(max_length=100, blank=True)
    mother_qualification = models.CharField(max_length=100, blank=True)
    father_job = models.CharField(max_length=100, blank=True)
    mother_job = models.CharField(max_length=100, blank=True)
    father_job_designation = models.CharField(max_length=100, blank=True)
    mother_job_designation = models.CharField(max_length=100, blank=True)
    father_business_type = models.CharField(max_length=100, blank=True)
    mother_business_type = models.CharField(max_length=100, blank=True)
    father_number = models.CharField(max_length=100, blank=True)
    mother_number = models.CharField(max_length=100, blank=True)
    father_office_address = models.CharField(max_length=100, blank=True)
    mother_office_address = models.CharField(max_length=100, blank=True)
    #guardian details
    guardian_name = models.CharField(max_length=75, blank=True)
    #12th class details
    board_12th = models.CharField(max_length=255, blank=True)
    year_of_12th = models.PositiveIntegerField(blank=True)
    rollno_12th = models.PositiveBigIntegerField(blank=True)
    school_12th = models.CharField(max_length=255, blank=True)
    aggregate_12th = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    first_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    second_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    third_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    fourth_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_12th = models.CharField(max_length=10, blank=True)     # because integer field was giving error even with null=True and Blank=True
    other_subject_2_12th =  models.CharField(max_length=10, blank=True)
    #10th class details
    board_10th = models.CharField(max_length=255, blank=True)
    year_of_10th = models.PositiveIntegerField(blank=True)
    rollno_10th = models.PositiveBigIntegerField(blank=True)
    school_10th = models.CharField(max_length=255, blank=True)
    aggregate_10th = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    maths_10th = models.PositiveIntegerField(blank=True)
    science_10th = models.PositiveIntegerField(blank=True)
    english_10th = models.PositiveIntegerField(blank=True)
    sst_10th = models.PositiveIntegerField(blank=True)
    other_subject_10th = models.CharField(max_length=100, blank=True)   # because integer field was giving error even with null=True and Blank=True
    other_subject_2_10th =  models.CharField(max_length=100, blank=True)
    #CET details
    cet_or_cuet = models.CharField(max_length=10)    # to ask user which paper did he/she appear for
    cet_rank = models.PositiveIntegerField(blank=True, null=True)
    cet_rollno = models.CharField(max_length=255, blank=True)
    #special acheivements
    special_achievements = models.CharField(max_length=255, blank=True)
    #images and files
    passport_photo = models.ImageField(upload_to=utils.ballb_photo_rename, blank=True)
    cet_result = models.FileField(upload_to=utils.ballb_cetresult_rename, blank=True)
    marksheet_10th = models.FileField(upload_to=utils.ballb_10thmarksheet_rename, blank=True)
    marksheet_12th = models.FileField(upload_to=utils.ballb_12thmarksheet_rename, blank=True)
    aadhaar = models.FileField(upload_to=utils.ballb_aadhar_rename, blank=True)
    pancard = models.FileField(upload_to=utils.ballb_pancard_rename, blank=True)
    ipuregistrationproof = models.FileField(upload_to=utils.ballb_ipuregistration_rename, blank=True)
    # Transaction Details
    transaction_id = models.CharField(max_length=255, blank=True)
    transaction_proof = models.FileField(upload_to=utils.ballb_transaction_rename, blank=True)
    # Counselling Fee Details
    counselling_transaction_id = models.CharField(max_length=255, blank=True)
    counselling_transaction_proof = models.FileField(upload_to=utils.ballb_counselling_transaction_rename, blank=True)
    # To track IP address and other information of users
    ip_address = models.CharField(max_length=100, blank=True, null=True)
    forwarded_address = models.CharField(max_length=255, blank=True ,null=True)
    browser_info = models.CharField(max_length=1000, blank=True ,null=True)
    created_at = models.CharField(max_length=255, blank=True ,null=True)

    def __str__(self):         # for showing record by name in admin panel
        return (self.candidate_first_name+' '+self.candidate_last_name)

    def photograph_preview(self):   #for previewing photo in admin panel
        return mark_safe(f'<img src = "{self.passport_photo.url}" width = "100"/>')

    class Meta:
        verbose_name_plural = "B.A. LLB"    # to show table by this name in admin panel
        db_table = "ballb"             # to use the name "ballb" instead of "form_ballb" in db




# BBAllb Temporary Records Model:
class BballbTemp(models.Model):
    # application id (auto generated)
    application_id = models.CharField(max_length=100, unique=True)
    #GGSIPU registration no.
    ipu_registration = models.PositiveBigIntegerField(blank=True, unique=True)
    #candidate details
    candidate_first_name = models.CharField(max_length=100, blank=True)
    candidate_middle_name = models.CharField(max_length=100, blank=True)
    candidate_last_name = models.CharField(max_length=100, blank=True)
    #other candidate details
    dob = models.DateField()
    complete_address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True, unique=False)
    candidate_number = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    #father mother details
    father_first_name = models.CharField(max_length=100, blank=True)
    father_middle_name = models.CharField(max_length=100, blank=True)
    father_last_name = models.CharField(max_length=100, blank=True)
    mother_first_name = models.CharField(max_length=100, blank=True)
    mother_middle_name = models.CharField(max_length=100, blank=True)
    mother_last_name = models.CharField(max_length=100, blank=True)
    father_qualification = models.CharField(max_length=100, blank=True)
    mother_qualification = models.CharField(max_length=100, blank=True)
    father_job = models.CharField(max_length=100, blank=True)
    mother_job = models.CharField(max_length=100, blank=True)
    father_job_designation = models.CharField(max_length=100, blank=True)
    mother_job_designation = models.CharField(max_length=100, blank=True)
    father_business_type = models.CharField(max_length=100, blank=True)
    mother_business_type = models.CharField(max_length=100, blank=True)
    father_number = models.CharField(max_length=100, blank=True)
    mother_number = models.CharField(max_length=100, blank=True)
    father_office_address = models.CharField(max_length=100, blank=True)
    mother_office_address = models.CharField(max_length=100, blank=True)
    #guardian details
    guardian_name = models.CharField(max_length=75, blank=True)
    #12th class details
    board_12th = models.CharField(max_length=255, blank=True)
    year_of_12th = models.PositiveIntegerField(blank=True, null=True)
    rollno_12th = models.PositiveBigIntegerField(blank=True, null=True)
    school_12th = models.CharField(max_length=255, blank=True)
    aggregate_12th = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    first_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    second_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    third_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    fourth_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_12th = models.CharField(max_length=10, blank=True)     # because integer field was giving error even with null=True and Blank=True
    other_subject_2_12th =  models.CharField(max_length=10, blank=True)
    #10th class details
    board_10th = models.CharField(max_length=255, blank=True)
    year_of_10th = models.PositiveIntegerField(blank=True, null=True)
    rollno_10th = models.PositiveBigIntegerField(blank=True, null=True)
    school_10th = models.CharField(max_length=255, blank=True)
    aggregate_10th = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    maths_10th = models.PositiveIntegerField(blank=True, null=True)
    science_10th = models.PositiveIntegerField(blank=True, null=True)
    english_10th = models.PositiveIntegerField(blank=True, null=True)
    sst_10th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_10th = models.CharField(max_length=100, blank=True)   # because integer field was giving error even with null=True and Blank=True
    other_subject_2_10th =  models.CharField(max_length=100, blank=True)
    #CET details
    cet_or_cuet = models.CharField(max_length=10)    # to ask user which paper did he/she appear for
    cet_rank = models.PositiveIntegerField(blank=True, null=True)
    cet_rollno = models.CharField(max_length=100, blank=True)
    #special acheivements
    special_achievements = models.CharField(max_length=255, blank=True)
    #images and files
    passport_photo = models.ImageField(upload_to=utils.bballb_photo_rename, blank=True)
    cet_result = models.FileField(upload_to=utils.bballb_cetresult_rename, blank=True)
    marksheet_10th = models.FileField(upload_to=utils.bballb_10thmarksheet_rename, blank=True)
    marksheet_12th = models.FileField(upload_to=utils.bballb_12thmarksheet_rename, blank=True)
    aadhaar = models.FileField(upload_to=utils.bballb_aadhar_rename, blank=True)
    pancard = models.FileField(upload_to=utils.bballb_pancard_rename, blank=True)
    ipuregistrationproof = models.FileField(upload_to=utils.bballb_ipuregistration_rename, blank=True)
    # Transaction Details
    transaction_id = models.CharField(max_length=255, blank=True)
    transaction_proof = models.FileField(upload_to=utils.bballb_transaction_rename, blank=True)
    # Counselling Fee Details
    counselling_transaction_id = models.CharField(max_length=255, blank=True)
    counselling_transaction_proof = models.FileField(upload_to=utils.bballb_counselling_transaction_rename, blank=True)
    # To track IP address and other information of users
    ip_address = models.CharField(max_length=100, blank=True, null=True)
    forwarded_address = models.CharField(max_length=255, blank=True ,null=True)
    browser_info = models.CharField(max_length=1000, blank=True ,null=True)
    created_at = models.CharField(max_length=255, blank=True ,null=True)

    def __str__(self):         # for showing record by name in admin panel
        return (self.candidate_first_name+' '+self.candidate_last_name)

    def photograph_preview(self):   #for previewing photo in admin panel
        return mark_safe(f'<img src = "{self.passport_photo.url}" width = "100"/>')

    class Meta:
        verbose_name_plural = "BBA LLB Temporary"    # to show table by this name in admin panel
        db_table = "bballb_temp"             # to use the name "bballb_temp" instead of "form_bballb_temp" in db 


# bballb Model:
class Bballb(models.Model):
    # application id (auto generated)
    application_id = models.CharField(max_length=100, unique=True)
    #GGSIPU registration no.
    ipu_registration = models.PositiveBigIntegerField(blank=True, unique=True)
    # allowed for counselling
    allow_for_counselling = models.BooleanField(default=False)
    # allow for editing of record
    allow_editing = models.BooleanField(default=False)
    #candidate details
    candidate_first_name = models.CharField(max_length=100, blank=True)
    candidate_middle_name = models.CharField(max_length=100, blank=True)
    candidate_last_name = models.CharField(max_length=100, blank=True)
    #other candidate details
    dob = models.DateField()
    complete_address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True, unique=False)
    candidate_number = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    #father mother details
    father_first_name = models.CharField(max_length=100, blank=True)
    father_middle_name = models.CharField(max_length=100, blank=True)
    father_last_name = models.CharField(max_length=100, blank=True)
    mother_first_name = models.CharField(max_length=100, blank=True)
    mother_middle_name = models.CharField(max_length=100, blank=True)
    mother_last_name = models.CharField(max_length=100, blank=True)
    father_qualification = models.CharField(max_length=100, blank=True)
    mother_qualification = models.CharField(max_length=100, blank=True)
    father_job = models.CharField(max_length=100, blank=True)
    mother_job = models.CharField(max_length=100, blank=True)
    father_job_designation = models.CharField(max_length=100, blank=True)
    mother_job_designation = models.CharField(max_length=100, blank=True)
    father_business_type = models.CharField(max_length=100, blank=True)
    mother_business_type = models.CharField(max_length=100, blank=True)
    father_number = models.CharField(max_length=100, blank=True)
    mother_number = models.CharField(max_length=100, blank=True)
    father_office_address = models.CharField(max_length=100, blank=True)
    mother_office_address = models.CharField(max_length=100, blank=True)
    #guardian details
    guardian_name = models.CharField(max_length=75, blank=True)
    #12th class details
    board_12th = models.CharField(max_length=255, blank=True)
    year_of_12th = models.PositiveIntegerField(blank=True)
    rollno_12th = models.PositiveBigIntegerField(blank=True)
    school_12th = models.CharField(max_length=255, blank=True)
    aggregate_12th = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    first_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    second_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    third_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    fourth_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_12th = models.CharField(max_length=10, blank=True)     # because integer field was giving error even with null=True and Blank=True
    other_subject_2_12th =  models.CharField(max_length=10, blank=True)
    #10th class details
    board_10th = models.CharField(max_length=255, blank=True)
    year_of_10th = models.PositiveIntegerField(blank=True)
    rollno_10th = models.PositiveBigIntegerField(blank=True)
    school_10th = models.CharField(max_length=255, blank=True)
    aggregate_10th = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    maths_10th = models.PositiveIntegerField(blank=True)
    science_10th = models.PositiveIntegerField(blank=True)
    english_10th = models.PositiveIntegerField(blank=True)
    sst_10th = models.PositiveIntegerField(blank=True)
    other_subject_10th = models.CharField(max_length=100, blank=True)   # because integer field was giving error even with null=True and Blank=True
    other_subject_2_10th =  models.CharField(max_length=100, blank=True)
    #CET details
    cet_or_cuet = models.CharField(max_length=10)    # to ask user which paper did he/she appear for
    cet_rank = models.PositiveIntegerField(blank=True, null=True)
    cet_rollno = models.CharField(max_length=255, blank=True)
    #special acheivements
    special_achievements = models.CharField(max_length=255, blank=True)
    #images and files
    passport_photo = models.ImageField(upload_to=utils.bballb_photo_rename, blank=True)
    cet_result = models.FileField(upload_to=utils.bballb_cetresult_rename, blank=True)
    marksheet_10th = models.FileField(upload_to=utils.bballb_10thmarksheet_rename, blank=True)
    marksheet_12th = models.FileField(upload_to=utils.bballb_12thmarksheet_rename, blank=True)
    aadhaar = models.FileField(upload_to=utils.bballb_aadhar_rename, blank=True)
    pancard = models.FileField(upload_to=utils.bballb_pancard_rename, blank=True)
    ipuregistrationproof = models.FileField(upload_to=utils.bballb_ipuregistration_rename, blank=True)
    # Transaction Details
    transaction_id = models.CharField(max_length=255, blank=True)
    transaction_proof = models.FileField(upload_to=utils.bballb_transaction_rename, blank=True)
    # Counselling Fee Details
    counselling_transaction_id = models.CharField(max_length=255, blank=True)
    counselling_transaction_proof = models.FileField(upload_to=utils.bballb_counselling_transaction_rename, blank=True)
    # To track IP address and other information of users
    ip_address = models.CharField(max_length=100, blank=True, null=True)
    forwarded_address = models.CharField(max_length=255, blank=True ,null=True)
    browser_info = models.CharField(max_length=1000, blank=True ,null=True)
    created_at = models.CharField(max_length=255, blank=True ,null=True)

    def __str__(self):         # for showing record by name in admin panel
        return (self.candidate_first_name+' '+self.candidate_last_name)

    def photograph_preview(self):   #for previewing photo in admin panel
        return mark_safe(f'<img src = "{self.passport_photo.url}" width = "100"/>')

    class Meta:
        verbose_name_plural = "BBA LLB"    # to show table by this name in admin panel
        db_table = "bballb"             # to use the name "bballb" instead of "form_bballb" in db






# Eco Temporary Records Model:
class EcoTemp(models.Model):
    # application id (auto generated)
    application_id = models.CharField(max_length=100, unique=True)
    #GGSIPU registration no.
    ipu_registration = models.PositiveBigIntegerField(blank=True, unique=True)
    #candidate details
    candidate_first_name = models.CharField(max_length=100, blank=True)
    candidate_middle_name = models.CharField(max_length=100, blank=True)
    candidate_last_name = models.CharField(max_length=100, blank=True)
    #other candidate details
    dob = models.DateField()
    complete_address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True, unique=False)
    candidate_number = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    #father mother details
    father_first_name = models.CharField(max_length=100, blank=True)
    father_middle_name = models.CharField(max_length=100, blank=True)
    father_last_name = models.CharField(max_length=100, blank=True)
    mother_first_name = models.CharField(max_length=100, blank=True)
    mother_middle_name = models.CharField(max_length=100, blank=True)
    mother_last_name = models.CharField(max_length=100, blank=True)
    father_qualification = models.CharField(max_length=100, blank=True)
    mother_qualification = models.CharField(max_length=100, blank=True)
    father_job = models.CharField(max_length=100, blank=True)
    mother_job = models.CharField(max_length=100, blank=True)
    father_job_designation = models.CharField(max_length=100, blank=True)
    mother_job_designation = models.CharField(max_length=100, blank=True)
    father_business_type = models.CharField(max_length=100, blank=True)
    mother_business_type = models.CharField(max_length=100, blank=True)
    father_number = models.CharField(max_length=100, blank=True)
    mother_number = models.CharField(max_length=100, blank=True)
    father_office_address = models.CharField(max_length=100, blank=True)
    mother_office_address = models.CharField(max_length=100, blank=True)
    #guardian details
    guardian_name = models.CharField(max_length=75, blank=True)
    #12th class details
    board_12th = models.CharField(max_length=255, blank=True)
    year_of_12th = models.PositiveIntegerField(blank=True, null=True)
    rollno_12th = models.PositiveBigIntegerField(blank=True, null=True)
    school_12th = models.CharField(max_length=255, blank=True)
    aggregate_12th = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    first_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    second_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    third_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    fourth_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_12th = models.CharField(max_length=10, blank=True)     # because integer field was giving error even with null=True and Blank=True
    other_subject_2_12th =  models.CharField(max_length=10, blank=True)
    #10th class details
    board_10th = models.CharField(max_length=255, blank=True)
    year_of_10th = models.PositiveIntegerField(blank=True, null=True)
    rollno_10th = models.PositiveBigIntegerField(blank=True, null=True)
    school_10th = models.CharField(max_length=255, blank=True)
    aggregate_10th = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    maths_10th = models.PositiveIntegerField(blank=True, null=True)
    science_10th = models.PositiveIntegerField(blank=True, null=True)
    english_10th = models.PositiveIntegerField(blank=True, null=True)
    sst_10th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_10th = models.CharField(max_length=100, blank=True)   # because integer field was giving error even with null=True and Blank=True
    other_subject_2_10th =  models.CharField(max_length=100, blank=True)
    #CET details
    cet_or_cuet = models.CharField(max_length=10)    # to ask user which paper did he/she appear for
    cet_rank = models.PositiveIntegerField(blank=True, null=True)
    cet_rollno = models.CharField(max_length=100, blank=True)
    #special acheivements
    special_achievements = models.CharField(max_length=255, blank=True)
    #images and files
    passport_photo = models.ImageField(upload_to=utils.eco_photo_rename, blank=True)
    cet_result = models.FileField(upload_to=utils.eco_cetresult_rename, blank=True)
    marksheet_10th = models.FileField(upload_to=utils.eco_10thmarksheet_rename, blank=True)
    marksheet_12th = models.FileField(upload_to=utils.eco_12thmarksheet_rename, blank=True)
    aadhaar = models.FileField(upload_to=utils.eco_aadhar_rename, blank=True)
    pancard = models.FileField(upload_to=utils.eco_pancard_rename, blank=True)
    ipuregistrationproof = models.FileField(upload_to=utils.eco_ipuregistration_rename, blank=True)
    # Transaction Details
    transaction_id = models.CharField(max_length=255, blank=True)
    transaction_proof = models.FileField(upload_to=utils.eco_transaction_rename, blank=True)
    # Counselling Fee Details
    counselling_transaction_id = models.CharField(max_length=255, blank=True)
    counselling_transaction_proof = models.FileField(upload_to=utils.eco_counselling_transaction_rename, blank=True)
    # To track IP address and other information of users
    ip_address = models.CharField(max_length=100, blank=True, null=True)
    forwarded_address = models.CharField(max_length=255, blank=True ,null=True)
    browser_info = models.CharField(max_length=1000, blank=True ,null=True)
    created_at = models.CharField(max_length=255, blank=True ,null=True)

    def __str__(self):         # for showing record by name in admin panel
        return (self.candidate_first_name+' '+self.candidate_last_name)

    def photograph_preview(self):   #for previewing photo in admin panel
        return mark_safe(f'<img src = "{self.passport_photo.url}" width = "100"/>')

    class Meta:
        verbose_name_plural = "Eco Hons Temporary"    # to show table by this name in admin panel
        db_table = "eco_temp"             # to use the name "eco_temp" instead of "form_eco_temp" in db 


# eco Model:
class Eco(models.Model):
    # application id (auto generated)
    application_id = models.CharField(max_length=100, unique=True)
    #GGSIPU registration no.
    ipu_registration = models.PositiveBigIntegerField(blank=True, unique=True)
    # allowed for counselling
    allow_for_counselling = models.BooleanField(default=False)
    # allow for editing of record
    allow_editing = models.BooleanField(default=False)
    #candidate details
    candidate_first_name = models.CharField(max_length=100, blank=True)
    candidate_middle_name = models.CharField(max_length=100, blank=True)
    candidate_last_name = models.CharField(max_length=100, blank=True)
    #other candidate details
    dob = models.DateField()
    complete_address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True, unique=False)
    candidate_number = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    #father mother details
    father_first_name = models.CharField(max_length=100, blank=True)
    father_middle_name = models.CharField(max_length=100, blank=True)
    father_last_name = models.CharField(max_length=100, blank=True)
    mother_first_name = models.CharField(max_length=100, blank=True)
    mother_middle_name = models.CharField(max_length=100, blank=True)
    mother_last_name = models.CharField(max_length=100, blank=True)
    father_qualification = models.CharField(max_length=100, blank=True)
    mother_qualification = models.CharField(max_length=100, blank=True)
    father_job = models.CharField(max_length=100, blank=True)
    mother_job = models.CharField(max_length=100, blank=True)
    father_job_designation = models.CharField(max_length=100, blank=True)
    mother_job_designation = models.CharField(max_length=100, blank=True)
    father_business_type = models.CharField(max_length=100, blank=True)
    mother_business_type = models.CharField(max_length=100, blank=True)
    father_number = models.CharField(max_length=100, blank=True)
    mother_number = models.CharField(max_length=100, blank=True)
    father_office_address = models.CharField(max_length=100, blank=True)
    mother_office_address = models.CharField(max_length=100, blank=True)
    #guardian details
    guardian_name = models.CharField(max_length=75, blank=True)
    #12th class details
    board_12th = models.CharField(max_length=255, blank=True)
    year_of_12th = models.PositiveIntegerField(blank=True)
    rollno_12th = models.PositiveBigIntegerField(blank=True)
    school_12th = models.CharField(max_length=255, blank=True)
    aggregate_12th = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    first_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    second_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    third_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    fourth_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_12th = models.CharField(max_length=10, blank=True)     # because integer field was giving error even with null=True and Blank=True
    other_subject_2_12th =  models.CharField(max_length=10, blank=True)
    #10th class details
    board_10th = models.CharField(max_length=255, blank=True)
    year_of_10th = models.PositiveIntegerField(blank=True)
    rollno_10th = models.PositiveBigIntegerField(blank=True)
    school_10th = models.CharField(max_length=255, blank=True)
    aggregate_10th = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    maths_10th = models.PositiveIntegerField(blank=True)
    science_10th = models.PositiveIntegerField(blank=True)
    english_10th = models.PositiveIntegerField(blank=True)
    sst_10th = models.PositiveIntegerField(blank=True)
    other_subject_10th = models.CharField(max_length=100, blank=True)   # because integer field was giving error even with null=True and Blank=True
    other_subject_2_10th =  models.CharField(max_length=100, blank=True)
    #CET details
    cet_or_cuet = models.CharField(max_length=10)    # to ask user which paper did he/she appear for
    cet_rank = models.PositiveIntegerField(blank=True, null=True)
    cet_rollno = models.CharField(max_length=255, blank=True)
    #special acheivements
    special_achievements = models.CharField(max_length=255, blank=True)
    #images and files
    passport_photo = models.ImageField(upload_to=utils.eco_photo_rename, blank=True)
    cet_result = models.FileField(upload_to=utils.eco_cetresult_rename, blank=True)
    marksheet_10th = models.FileField(upload_to=utils.eco_10thmarksheet_rename, blank=True)
    marksheet_12th = models.FileField(upload_to=utils.eco_12thmarksheet_rename, blank=True)
    aadhaar = models.FileField(upload_to=utils.eco_aadhar_rename, blank=True)
    pancard = models.FileField(upload_to=utils.eco_pancard_rename, blank=True)
    ipuregistrationproof = models.FileField(upload_to=utils.eco_ipuregistration_rename, blank=True)
    # Transaction Details
    transaction_id = models.CharField(max_length=255, blank=True)
    transaction_proof = models.FileField(upload_to=utils.eco_transaction_rename, blank=True)
    # Counselling Fee Details
    counselling_transaction_id = models.CharField(max_length=255, blank=True)
    counselling_transaction_proof = models.FileField(upload_to=utils.eco_counselling_transaction_rename, blank=True)
    # To track IP address and other information of users
    ip_address = models.CharField(max_length=100, blank=True, null=True)
    forwarded_address = models.CharField(max_length=255, blank=True ,null=True)
    browser_info = models.CharField(max_length=1000, blank=True ,null=True)
    created_at = models.CharField(max_length=255, blank=True ,null=True)

    def __str__(self):         # for showing record by name in admin panel
        return (self.candidate_first_name+' '+self.candidate_last_name)

    def photograph_preview(self):   #for previewing photo in admin panel
        return mark_safe(f'<img src = "{self.passport_photo.url}" width = "100"/>')

    class Meta:
        verbose_name_plural = "Eco Hons"    # to show table by this name in admin panel
        db_table = "eco"             # to use the name "eco" instead of "form_eco" in db








# LLM Temporary Records Model:
class LlmTemp(models.Model):
    # application id (auto generated)
    application_id = models.CharField(max_length=100, unique=True)
    #GGSIPU registration no.
    ipu_registration = models.PositiveBigIntegerField(blank=True, unique=True)
    #candidate details
    candidate_first_name = models.CharField(max_length=100, blank=True)
    candidate_middle_name = models.CharField(max_length=100, blank=True)
    candidate_last_name = models.CharField(max_length=100, blank=True)
    #other candidate details
    dob = models.DateField()
    complete_address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True, unique=False)
    candidate_number = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    #father mother details
    father_first_name = models.CharField(max_length=100, blank=True)
    father_middle_name = models.CharField(max_length=100, blank=True)
    father_last_name = models.CharField(max_length=100, blank=True)
    mother_first_name = models.CharField(max_length=100, blank=True)
    mother_middle_name = models.CharField(max_length=100, blank=True)
    mother_last_name = models.CharField(max_length=100, blank=True)
    father_qualification = models.CharField(max_length=100, blank=True)
    mother_qualification = models.CharField(max_length=100, blank=True)
    father_job = models.CharField(max_length=100, blank=True)
    mother_job = models.CharField(max_length=100, blank=True)
    father_job_designation = models.CharField(max_length=100, blank=True)
    mother_job_designation = models.CharField(max_length=100, blank=True)
    father_business_type = models.CharField(max_length=100, blank=True)
    mother_business_type = models.CharField(max_length=100, blank=True)
    father_number = models.CharField(max_length=100, blank=True)
    mother_number = models.CharField(max_length=100, blank=True)
    father_office_address = models.CharField(max_length=100, blank=True)
    mother_office_address = models.CharField(max_length=100, blank=True)
    #guardian details
    guardian_name = models.CharField(max_length=75, blank=True)
    #12th class details
    board_12th = models.CharField(max_length=255, blank=True)
    year_of_12th = models.PositiveIntegerField(blank=True, null=True)
    rollno_12th = models.PositiveBigIntegerField(blank=True, null=True)
    school_12th = models.CharField(max_length=255, blank=True)
    aggregate_12th = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    first_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    second_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    third_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    fourth_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_12th = models.CharField(max_length=10, blank=True)     # because integer field was giving error even with null=True and Blank=True
    other_subject_2_12th =  models.CharField(max_length=10, blank=True)
    #10th class details
    board_10th = models.CharField(max_length=255, blank=True)
    year_of_10th = models.PositiveIntegerField(blank=True, null=True)
    rollno_10th = models.PositiveBigIntegerField(blank=True, null=True)
    school_10th = models.CharField(max_length=255, blank=True)
    aggregate_10th = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    maths_10th = models.PositiveIntegerField(blank=True, null=True)
    science_10th = models.PositiveIntegerField(blank=True, null=True)
    english_10th = models.PositiveIntegerField(blank=True, null=True)
    sst_10th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_10th = models.CharField(max_length=100, blank=True)   # because integer field was giving error even with null=True and Blank=True
    other_subject_2_10th =  models.CharField(max_length=100, blank=True)
    #UG Fields
    ug_type = models.CharField(max_length=10)
    board_ug = models.CharField(max_length=75)
    year_of_ug = models.PositiveIntegerField(blank=True, null=True)
    rollno_ug = models.PositiveBigIntegerField(blank=True, null=True)
    school_ug = models.CharField(max_length=125)
    aggregate_ug = models.CharField(max_length=125)
    #CET IPU details
    cet_rank = models.PositiveIntegerField(blank=True, null=True)
    cet_rollno = models.CharField(max_length=20)
    #special acheivements
    special_achievements = models.CharField(max_length=255, blank=True)
    #images and files
    passport_photo = models.ImageField(upload_to=utils.llm_photo_rename, blank=True)
    cet_result = models.FileField(upload_to=utils.llm_cetresult_rename, blank=True)
    marksheet_10th = models.FileField(upload_to=utils.llm_10thmarksheet_rename, blank=True)
    marksheet_12th = models.FileField(upload_to=utils.llm_12thmarksheet_rename, blank=True)
    aadhaar = models.FileField(upload_to=utils.llm_aadhar_rename, blank=True)
    pancard = models.FileField(upload_to=utils.llm_pancard_rename, blank=True)
    ipuregistrationproof = models.FileField(upload_to=utils.llm_ipuregistration_rename, blank=True)
    ug_degree = models.FileField(upload_to=utils.llm_ug_degree_rename, blank=True)
    graduation_result = models.FileField(upload_to=utils.llm_graduationresult_rename, blank=True)
    # Transaction Details
    transaction_id = models.CharField(max_length=255, blank=True)
    transaction_proof = models.FileField(upload_to=utils.llm_transaction_rename, blank=True)
    # Counselling Fee Details
    counselling_transaction_id = models.CharField(max_length=255, blank=True)
    counselling_transaction_proof = models.FileField(upload_to=utils.llm_counselling_transaction_rename, blank=True)
    # To track IP address and other information of users
    ip_address = models.CharField(max_length=100, blank=True, null=True)
    forwarded_address = models.CharField(max_length=255, blank=True ,null=True)
    browser_info = models.CharField(max_length=1000, blank=True ,null=True)
    created_at = models.CharField(max_length=255, blank=True ,null=True)

    def __str__(self):         # for showing record by name in admin panel
        return (self.candidate_first_name+' '+self.candidate_last_name)

    def photograph_preview(self):   #for previewing photo in admin panel
        return mark_safe(f'<img src = "{self.passport_photo.url}" width = "100"/>')

    class Meta:
        verbose_name_plural = "LLM Temporary"    # to show table by this name in admin panel
        db_table = "llm_temp"             # to use the name "llm_temp" instead of "form_llm_temp" in db 


# llm Model:
class Llm(models.Model):
    # application id (auto generated)
    application_id = models.CharField(max_length=100, unique=True)
    #GGSIPU registration no.
    ipu_registration = models.PositiveBigIntegerField(blank=True, unique=True)
    # allowed for counselling
    allow_for_counselling = models.BooleanField(default=False)
    # allow for editing of record
    allow_editing = models.BooleanField(default=False)
    #candidate details
    candidate_first_name = models.CharField(max_length=100, blank=True)
    candidate_middle_name = models.CharField(max_length=100, blank=True)
    candidate_last_name = models.CharField(max_length=100, blank=True)
    #other candidate details
    dob = models.DateField()
    complete_address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True, unique=False)
    candidate_number = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    #father mother details
    father_first_name = models.CharField(max_length=100, blank=True)
    father_middle_name = models.CharField(max_length=100, blank=True)
    father_last_name = models.CharField(max_length=100, blank=True)
    mother_first_name = models.CharField(max_length=100, blank=True)
    mother_middle_name = models.CharField(max_length=100, blank=True)
    mother_last_name = models.CharField(max_length=100, blank=True)
    father_qualification = models.CharField(max_length=100, blank=True)
    mother_qualification = models.CharField(max_length=100, blank=True)
    father_job = models.CharField(max_length=100, blank=True)
    mother_job = models.CharField(max_length=100, blank=True)
    father_job_designation = models.CharField(max_length=100, blank=True)
    mother_job_designation = models.CharField(max_length=100, blank=True)
    father_business_type = models.CharField(max_length=100, blank=True)
    mother_business_type = models.CharField(max_length=100, blank=True)
    father_number = models.CharField(max_length=100, blank=True)
    mother_number = models.CharField(max_length=100, blank=True)
    father_office_address = models.CharField(max_length=100, blank=True)
    mother_office_address = models.CharField(max_length=100, blank=True)
    #guardian details
    guardian_name = models.CharField(max_length=75, blank=True)
    #12th class details
    board_12th = models.CharField(max_length=255, blank=True)
    year_of_12th = models.PositiveIntegerField(blank=True)
    rollno_12th = models.PositiveBigIntegerField(blank=True)
    school_12th = models.CharField(max_length=255, blank=True)
    aggregate_12th = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    first_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    second_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    third_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    fourth_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_12th = models.CharField(max_length=10, blank=True)     # because integer field was giving error even with null=True and Blank=True
    other_subject_2_12th =  models.CharField(max_length=10, blank=True)
    #10th class details
    board_10th = models.CharField(max_length=255, blank=True)
    year_of_10th = models.PositiveIntegerField(blank=True)
    rollno_10th = models.PositiveBigIntegerField(blank=True)
    school_10th = models.CharField(max_length=255, blank=True)
    aggregate_10th = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    maths_10th = models.PositiveIntegerField(blank=True)
    science_10th = models.PositiveIntegerField(blank=True)
    english_10th = models.PositiveIntegerField(blank=True)
    sst_10th = models.PositiveIntegerField(blank=True)
    other_subject_10th = models.CharField(max_length=100, blank=True)   # because integer field was giving error even with null=True and Blank=True
    other_subject_2_10th =  models.CharField(max_length=100, blank=True)
    #UG Fields
    ug_type = models.CharField(max_length=10)
    board_ug = models.CharField(max_length=75)
    year_of_ug = models.PositiveIntegerField(blank=True, null=True)
    rollno_ug = models.PositiveBigIntegerField(blank=True, null=True)
    school_ug = models.CharField(max_length=125)
    aggregate_ug = models.CharField(max_length=125)
    #CET IPU details
    cet_rank = models.PositiveIntegerField(blank=True, null=True)
    cet_rollno = models.CharField(max_length=20)
    #special acheivements
    special_achievements = models.CharField(max_length=255, blank=True)
    #images and files
    passport_photo = models.ImageField(upload_to=utils.llm_photo_rename, blank=True)
    cet_result = models.FileField(upload_to=utils.llm_cetresult_rename, blank=True)
    marksheet_10th = models.FileField(upload_to=utils.llm_10thmarksheet_rename, blank=True)
    marksheet_12th = models.FileField(upload_to=utils.llm_12thmarksheet_rename, blank=True)
    aadhaar = models.FileField(upload_to=utils.llm_aadhar_rename, blank=True)
    pancard = models.FileField(upload_to=utils.llm_pancard_rename, blank=True)
    ipuregistrationproof = models.FileField(upload_to=utils.llm_ipuregistration_rename, blank=True)
    ug_degree = models.FileField(upload_to=utils.llm_ug_degree_rename, blank=True)
    graduation_result = models.FileField(upload_to=utils.llm_graduationresult_rename, blank=True)
    # Transaction Details
    transaction_id = models.CharField(max_length=255, blank=True)
    transaction_proof = models.FileField(upload_to=utils.llm_transaction_rename, blank=True)
    # Counselling Fee Details
    counselling_transaction_id = models.CharField(max_length=255, blank=True)
    counselling_transaction_proof = models.FileField(upload_to=utils.llm_counselling_transaction_rename, blank=True)
    # To track IP address and other information of users
    ip_address = models.CharField(max_length=100, blank=True, null=True)
    forwarded_address = models.CharField(max_length=255, blank=True ,null=True)
    browser_info = models.CharField(max_length=1000, blank=True ,null=True)
    created_at = models.CharField(max_length=255, blank=True ,null=True)

    def __str__(self):         # for showing record by name in admin panel
        return (self.candidate_first_name+' '+self.candidate_last_name)

    def photograph_preview(self):   #for previewing photo in admin panel
        return mark_safe(f'<img src = "{self.passport_photo.url}" width = "100"/>')

    class Meta:
        verbose_name_plural = "LLM"    # to show table by this name in admin panel
        db_table = "llm"             # to use the name "llm" instead of "form_llm" in db

