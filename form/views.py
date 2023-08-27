from django.shortcuts import render, redirect
import datetime
from . models import AllowedIP, Login, Bba, BbaTemp, Bcom, BcomTemp, Bjmc, BjmcTemp, Ballb, BallbTemp, Bballb, BballbTemp, Eco, EcoTemp, Llm, LlmTemp
from django.contrib import messages
# For sending mails:
from django.core.mail import send_mail
from django.conf import settings
# For random password generation
import secrets
import string
from django.db import IntegrityError




# we are taking a flag variable named logged_in
logged_in = False 
# if this logged_in is True, then only user can see pages like /bba or /bba-preview etc.
# if user tries to directly come to /bba or /bba-preview etc, then we will redirect him back to /login

# also we are taking application_id as a global variable at the very beginning of the program
# so that we avoid passing the application_id from one view to other for performing CRUD operations
application_id = ""
ipu_registration = ""
course=""
# this empty string will be filled with value either from the index function or from login function 


# Function for generating random 12 letter/digit password
def get_random_pwd():
    # all uppercase lowercase letters
    letters = string.ascii_letters
    # all digits
    digits = string.digits
    # concatenation
    alphabet = letters + digits
    pwd_length = 12
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))

    return pwd

# Function for generating random 8 digit ID
def get_random_id():
    digits = string.digits
    id_length = 8
    id = ''
    for i in range(id_length):
        id += ''.join(secrets.choice(digits))
    # retreiving all existing records
    logins = Login.objects.all()
    credentials = {}         # empty dictionary for storing key value pairs of id:pwd
    for login in logins:
        credentials[login.ipu_registration] = login.password
    # checking if that id doesnt exist then only we will proceed (bcoz we are generating randomly so they can repeat)
    flag_unique = False
    while flag_unique == False:
        if id not in credentials:
            flag_unique = True
            return id
        else:
            id = get_random_id()




# Index Page: The first page user sees after coming on empty path
def index(request):
    if request.method == 'POST':
        # for allowing only specific IP addresses
        allowed_ips = AllowedIP.objects.all()
        allowed_ips_list = []
        # making a list out of this query set
        for ip in allowed_ips:
            allowed_ips_list.append(ip.ip_address)
        ip_address = request.META.get('REMOTE_ADDR')
        # Temporarily allowing all ips
        # if ip_address not in allowed_ips_list:
        #     return render(request, 'index.html')
        candidate_name = request.POST.get('candidate_name')
        candidate_email = request.POST.get('candidate_email')
        candidate_mobile = request.POST.get('candidate_mobile')
        global ipu_registration
        ipu_registration = request.POST.get('ipu_registration')
        created_at = str(datetime.datetime.now())[:19]        # only first 19 indexes so that it doesnt store microseconds
        logins = Login.objects.all()
        for login in logins:
            if ((login.candidate_email == candidate_email) or (login.candidate_mobile == candidate_mobile)):
                message="User already exists"
                context = {'message': message}
                return render(request, 'login.html', context) 
        # getting unique password and id
        id = get_random_id()
        pwd = get_random_pwd()
        #sending mail
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [candidate_email, ]
        custom_message = "Your IPU Registration No. is:\n  " + ipu_registration + "\n\nYour password is:\n  " + pwd
        send_mail( 'MAIMS Login Credentials', custom_message , email_from, recipient_list, fail_silently=True)
        # After sending mail, now saving user id and password
        final_id = "MAIMS/MQ/2023-24/"+id   #only last 8 randomly generated digits to be sent to user but whole id to be stored in database
        global application_id
        application_id = final_id
        newlogin = Login(application_id = application_id, password=pwd, ipu_registration=ipu_registration, candidate_name=candidate_name, candidate_mobile=candidate_mobile, candidate_email=candidate_email, ip_address=ip_address, created_at=created_at)
        # when the ipu_registration number is already exisiting in db, then an error is raised while saving the records
        try:
            newlogin.save()
        except IntegrityError as e:
            message = e
            context = {'message': message}
            return render(request, 'login.html', context) 
        return redirect('login')
    else:
        # GET request
        return render(request, 'index.html')

# Login Page
def login(request):
    message="OK"
    # getting all user ids and correspponding passwords in a list
    logins = Login.objects.all()
    credentials = {}         # empty dictionary for storing key value pairs of id:pwd
    for login in logins:
        credentials[str(login.ipu_registration)] = login.password
    # this post request comes from the 'form action=login' in the login page
    if request.method == 'POST' :
        # for allowing only specific IP addresses
        allowed_ips = AllowedIP.objects.all()
        allowed_ips_list = []
        # making a list out of this query set
        for ip in allowed_ips:
            allowed_ips_list.append(ip.ip_address)
        ip_address = request.META.get('REMOTE_ADDR')
        # Temporarily allowing all ips
        # if ip_address not in allowed_ips_list:
        #     return render(request, 'login.html')
        global ipu_registration
        ipu_registration = request.POST.get('ipu_registration')
        user_pwd = request.POST.get('user_pwd')
        # now checking id password
        if ipu_registration in credentials:
            if user_pwd == credentials[ipu_registration] :
                # when both ipu_registration no. and password are correct, then redirecting to courses page 
                # and setting global variable application_id to corresponding value
                # and setting flag logged_in to True
                global logged_in
                logged_in = True
                global application_id
                application_id = Login.objects.filter(ipu_registration=ipu_registration).first().application_id
                return redirect('courses')
            else :                   # when ipu_registration is ok but doesnt match the corresponding user password
                message="Invalid Password"
                context = {'message': message}
                return render(request, 'login.html', context) 
        else :
            message="Invalid Registration Number or Password"
            context = {'message': message}
            return render(request, 'login.html', context)
    # GET method
    context = {'message': message}
    return render(request, 'login.html', context)

# Courses: For choice of course
def courses(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Proceed" on the /courses.html page
    if request.method == "POST":
        global course
        course = request.POST.get('course')
        # if user selected bba then three possibilities:
        # either he is a completely new user (then redirect to bba1)
        # or he has some temporary data submitted (then redirect to bba1)
        # or he has permanent data submitted (then redirect to bba-preview)
        # same case is for all courses
        if course == "BBA":
            login_record = Login.objects.filter(application_id=application_id).first()
            login_record.course = course
            login_record.save()
            temp_record = BbaTemp.objects.filter(application_id=application_id).first()
            permanent_record = Bba.objects.filter(application_id=application_id).first()
            if temp_record:
                return redirect ('bba1')
            if permanent_record:
                return redirect ('dashboard')
            return redirect ('bba1')
        if course == "BCOM":
            login_record = Login.objects.filter(application_id=application_id).first()
            login_record.course = course
            login_record.save()
            temp_record = BcomTemp.objects.filter(application_id=application_id).first()
            permanent_record = Bcom.objects.filter(application_id=application_id).first()
            if temp_record:
                return redirect ('bcom1')
            if permanent_record:
                return redirect ('dashboard')
            return redirect ('bcom1')
        if course == "BJMC":
            login_record = Login.objects.filter(application_id=application_id).first()
            login_record.course = course
            login_record.save()
            temp_record = BjmcTemp.objects.filter(application_id=application_id).first()
            permanent_record = Bjmc.objects.filter(application_id=application_id).first()
            if temp_record:
                return redirect ('bjmc1')
            if permanent_record:
                return redirect ('dashboard')
            return redirect ('bjmc1')
        if course == "BALLB":
            login_record = Login.objects.filter(application_id=application_id).first()
            login_record.course = course
            login_record.save()
            temp_record = BallbTemp.objects.filter(application_id=application_id).first()
            permanent_record = Ballb.objects.filter(application_id=application_id).first()
            if temp_record:
                return redirect ('ballb1')
            if permanent_record:
                return redirect ('dashboard')
            return redirect ('ballb1')
        if course == "BBALLB":
            login_record = Login.objects.filter(application_id=application_id).first()
            login_record.course = course
            login_record.save()
            temp_record = BballbTemp.objects.filter(application_id=application_id).first()
            permanent_record = Bballb.objects.filter(application_id=application_id).first()
            if temp_record:
                return redirect ('bballb1')
            if permanent_record:
                return redirect ('dashboard')
            return redirect ('bballb1')
        if course == "ECO":
            login_record = Login.objects.filter(application_id=application_id).first()
            login_record.course = course
            login_record.save()
            temp_record = EcoTemp.objects.filter(application_id=application_id).first()
            permanent_record = Eco.objects.filter(application_id=application_id).first()
            if temp_record:
                return redirect ('eco1')
            if permanent_record:
                return redirect ('dashboard')
            return redirect ('eco1')
        if course == "LLM":
            login_record = Login.objects.filter(application_id=application_id).first()
            login_record.course = course
            login_record.save()
            temp_record = LlmTemp.objects.filter(application_id=application_id).first()
            permanent_record = Llm.objects.filter(application_id=application_id).first()
            if temp_record:
                return redirect ('llm1')
            if permanent_record:
                return redirect ('dashboard')
            return redirect ('llm1')
    else:
        # GET request
        return render(request, 'courses.html')    

# For resetting password
def password_reset(request):
    if request.method == "POST":
        # getting all user ids and correspponding emails in a list
        logins = Login.objects.all()
        credentials = {}         # empty dictionary for storing key value pairs of id:pwd
        for login in logins:
            credentials[str(login.ipu_registration)] = login.candidate_email
        global ipu_registration
        ipu_registration = request.POST.get('ipu_registration')
        email = request.POST.get('email')
        # now checking id and email
        if ipu_registration in credentials:
            if email == credentials[ipu_registration] :
                # when both ipu_registration no. and email are correct, then we will send the password
                #sending mail
                new_pwd = get_random_pwd()
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email, ]
                custom_message = "Your GGSIPU Registration No. is:\n  " + ipu_registration + "\n\nYour New password is:\n  " + new_pwd
                send_mail( 'MAIMS Login Credentials', custom_message , email_from, recipient_list, fail_silently=True)
                newobj = Login.objects.filter(ipu_registration = ipu_registration).first()
                newobj.password = new_pwd
                newobj.save()
                message="New credentials have been sent to your mail."
                messages.info(request, message)
                return redirect('login')
            else :                   
                # when ipu_registration is ok but doesnt match the corresponding user email
                message="The GGSIPU Registration No. "+ipu_registration+" has a different mail associated with it."
                messages.info(request, message)
                return render(request, 'password-reset.html') 
        else :
            message="No record found for GGSIPU Registration Number "+ipu_registration
            messages.info(request, message)
            return render(request, 'password-reset.html')
    # GET request
    return render(request, 'password-reset.html')

# Dashboard: For giving preview/edit/counselling fee options
def dashboard(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # GET request: We shall pass the course as context too
    global course
    if course == "BBA":
        record = Bba.objects.all().filter(application_id = application_id).first()
    if course == "BCOM":
        record = Bcom.objects.all().filter(application_id = application_id).first()
    if course == "BJMC":
        record = Bjmc.objects.all().filter(application_id = application_id).first()
    if course == "BALLB":
        record = Ballb.objects.all().filter(application_id = application_id).first()
    if course == "BBALLB":
        record = Bballb.objects.all().filter(application_id = application_id).first()
    if course == "ECO":
        record = Eco.objects.all().filter(application_id = application_id).first()
    if course == "LLM":
        record = Llm.objects.all().filter(application_id = application_id).first()
    context = {'course': course, 'record': record}
    return render(request, 'dashboard.html', context)

# Counselling: For user to pay counselling fees
def counselling(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # When POST, then simply save the two fields
    if request.method == "POST":
        counselling_transaction_id = request.POST.get('counselling_transaction_id')
        counselling_transaction_proof = request.FILES['counselling_transaction_proof']
        global course
        if course == "BBA":
            record = Bba.objects.filter(application_id = application_id).first()
            record.counselling_transaction_id = counselling_transaction_id
            record.counselling_transaction_proof = counselling_transaction_proof
            record.save()
            return redirect ('bba_preview')
        if course == "BCOM":
            record = Bcom.objects.filter(application_id = application_id).first()
            record.counselling_transaction_id = counselling_transaction_id
            record.counselling_transaction_proof = counselling_transaction_proof
            record.save()
            return redirect ('bcom_preview')
        if course == "BJMC":
            record = Bjmc.objects.filter(application_id = application_id).first()
            record.counselling_transaction_id = counselling_transaction_id
            record.counselling_transaction_proof = counselling_transaction_proof
            record.save()
            return redirect ('bjmc_preview')
        if course == "BALLB":
            record = Ballb.objects.filter(application_id = application_id).first()
            record.counselling_transaction_id = counselling_transaction_id
            record.counselling_transaction_proof = counselling_transaction_proof
            record.save()
            return redirect ('ballb_preview')
        if course == "BBALLB":
            record = Bballb.objects.filter(application_id = application_id).first()
            record.counselling_transaction_id = counselling_transaction_id
            record.counselling_transaction_proof = counselling_transaction_proof
            record.save()
            return redirect ('bballb_preview')
        if course == "ECO":
            record = Eco.objects.filter(application_id = application_id).first()
            record.counselling_transaction_id = counselling_transaction_id
            record.counselling_transaction_proof = counselling_transaction_proof
            record.save()
            return redirect ('eco_preview')
        if course == "LLM":
            record = Llm.objects.filter(application_id = application_id).first()
            record.counselling_transaction_id = counselling_transaction_id
            record.counselling_transaction_proof = counselling_transaction_proof
            record.save()
            return redirect ('llm_preview')
    # GET request: simply show counselling page
    return render(request, 'counselling.html')






def bba1(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bba1.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        candidate_first_name = request.POST.get('candidate_first_name')
        candidate_middle_name = request.POST.get('candidate_middle_name')
        candidate_last_name = request.POST.get('candidate_last_name')
        email = request.POST.get('email')
        candidate_number = request.POST.get('candidate_number')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        category = request.POST.get('category')
        region = request.POST.get('region')
        # To track IP address and other info of user coming from request.META header
        ip_address = request.META.get('REMOTE_ADDR','-1')      # return -1 if no address found
        forwarded_address = request.META.get('HTTP_X_FORWARDED_FOR','-1')
        browser_info = request.META.get('HTTP_USER_AGENT','-1')
        created_at = str(datetime.datetime.now())[:19]        # only first 19 indexes so that it doesnt store microseconds
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BbaTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.candidate_first_name = candidate_first_name   
            existing_record.candidate_middle_name = candidate_middle_name
            existing_record.candidate_last_name = candidate_last_name
            existing_record.email = email
            existing_record.candidate_number = candidate_number
            existing_record.gender = gender
            existing_record.dob = dob
            existing_record.category = category
            existing_record.region = region
            existing_record.ip_address = ip_address
            existing_record.forwarded_address = forwarded_address
            existing_record.browser_info = browser_info
            existing_record.created_at = created_at
            # saving the updated record
            existing_record.save()
            return redirect ('bba2')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BbaTemp(application_id=application_id, ipu_registration=ipu_registration,
                            candidate_first_name=candidate_first_name,
                            candidate_middle_name=candidate_middle_name, candidate_last_name=candidate_last_name,
                            email=email, candidate_number=candidate_number, gender=gender, dob=dob, category=category, region=region,
                            ip_address=ip_address, forwarded_address=forwarded_address, browser_info=browser_info, created_at=created_at,)
            newform.save()
            return redirect ('bba2')
    # if the request method is not POST, then:
    # either user is coming from login page for the very first time
    # or user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bba form by clicking the step-form (progress bar)
    # in all three cases we can render bba1.html with context
    # to create context we will use the globally available variable application_id
    record = BbaTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bba/bba1.html', context)

def bba2(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bba2.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        father_first_name = request.POST.get('father_first_name')
        father_middle_name = request.POST.get('father_middle_name')
        father_last_name = request.POST.get('father_last_name')
        mother_first_name = request.POST.get('mother_first_name')
        mother_middle_name = request.POST.get('mother_middle_name')
        mother_last_name = request.POST.get('mother_last_name')
        father_qualification = request.POST.get('father_qualification')
        mother_qualification = request.POST.get('mother_qualification')
        father_job = request.POST.get('father_job')
        mother_job = request.POST.get('mother_job')
        father_job_designation = request.POST.get('father_job_designation')
        mother_job_designation = request.POST.get('mother_job_designation')
        father_business_type = request.POST.get('father_business_type')
        mother_business_type = request.POST.get('mother_business_type')
        father_number = request.POST.get('father_number')
        mother_number = request.POST.get('mother_number')
        father_office_address = request.POST.get('father_office_address')
        mother_office_address = request.POST.get('mother_office_address')
        guardian_name = request.POST.get('guardian_name')
        complete_address = request.POST.get('complete_address')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BbaTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.father_first_name = father_first_name   
            existing_record.father_middle_name = father_middle_name
            existing_record.father_last_name = father_last_name
            existing_record.mother_first_name = mother_first_name   
            existing_record.mother_middle_name = mother_middle_name
            existing_record.mother_last_name = mother_last_name
            existing_record.father_qualification = father_qualification
            existing_record.mother_qualification = mother_qualification
            existing_record.father_job = father_job
            existing_record.mother_job = mother_job
            existing_record.father_job_designation = father_job_designation
            existing_record.mother_job_designation = mother_job_designation
            existing_record.father_business_type = father_business_type   
            existing_record.mother_business_type = mother_business_type
            existing_record.father_office_address = father_office_address
            existing_record.mother_office_address = mother_office_address   
            existing_record.father_number = father_number
            existing_record.mother_number = mother_number
            existing_record.guardian_name = guardian_name   
            existing_record.complete_address = complete_address
            # saving the updated record
            existing_record.save()
            return redirect ('bba3')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BbaTemp(application_id=application_id, ipu_registration=ipu_registration, 
                            father_first_name=father_first_name, father_middle_name=father_middle_name, father_last_name=father_last_name,
                            mother_first_name=mother_first_name, mother_middle_name=mother_middle_name, mother_last_name=mother_last_name,
                            father_qualification=father_qualification, mother_qualification=mother_qualification,
                            father_job=father_job, mother_job=mother_job,
                            father_job_designation=father_job_designation, mother_job_designation=mother_job_designation,
                            father_business_type=father_business_type, mother_business_type=mother_business_type,
                            father_number=father_number, mother_number=mother_number,
                            father_office_address=father_office_address, mother_office_address=mother_office_address,
                            complete_address=complete_address, guardian_name=guardian_name,)
            newform.save()
            return redirect ('bba3')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bba form by clicking the step-form (progress bar)
    # or user is coming from bba1.html after saving his record
    # in all three cases we can render bba2.html with context
    # to create context we will use the globally available variable application_id
    record = BbaTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bba/bba2.html', context)

def bba3(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bba3.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        board_12th = request.POST.get('board_12th')
        year_of_12th = request.POST.get('year_of_12th')
        rollno_12th = request.POST.get('rollno_12th')
        school_12th = request.POST.get('school_12th')
        aggregate_12th = float(request.POST.get('aggregate_12th'))
        first_subject_12th = request.POST.get('first_subject_12th')
        second_subject_12th = request.POST.get('second_subject_12th')
        third_subject_12th = request.POST.get('third_subject_12th')
        fourth_subject_12th = request.POST.get('fourth_subject_12th')
        other_subject_12th = request.POST.get('other_subject_12th')
        other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        board_10th = request.POST.get('board_10th')
        year_of_10th = request.POST.get('year_of_10th')
        rollno_10th = request.POST.get('rollno_10th')
        school_10th = request.POST.get('school_10th')
        aggregate_10th = float(request.POST.get('aggregate_10th'))
        maths_10th = request.POST.get('maths_10th')
        science_10th = request.POST.get('science_10th')
        english_10th = request.POST.get('english_10th')
        sst_10th = request.POST.get('sst_10th')
        other_subject_10th = request.POST.get('other_subject_10th')
        other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BbaTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.board_12th = board_12th   
            existing_record.year_of_12th = year_of_12th
            existing_record.rollno_12th = rollno_12th
            existing_record.school_12th = school_12th
            existing_record.aggregate_12th = aggregate_12th
            existing_record.first_subject_12th = first_subject_12th
            existing_record.second_subject_12th = second_subject_12th
            existing_record.third_subject_12th = third_subject_12th
            existing_record.fourth_subject_12th = fourth_subject_12th
            existing_record.other_subject_12th = other_subject_12th
            existing_record.other_subject_2_12th = other_subject_2_12th
            existing_record.board_10th = board_10th   
            existing_record.year_of_10th = year_of_10th
            existing_record.rollno_10th = rollno_10th
            existing_record.school_10th = school_10th
            existing_record.aggregate_10th = aggregate_10th
            existing_record.maths_10th = maths_10th
            existing_record.science_10th = science_10th
            existing_record.english_10th = english_10th
            existing_record.sst_10th = sst_10th
            existing_record.other_subject_10th = other_subject_10th
            existing_record.other_subject_2_10th = other_subject_2_10th
            # saving the updated record
            existing_record.save()
            return redirect ('bba4')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BbaTemp(application_id=application_id, ipu_registration=ipu_registration,
                            board_12th=board_12th, year_of_12th=year_of_12th, rollno_12th=rollno_12th, school_12th=school_12th,
                            first_subject_12th=first_subject_12th, second_subject_12th=second_subject_12th, third_subject_12th=third_subject_12th, fourth_subject_12th=fourth_subject_12th,
                            other_subject_12th=other_subject_12th, other_subject_2_12th=other_subject_2_12th, aggregate_12th=aggregate_12th, 
                            board_10th=board_10th, year_of_10th=year_of_10th, rollno_10th=rollno_10th, school_10th=school_10th,
                            maths_10th=maths_10th, science_10th=science_10th, english_10th=english_10th, sst_10th=sst_10th,
                            other_subject_10th=other_subject_10th, other_subject_2_10th=other_subject_2_10th, aggregate_10th=aggregate_10th,)
            newform.save()
            return redirect ('bba4')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bba form by clicking the step-form (progress bar)
    # or user is coming from bba2.html after saving his record
    # in all three cases we can render bba3.html with context
    # to create context we will use the globally available variable application_id
    record = BbaTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bba/bba3.html', context)

def bba4(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bba4.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        cet_or_cuet = request.POST.get('cet_or_cuet')
        cet_rank = request.POST.get('cet_rank')
        cet_rollno = request.POST.get('cet_rollno')
        special_achievements = request.POST.get('special_achievements')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BbaTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.cet_or_cuet = cet_or_cuet   
            existing_record.cet_rank = cet_rank
            existing_record.cet_rollno = cet_rollno
            existing_record.special_achievements = special_achievements
            # saving the updated record
            existing_record.save()
            return redirect ('bba5')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BbaTemp(application_id=application_id, ipu_registration=ipu_registration,
                            cet_rank=cet_rank, cet_rollno=cet_rollno, cet_or_cuet=cet_or_cuet,
                            special_achievements=special_achievements,)
            newform.save()
            return redirect ('bba5')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bba form by clicking the step-form (progress bar)
    # or user is coming from bba3.html after saving his record
    # in all three cases we can render bba4.html with context
    # to create context we will use the globally available variable application_id
    record = BbaTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bba/bba4.html', context)

def bba5(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bba5.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        passport_photo = request.FILES['passport_photo']
        cet_result = request.FILES['cet_result']
        marksheet_10th = request.FILES['marksheet_10th']
        marksheet_12th = request.FILES['marksheet_12th']
        aadhaar = request.FILES['aadhaar']
        pancard = request.FILES['pancard']
        ipuregistrationproof = request.FILES['ipuregistrationproof']
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BbaTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.passport_photo = passport_photo   
            existing_record.cet_result = cet_result
            existing_record.marksheet_10th = marksheet_10th
            existing_record.marksheet_12th = marksheet_12th
            existing_record.aadhaar = aadhaar
            existing_record.pancard = pancard
            existing_record.ipuregistrationproof = ipuregistrationproof
            # saving the updated record
            existing_record.save()
            # we will only redirect to payments on /bba6 if all previous steps are filled
            # so to check that, we will check whether some value on each step is filled or not
            if not existing_record.candidate_first_name:
                return redirect('bba1')
            if not existing_record.father_first_name:
                return redirect('bba2')
            if not existing_record.board_10th:
                return redirect('bba3')
            if not existing_record.cet_rollno:
                return redirect('bba4')
            # if all of these details are filled, then we can safely proceed to payment
            return redirect ('bba6')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BbaTemp(application_id=application_id, ipu_registration=ipu_registration,
                            passport_photo=passport_photo, cet_result=cet_result, marksheet_10th=marksheet_10th, marksheet_12th=marksheet_12th,
                            aadhaar=aadhaar, pancard=pancard, ipuregistrationproof=ipuregistrationproof)
            newform.save()
            # if its a new record, then we shall not allow to proceed to payment, so we are redirecting to /bba1
            return redirect ('bba1')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bba form by clicking the step-form (progress bar)
    # or user is coming from bba4.html after saving his record
    # in all three cases we can render bba5.html with context
    # to create context we will use the globally available variable application_id
    record = BbaTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bba/bba5.html', context)

def bba6(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bba6.html page
    # so we shall save the data 
    if request.method == "POST" :
        transaction_id = request.POST.get('transaction_id')
        transaction_proof = request.FILES['transaction_proof']
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # (this will never be the case because we are not allowing user to come to /bba6 if he hasn't already filled previous data , but still handling this case)
        # so, let's check if a record exists or not
        existing_record = BbaTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.transaction_id = transaction_id   
            existing_record.transaction_proof = transaction_proof
            # saving the updated record
            existing_record.save()
            # all steps are completed, now redirecting to final preview where data will move from temp table to permanent table 
            return redirect ('bba')
        else:
            # saving all fields in a new object
            newform = BbaTemp(application_id=application_id, ipu_registration=ipu_registration,
                            transaction_id=transaction_id, transaction_proof=transaction_proof)
            newform.save()
            return redirect ('bba')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bba form by clicking the step-form (progress bar)
    # or user is coming from bba5.html after saving his record
    # we shall allow the user only in the case when he has submitted all 5 steps
    record = BbaTemp.objects.all().filter(application_id = application_id).first()
    # so to check that, we will check whether some value on each step is filled or not
    # before that we can check if record exists or not:
    if not record:
        messages.info(request, 'Please fill candidate details before payment')
        return redirect('bba1')
    if not record.candidate_first_name:
        messages.info(request, 'Please fill candidate details before payment')
        return redirect('bba1')
    if not record.father_first_name:
        messages.info(request, 'Please fill parent details before payment')
        return redirect('bba2')
    if not record.board_10th:
        messages.info(request, 'Please fill educational details before payment')
        return redirect('bba3')
    if not record.cet_rollno:
        messages.info(request, 'Please fill qualifying details before payment')
        return redirect('bba4')
    if not record.passport_photo:
        messages.info(request, 'Please upload documents before payment')
        return redirect("bba5")
    # if all of these details are filled, then we can safely render /bba6.html
    context = {'record': record}
    return render(request, 'bba/bba6.html', context)

# Bba
def bba(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Submit" on the /bba.html page
    # so we shall save the data in permanent table and delete from temporary table
    if request.method == 'POST':
        transaction_id = request.POST.get('transaction_id')
        # category and region
        category = request.POST.get('category')
        region = request.POST.get('region')
        candidate_first_name = request.POST.get('candidate_first_name')
        candidate_middle_name = request.POST.get('candidate_middle_name')
        candidate_last_name = request.POST.get('candidate_last_name')
        #father mother details
        father_first_name = request.POST.get('father_first_name')
        father_middle_name = request.POST.get('father_middle_name')
        father_last_name = request.POST.get('father_last_name')
        mother_first_name = request.POST.get('mother_first_name')
        mother_middle_name = request.POST.get('mother_middle_name')
        mother_last_name = request.POST.get('mother_last_name')
        father_qualification = request.POST.get('father_qualification')
        mother_qualification = request.POST.get('mother_qualification')
        father_job = request.POST.get('father_job')
        mother_job = request.POST.get('mother_job')
        father_job_designation = request.POST.get('father_job_designation')
        mother_job_designation = request.POST.get('mother_job_designation')
        father_business_type = request.POST.get('father_business_type')
        mother_business_type = request.POST.get('mother_business_type')
        father_number = request.POST.get('father_number')
        mother_number = request.POST.get('mother_number')
        father_office_address = request.POST.get('father_office_address')
        mother_office_address = request.POST.get('mother_office_address')
        #other candidate details
        complete_address = request.POST.get('complete_address')
        email = request.POST.get('email')
        candidate_number = request.POST.get('candidate_number')
        gender = request.POST.get('gender')
        #guardian details
        guardian_name = request.POST.get('guardian_name')
        #candidate dob
        dob = request.POST.get('dob')
        #12th class details
        board_12th = request.POST.get('board_12th')
        year_of_12th = request.POST.get('year_of_12th')
        rollno_12th = request.POST.get('rollno_12th')
        school_12th = request.POST.get('school_12th')
        aggregate_12th = float(request.POST.get('aggregate_12th'))
        first_subject_12th = request.POST.get('first_subject_12th')
        second_subject_12th = request.POST.get('second_subject_12th')
        third_subject_12th = request.POST.get('third_subject_12th')
        fourth_subject_12th = request.POST.get('fourth_subject_12th')
        other_subject_12th = request.POST.get('other_subject_12th')
        other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        #10th class details
        board_10th = request.POST.get('board_10th')
        year_of_10th = request.POST.get('year_of_10th')
        rollno_10th = request.POST.get('rollno_10th')
        school_10th = request.POST.get('school_10th')
        aggregate_10th = float(request.POST.get('aggregate_10th'))
        maths_10th = request.POST.get('maths_10th')
        science_10th = request.POST.get('science_10th')
        english_10th = request.POST.get('english_10th')
        sst_10th = request.POST.get('sst_10th')
        other_subject_10th = request.POST.get('other_subject_10th')
        other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        #CET details
        cet_or_cuet = request.POST.get('cet_or_cuet')
        cet_rank = request.POST.get('cet_rank')
        cet_rollno = request.POST.get('cet_rollno')
        #special acheivements
        special_achievements = request.POST.get('special_achievements')
        # To track IP address and other info of user coming from request.META header
        ip_address = request.META.get('REMOTE_ADDR','-1')      # return -1 if no address found
        forwarded_address = request.META.get('HTTP_X_FORWARDED_FOR','-1')
        browser_info = request.META.get('HTTP_USER_AGENT','-1')
        created_at = str(datetime.datetime.now())[:19]        # only first 19 indexes so that it doesnt store microseconds
        # saving all fields expect files in a new object
        newform = Bba(candidate_first_name=candidate_first_name, candidate_middle_name=candidate_middle_name, candidate_last_name=candidate_last_name,
                        father_first_name=father_first_name, father_middle_name=father_middle_name, father_last_name=father_last_name,
                        mother_first_name=mother_first_name, mother_middle_name=mother_middle_name, mother_last_name=mother_last_name,
                        father_qualification=father_qualification, mother_qualification=mother_qualification,
                        father_job=father_job, mother_job=mother_job,
                        father_job_designation=father_job_designation, mother_job_designation=mother_job_designation,
                        father_business_type=father_business_type, mother_business_type=mother_business_type,
                        father_number=father_number, mother_number=mother_number,
                        father_office_address=father_office_address, mother_office_address=mother_office_address,
                        complete_address=complete_address, candidate_number=candidate_number,
                        guardian_name=guardian_name, email=email, dob=dob, gender=gender,
                        board_12th=board_12th, year_of_12th=year_of_12th, rollno_12th=rollno_12th, school_12th=school_12th,
                        first_subject_12th=first_subject_12th, second_subject_12th=second_subject_12th, third_subject_12th=third_subject_12th, fourth_subject_12th=fourth_subject_12th,
                        other_subject_12th=other_subject_12th, other_subject_2_12th=other_subject_2_12th, aggregate_12th=aggregate_12th, 
                        board_10th=board_10th, year_of_10th=year_of_10th, rollno_10th=rollno_10th, school_10th=school_10th,
                        maths_10th=maths_10th, science_10th=science_10th, english_10th=english_10th, sst_10th=sst_10th,
                        other_subject_10th=other_subject_10th, other_subject_2_10th=other_subject_2_10th, aggregate_10th=aggregate_10th, 
                        cet_rank=cet_rank, cet_rollno=cet_rollno, cet_or_cuet=cet_or_cuet,
                        ipu_registration=ipu_registration, special_achievements=special_achievements,
                        application_id=application_id, transaction_id=transaction_id,
                        category=category, region=region,
                        ip_address=ip_address, forwarded_address=forwarded_address, browser_info=browser_info, created_at=created_at,)
        newform.save()
        # now saving files after instance is created
        temp_record = BbaTemp.objects.get(application_id=application_id)
        newobj = Bba.objects.get(pk=newform.pk)
        newobj.passport_photo = temp_record.passport_photo
        newobj.cet_result = temp_record.cet_result
        newobj.marksheet_10th = temp_record.marksheet_10th
        newobj.marksheet_12th = temp_record.marksheet_12th
        newobj.aadhaar = temp_record.aadhaar
        newobj.pancard = temp_record.pancard
        newobj.ipuregistrationproof = temp_record.ipuregistrationproof
        newobj.transaction_proof = temp_record.transaction_proof
        newobj.save()
        temp_record.delete()   # deleting the temporary record
        # At this point, form is submitted successfully
        return redirect('bba_preview')
    record = BbaTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bba/bba.html', context)
    
# Bba Preview
def bba_preview(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    record = Bba.objects.filter(application_id=application_id).first()
    context = {'record': record}
    return render(request, 'bba/bba-preview.html', context)

# Edit Bba (after final submission)
def bba_edit(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save" on the /bba-edit.html page
    # so we shall save the data in permanent table and delete from temporary table
    if request.method == 'POST':
        record = Bba.objects.all().filter(application_id = application_id).first()
        record.transaction_id = request.POST.get('transaction_id')
        # category and region
        record.category = request.POST.get('category')
        record.region = request.POST.get('region')
        record.candidate_first_name = request.POST.get('candidate_first_name')
        record.candidate_middle_name = request.POST.get('candidate_middle_name')
        record.candidate_last_name = request.POST.get('candidate_last_name')
        #father mother details
        record.father_first_name = request.POST.get('father_first_name')
        record.father_middle_name = request.POST.get('father_middle_name')
        record.father_last_name = request.POST.get('father_last_name')
        record.mother_first_name = request.POST.get('mother_first_name')
        record.mother_middle_name = request.POST.get('mother_middle_name')
        record.mother_last_name = request.POST.get('mother_last_name')
        record.father_qualification = request.POST.get('father_qualification')
        record.mother_qualification = request.POST.get('mother_qualification')
        record.father_job = request.POST.get('father_job')
        record.mother_job = request.POST.get('mother_job')
        record.father_job_designation = request.POST.get('father_job_designation')
        record.mother_job_designation = request.POST.get('mother_job_designation')
        record.father_business_type = request.POST.get('father_business_type')
        record.mother_business_type = request.POST.get('mother_business_type')
        record.father_number = request.POST.get('father_number')
        record.mother_number = request.POST.get('mother_number')
        record.father_office_address = request.POST.get('father_office_address')
        record.mother_office_address = request.POST.get('mother_office_address')
        #other candidate details
        record.complete_address = request.POST.get('complete_address')
        record.email = request.POST.get('email')
        record.candidate_number = request.POST.get('candidate_number')
        record.gender = request.POST.get('gender')
        #guardian details
        record.guardian_name = request.POST.get('guardian_name')
        #candidate dob
        record.dob = request.POST.get('dob')
        #12th class details
        record.board_12th = request.POST.get('board_12th')
        record.year_of_12th = request.POST.get('year_of_12th')
        record.rollno_12th = request.POST.get('rollno_12th')
        record.school_12th = request.POST.get('school_12th')
        record.aggregate_12th = float(request.POST.get('aggregate_12th'))
        record.first_subject_12th = request.POST.get('first_subject_12th')
        record.second_subject_12th = request.POST.get('second_subject_12th')
        record.third_subject_12th = request.POST.get('third_subject_12th')
        record.fourth_subject_12th = request.POST.get('fourth_subject_12th')
        record.other_subject_12th = request.POST.get('other_subject_12th')
        record.other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        #10th class details
        record.board_10th = request.POST.get('board_10th')
        record.year_of_10th = request.POST.get('year_of_10th')
        record.rollno_10th = request.POST.get('rollno_10th')
        record.school_10th = request.POST.get('school_10th')
        record.aggregate_10th = float(request.POST.get('aggregate_10th'))
        record.maths_10th = request.POST.get('maths_10th')
        record.science_10th = request.POST.get('science_10th')
        record.english_10th = request.POST.get('english_10th')
        record.sst_10th = request.POST.get('sst_10th')
        record.other_subject_10th = request.POST.get('other_subject_10th')
        record.other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        #JEE details
        record.cet_rank = request.POST.get('cet_rank')
        record.cet_or_cuet = request.POST.get('cet_or_cuet')
        record.cet_rollno = request.POST.get('cet_rollno')
        #special acheivements
        record.special_achievements = request.POST.get('special_achievements')
        record.save()
        # At this point, form is submitted successfully
        return redirect('bba_preview')
    # GET request: render the filled details
    record = Bba.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bba/bba-edit.html', context)







def bcom1(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bcom1.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        candidate_first_name = request.POST.get('candidate_first_name')
        candidate_middle_name = request.POST.get('candidate_middle_name')
        candidate_last_name = request.POST.get('candidate_last_name')
        email = request.POST.get('email')
        candidate_number = request.POST.get('candidate_number')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        category = request.POST.get('category')
        region = request.POST.get('region')
        # To track IP address and other info of user coming from request.META header
        ip_address = request.META.get('REMOTE_ADDR','-1')      # return -1 if no address found
        forwarded_address = request.META.get('HTTP_X_FORWARDED_FOR','-1')
        browser_info = request.META.get('HTTP_USER_AGENT','-1')
        created_at = str(datetime.datetime.now())[:19]        # only first 19 indexes so that it doesnt store microseconds
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BcomTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.candidate_first_name = candidate_first_name   
            existing_record.candidate_middle_name = candidate_middle_name
            existing_record.candidate_last_name = candidate_last_name
            existing_record.email = email
            existing_record.candidate_number = candidate_number
            existing_record.gender = gender
            existing_record.dob = dob
            existing_record.category = category
            existing_record.region = region
            existing_record.ip_address = ip_address
            existing_record.forwarded_address = forwarded_address
            existing_record.browser_info = browser_info
            existing_record.created_at = created_at
            # saving the updated record
            existing_record.save()
            return redirect ('bcom2')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BcomTemp(application_id=application_id, ipu_registration=ipu_registration,
                            candidate_first_name=candidate_first_name,
                            candidate_middle_name=candidate_middle_name, candidate_last_name=candidate_last_name,
                            email=email, candidate_number=candidate_number, gender=gender, dob=dob, category=category, region=region,
                            ip_address=ip_address, forwarded_address=forwarded_address, browser_info=browser_info, created_at=created_at,)
            newform.save()
            return redirect ('bcom2')
    # if the request method is not POST, then:
    # either user is coming from login page for the very first time
    # or user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bcom form by clicking the step-form (progress bar)
    # in all three cases we can render bcom1.html with context
    # to create context we will use the globally available variable application_id
    record = BcomTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bcom/bcom1.html', context)

def bcom2(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bcom2.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        father_first_name = request.POST.get('father_first_name')
        father_middle_name = request.POST.get('father_middle_name')
        father_last_name = request.POST.get('father_last_name')
        mother_first_name = request.POST.get('mother_first_name')
        mother_middle_name = request.POST.get('mother_middle_name')
        mother_last_name = request.POST.get('mother_last_name')
        father_qualification = request.POST.get('father_qualification')
        mother_qualification = request.POST.get('mother_qualification')
        father_job = request.POST.get('father_job')
        mother_job = request.POST.get('mother_job')
        father_job_designation = request.POST.get('father_job_designation')
        mother_job_designation = request.POST.get('mother_job_designation')
        father_business_type = request.POST.get('father_business_type')
        mother_business_type = request.POST.get('mother_business_type')
        father_number = request.POST.get('father_number')
        mother_number = request.POST.get('mother_number')
        father_office_address = request.POST.get('father_office_address')
        mother_office_address = request.POST.get('mother_office_address')
        guardian_name = request.POST.get('guardian_name')
        complete_address = request.POST.get('complete_address')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BcomTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.father_first_name = father_first_name   
            existing_record.father_middle_name = father_middle_name
            existing_record.father_last_name = father_last_name
            existing_record.mother_first_name = mother_first_name   
            existing_record.mother_middle_name = mother_middle_name
            existing_record.mother_last_name = mother_last_name
            existing_record.father_qualification = father_qualification
            existing_record.mother_qualification = mother_qualification
            existing_record.father_job = father_job
            existing_record.mother_job = mother_job
            existing_record.father_job_designation = father_job_designation
            existing_record.mother_job_designation = mother_job_designation
            existing_record.father_business_type = father_business_type   
            existing_record.mother_business_type = mother_business_type
            existing_record.father_office_address = father_office_address
            existing_record.mother_office_address = mother_office_address   
            existing_record.father_number = father_number
            existing_record.mother_number = mother_number
            existing_record.guardian_name = guardian_name   
            existing_record.complete_address = complete_address
            # saving the updated record
            existing_record.save()
            return redirect ('bcom3')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BcomTemp(application_id=application_id, ipu_registration=ipu_registration, 
                            father_first_name=father_first_name, father_middle_name=father_middle_name, father_last_name=father_last_name,
                            mother_first_name=mother_first_name, mother_middle_name=mother_middle_name, mother_last_name=mother_last_name,
                            father_qualification=father_qualification, mother_qualification=mother_qualification,
                            father_job=father_job, mother_job=mother_job,
                            father_job_designation=father_job_designation, mother_job_designation=mother_job_designation,
                            father_business_type=father_business_type, mother_business_type=mother_business_type,
                            father_number=father_number, mother_number=mother_number,
                            father_office_address=father_office_address, mother_office_address=mother_office_address,
                            complete_address=complete_address, guardian_name=guardian_name,)
            newform.save()
            return redirect ('bcom3')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bcom form by clicking the step-form (progress bar)
    # or user is coming from bcom1.html after saving his record
    # in all three cases we can render bcom2.html with context
    # to create context we will use the globally available variable application_id
    record = BcomTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bcom/bcom2.html', context)

def bcom3(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bcom3.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        board_12th = request.POST.get('board_12th')
        year_of_12th = request.POST.get('year_of_12th')
        rollno_12th = request.POST.get('rollno_12th')
        school_12th = request.POST.get('school_12th')
        aggregate_12th = float(request.POST.get('aggregate_12th'))
        first_subject_12th = request.POST.get('first_subject_12th')
        second_subject_12th = request.POST.get('second_subject_12th')
        third_subject_12th = request.POST.get('third_subject_12th')
        fourth_subject_12th = request.POST.get('fourth_subject_12th')
        other_subject_12th = request.POST.get('other_subject_12th')
        other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        board_10th = request.POST.get('board_10th')
        year_of_10th = request.POST.get('year_of_10th')
        rollno_10th = request.POST.get('rollno_10th')
        school_10th = request.POST.get('school_10th')
        aggregate_10th = float(request.POST.get('aggregate_10th'))
        maths_10th = request.POST.get('maths_10th')
        science_10th = request.POST.get('science_10th')
        english_10th = request.POST.get('english_10th')
        sst_10th = request.POST.get('sst_10th')
        other_subject_10th = request.POST.get('other_subject_10th')
        other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BcomTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.board_12th = board_12th   
            existing_record.year_of_12th = year_of_12th
            existing_record.rollno_12th = rollno_12th
            existing_record.school_12th = school_12th
            existing_record.aggregate_12th = aggregate_12th
            existing_record.first_subject_12th = first_subject_12th
            existing_record.second_subject_12th = second_subject_12th
            existing_record.third_subject_12th = third_subject_12th
            existing_record.fourth_subject_12th = fourth_subject_12th
            existing_record.other_subject_12th = other_subject_12th
            existing_record.other_subject_2_12th = other_subject_2_12th
            existing_record.board_10th = board_10th   
            existing_record.year_of_10th = year_of_10th
            existing_record.rollno_10th = rollno_10th
            existing_record.school_10th = school_10th
            existing_record.aggregate_10th = aggregate_10th
            existing_record.maths_10th = maths_10th
            existing_record.science_10th = science_10th
            existing_record.english_10th = english_10th
            existing_record.sst_10th = sst_10th
            existing_record.other_subject_10th = other_subject_10th
            existing_record.other_subject_2_10th = other_subject_2_10th
            # saving the updated record
            existing_record.save()
            return redirect ('bcom4')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BcomTemp(application_id=application_id, ipu_registration=ipu_registration,
                            board_12th=board_12th, year_of_12th=year_of_12th, rollno_12th=rollno_12th, school_12th=school_12th,
                            first_subject_12th=first_subject_12th, second_subject_12th=second_subject_12th, third_subject_12th=third_subject_12th, fourth_subject_12th=fourth_subject_12th,
                            other_subject_12th=other_subject_12th, other_subject_2_12th=other_subject_2_12th, aggregate_12th=aggregate_12th, 
                            board_10th=board_10th, year_of_10th=year_of_10th, rollno_10th=rollno_10th, school_10th=school_10th,
                            maths_10th=maths_10th, science_10th=science_10th, english_10th=english_10th, sst_10th=sst_10th,
                            other_subject_10th=other_subject_10th, other_subject_2_10th=other_subject_2_10th, aggregate_10th=aggregate_10th,)
            newform.save()
            return redirect ('bcom4')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bcom form by clicking the step-form (progress bar)
    # or user is coming from bcom2.html after saving his record
    # in all three cases we can render bcom3.html with context
    # to create context we will use the globally available variable application_id
    record = BcomTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bcom/bcom3.html', context)

def bcom4(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bcom4.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        cet_or_cuet = request.POST.get('cet_or_cuet')
        cet_rank = request.POST.get('cet_rank')
        cet_rollno = request.POST.get('cet_rollno')
        special_achievements = request.POST.get('special_achievements')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BcomTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.cet_or_cuet = cet_or_cuet   
            existing_record.cet_rank = cet_rank
            existing_record.cet_rollno = cet_rollno
            existing_record.special_achievements = special_achievements
            # saving the updated record
            existing_record.save()
            return redirect ('bcom5')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BcomTemp(application_id=application_id, ipu_registration=ipu_registration,
                            cet_rank=cet_rank, cet_rollno=cet_rollno, cet_or_cuet=cet_or_cuet,
                            special_achievements=special_achievements,)
            newform.save()
            return redirect ('bcom5')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bcom form by clicking the step-form (progress bar)
    # or user is coming from bcom3.html after saving his record
    # in all three cases we can render bcom4.html with context
    # to create context we will use the globally available variable application_id
    record = BcomTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bcom/bcom4.html', context)

def bcom5(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bcom5.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        passport_photo = request.FILES['passport_photo']
        cet_result = request.FILES['cet_result']
        marksheet_10th = request.FILES['marksheet_10th']
        marksheet_12th = request.FILES['marksheet_12th']
        aadhaar = request.FILES['aadhaar']
        pancard = request.FILES['pancard']
        ipuregistrationproof = request.FILES['ipuregistrationproof']
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BcomTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.passport_photo = passport_photo   
            existing_record.cet_result = cet_result
            existing_record.marksheet_10th = marksheet_10th
            existing_record.marksheet_12th = marksheet_12th
            existing_record.aadhaar = aadhaar
            existing_record.pancard = pancard
            existing_record.ipuregistrationproof = ipuregistrationproof
            # saving the updated record
            existing_record.save()
            # we will only redirect to payments on /bcom6 if all previous steps are filled
            # so to check that, we will check whether some value on each step is filled or not
            if not existing_record.candidate_first_name:
                return redirect('bcom1')
            if not existing_record.father_first_name:
                return redirect('bcom2')
            if not existing_record.board_10th:
                return redirect('bcom3')
            if not existing_record.cet_rollno:
                return redirect('bcom4')
            # if all of these details are filled, then we can safely proceed to payment
            return redirect ('bcom6')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BcomTemp(application_id=application_id, ipu_registration=ipu_registration,
                            passport_photo=passport_photo, cet_result=cet_result, marksheet_10th=marksheet_10th, marksheet_12th=marksheet_12th,
                            aadhaar=aadhaar, pancard=pancard, ipuregistrationproof=ipuregistrationproof)
            newform.save()
            # if its a new record, then we shall not allow to proceed to payment, so we are redirecting to /bcom1
            return redirect ('bcom1')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bcom form by clicking the step-form (progress bar)
    # or user is coming from bcom4.html after saving his record
    # in all three cases we can render bcom5.html with context
    # to create context we will use the globally available variable application_id
    record = BcomTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bcom/bcom5.html', context)

def bcom6(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bcom6.html page
    # so we shall save the data 
    if request.method == "POST" :
        transaction_id = request.POST.get('transaction_id')
        transaction_proof = request.FILES['transaction_proof']
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # (this will never be the case because we are not allowing user to come to /bcom6 if he hasn't already filled previous data , but still handling this case)
        # so, let's check if a record exists or not
        existing_record = BcomTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.transaction_id = transaction_id   
            existing_record.transaction_proof = transaction_proof
            # saving the updated record
            existing_record.save()
            # all steps are completed, now redirecting to final preview where data will move from temp table to permanent table 
            return redirect ('bcom')
        else:
            # saving all fields in a new object
            newform = BcomTemp(application_id=application_id, ipu_registration=ipu_registration,
                            transaction_id=transaction_id, transaction_proof=transaction_proof)
            newform.save()
            return redirect ('bcom')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bcom form by clicking the step-form (progress bar)
    # or user is coming from bcom5.html after saving his record
    # we shall allow the user only in the case when he has submitted all 5 steps
    record = BcomTemp.objects.all().filter(application_id = application_id).first()
    # so to check that, we will check whether some value on each step is filled or not
    # before that we can check if record exists or not:
    if not record:
        messages.info(request, 'Please fill candidate details before payment')
        return redirect('bcom1')
    if not record.candidate_first_name:
        messages.info(request, 'Please fill candidate details before payment')
        return redirect('bcom1')
    if not record.father_first_name:
        messages.info(request, 'Please fill parent details before payment')
        return redirect('bcom2')
    if not record.board_10th:
        messages.info(request, 'Please fill educational details before payment')
        return redirect('bcom3')
    if not record.cet_rollno:
        messages.info(request, 'Please fill qualifying details before payment')
        return redirect('bcom4')
    if not record.passport_photo:
        messages.info(request, 'Please upload documents before payment')
        return redirect("bcom5")
    # if all of these details are filled, then we can safely render /bcom6.html
    context = {'record': record}
    return render(request, 'bcom/bcom6.html', context)

# bcom
def bcom(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Submit" on the /bcom.html page
    # so we shall save the data in permanent table and delete from temporary table
    if request.method == 'POST':
        transaction_id = request.POST.get('transaction_id')
        # category and region
        category = request.POST.get('category')
        region = request.POST.get('region')
        candidate_first_name = request.POST.get('candidate_first_name')
        candidate_middle_name = request.POST.get('candidate_middle_name')
        candidate_last_name = request.POST.get('candidate_last_name')
        #father mother details
        father_first_name = request.POST.get('father_first_name')
        father_middle_name = request.POST.get('father_middle_name')
        father_last_name = request.POST.get('father_last_name')
        mother_first_name = request.POST.get('mother_first_name')
        mother_middle_name = request.POST.get('mother_middle_name')
        mother_last_name = request.POST.get('mother_last_name')
        father_qualification = request.POST.get('father_qualification')
        mother_qualification = request.POST.get('mother_qualification')
        father_job = request.POST.get('father_job')
        mother_job = request.POST.get('mother_job')
        father_job_designation = request.POST.get('father_job_designation')
        mother_job_designation = request.POST.get('mother_job_designation')
        father_business_type = request.POST.get('father_business_type')
        mother_business_type = request.POST.get('mother_business_type')
        father_number = request.POST.get('father_number')
        mother_number = request.POST.get('mother_number')
        father_office_address = request.POST.get('father_office_address')
        mother_office_address = request.POST.get('mother_office_address')
        #other candidate details
        complete_address = request.POST.get('complete_address')
        email = request.POST.get('email')
        candidate_number = request.POST.get('candidate_number')
        gender = request.POST.get('gender')
        #guardian details
        guardian_name = request.POST.get('guardian_name')
        #candidate dob
        dob = request.POST.get('dob')
        #12th class details
        board_12th = request.POST.get('board_12th')
        year_of_12th = request.POST.get('year_of_12th')
        rollno_12th = request.POST.get('rollno_12th')
        school_12th = request.POST.get('school_12th')
        aggregate_12th = float(request.POST.get('aggregate_12th'))
        first_subject_12th = request.POST.get('first_subject_12th')
        second_subject_12th = request.POST.get('second_subject_12th')
        third_subject_12th = request.POST.get('third_subject_12th')
        fourth_subject_12th = request.POST.get('fourth_subject_12th')
        other_subject_12th = request.POST.get('other_subject_12th')
        other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        #10th class details
        board_10th = request.POST.get('board_10th')
        year_of_10th = request.POST.get('year_of_10th')
        rollno_10th = request.POST.get('rollno_10th')
        school_10th = request.POST.get('school_10th')
        aggregate_10th = float(request.POST.get('aggregate_10th'))
        maths_10th = request.POST.get('maths_10th')
        science_10th = request.POST.get('science_10th')
        english_10th = request.POST.get('english_10th')
        sst_10th = request.POST.get('sst_10th')
        other_subject_10th = request.POST.get('other_subject_10th')
        other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        #CET details
        cet_or_cuet = request.POST.get('cet_or_cuet')
        cet_rank = request.POST.get('cet_rank')
        cet_rollno = request.POST.get('cet_rollno')
        #special acheivements
        special_achievements = request.POST.get('special_achievements')
        # To track IP address and other info of user coming from request.META header
        ip_address = request.META.get('REMOTE_ADDR','-1')      # return -1 if no address found
        forwarded_address = request.META.get('HTTP_X_FORWARDED_FOR','-1')
        browser_info = request.META.get('HTTP_USER_AGENT','-1')
        created_at = str(datetime.datetime.now())[:19]        # only first 19 indexes so that it doesnt store microseconds
        # saving all fields expect files in a new object
        newform = Bcom(candidate_first_name=candidate_first_name, candidate_middle_name=candidate_middle_name, candidate_last_name=candidate_last_name,
                        father_first_name=father_first_name, father_middle_name=father_middle_name, father_last_name=father_last_name,
                        mother_first_name=mother_first_name, mother_middle_name=mother_middle_name, mother_last_name=mother_last_name,
                        father_qualification=father_qualification, mother_qualification=mother_qualification,
                        father_job=father_job, mother_job=mother_job,
                        father_job_designation=father_job_designation, mother_job_designation=mother_job_designation,
                        father_business_type=father_business_type, mother_business_type=mother_business_type,
                        father_number=father_number, mother_number=mother_number,
                        father_office_address=father_office_address, mother_office_address=mother_office_address,
                        complete_address=complete_address, candidate_number=candidate_number,
                        guardian_name=guardian_name, email=email, dob=dob, gender=gender,
                        board_12th=board_12th, year_of_12th=year_of_12th, rollno_12th=rollno_12th, school_12th=school_12th,
                        first_subject_12th=first_subject_12th, second_subject_12th=second_subject_12th, third_subject_12th=third_subject_12th, fourth_subject_12th=fourth_subject_12th,
                        other_subject_12th=other_subject_12th, other_subject_2_12th=other_subject_2_12th, aggregate_12th=aggregate_12th, 
                        board_10th=board_10th, year_of_10th=year_of_10th, rollno_10th=rollno_10th, school_10th=school_10th,
                        maths_10th=maths_10th, science_10th=science_10th, english_10th=english_10th, sst_10th=sst_10th,
                        other_subject_10th=other_subject_10th, other_subject_2_10th=other_subject_2_10th, aggregate_10th=aggregate_10th, 
                        cet_rank=cet_rank, cet_rollno=cet_rollno, cet_or_cuet=cet_or_cuet,
                        ipu_registration=ipu_registration, special_achievements=special_achievements,
                        application_id=application_id, transaction_id=transaction_id,
                        category=category, region=region,
                        ip_address=ip_address, forwarded_address=forwarded_address, browser_info=browser_info, created_at=created_at,)
        newform.save()
        # now saving files after instance is created
        temp_record = BcomTemp.objects.get(application_id=application_id)
        newobj = Bcom.objects.get(pk=newform.pk)
        newobj.passport_photo = temp_record.passport_photo
        newobj.cet_result = temp_record.cet_result
        newobj.marksheet_10th = temp_record.marksheet_10th
        newobj.marksheet_12th = temp_record.marksheet_12th
        newobj.aadhaar = temp_record.aadhaar
        newobj.pancard = temp_record.pancard
        newobj.ipuregistrationproof = temp_record.ipuregistrationproof
        newobj.transaction_proof = temp_record.transaction_proof
        newobj.save()
        temp_record.delete()   # deleting the temporary record
        # At this point, form is submitted successfully
        return redirect('bcom_preview')
    record = BcomTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bcom/bcom.html', context)
    
# bcom Preview
def bcom_preview(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    record = Bcom.objects.filter(application_id=application_id).first()
    context = {'record': record}
    return render(request, 'bcom/bcom-preview.html', context)

# Edit bcom (after final submission)
def bcom_edit(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save" on the /bcom-edit.html page
    # so we shall save the data in permanent table and delete from temporary table
    if request.method == 'POST':
        record = Bcom.objects.all().filter(application_id = application_id).first()
        record.transaction_id = request.POST.get('transaction_id')
        # category and region
        record.category = request.POST.get('category')
        record.region = request.POST.get('region')
        record.candidate_first_name = request.POST.get('candidate_first_name')
        record.candidate_middle_name = request.POST.get('candidate_middle_name')
        record.candidate_last_name = request.POST.get('candidate_last_name')
        #father mother details
        record.father_first_name = request.POST.get('father_first_name')
        record.father_middle_name = request.POST.get('father_middle_name')
        record.father_last_name = request.POST.get('father_last_name')
        record.mother_first_name = request.POST.get('mother_first_name')
        record.mother_middle_name = request.POST.get('mother_middle_name')
        record.mother_last_name = request.POST.get('mother_last_name')
        record.father_qualification = request.POST.get('father_qualification')
        record.mother_qualification = request.POST.get('mother_qualification')
        record.father_job = request.POST.get('father_job')
        record.mother_job = request.POST.get('mother_job')
        record.father_job_designation = request.POST.get('father_job_designation')
        record.mother_job_designation = request.POST.get('mother_job_designation')
        record.father_business_type = request.POST.get('father_business_type')
        record.mother_business_type = request.POST.get('mother_business_type')
        record.father_number = request.POST.get('father_number')
        record.mother_number = request.POST.get('mother_number')
        record.father_office_address = request.POST.get('father_office_address')
        record.mother_office_address = request.POST.get('mother_office_address')
        #other candidate details
        record.complete_address = request.POST.get('complete_address')
        record.email = request.POST.get('email')
        record.candidate_number = request.POST.get('candidate_number')
        record.gender = request.POST.get('gender')
        #guardian details
        record.guardian_name = request.POST.get('guardian_name')
        #candidate dob
        record.dob = request.POST.get('dob')
        #12th class details
        record.board_12th = request.POST.get('board_12th')
        record.year_of_12th = request.POST.get('year_of_12th')
        record.rollno_12th = request.POST.get('rollno_12th')
        record.school_12th = request.POST.get('school_12th')
        record.aggregate_12th = float(request.POST.get('aggregate_12th'))
        record.first_subject_12th = request.POST.get('first_subject_12th')
        record.second_subject_12th = request.POST.get('second_subject_12th')
        record.third_subject_12th = request.POST.get('third_subject_12th')
        record.fourth_subject_12th = request.POST.get('fourth_subject_12th')
        record.other_subject_12th = request.POST.get('other_subject_12th')
        record.other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        #10th class details
        record.board_10th = request.POST.get('board_10th')
        record.year_of_10th = request.POST.get('year_of_10th')
        record.rollno_10th = request.POST.get('rollno_10th')
        record.school_10th = request.POST.get('school_10th')
        record.aggregate_10th = float(request.POST.get('aggregate_10th'))
        record.maths_10th = request.POST.get('maths_10th')
        record.science_10th = request.POST.get('science_10th')
        record.english_10th = request.POST.get('english_10th')
        record.sst_10th = request.POST.get('sst_10th')
        record.other_subject_10th = request.POST.get('other_subject_10th')
        record.other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        #JEE details
        record.cet_rank = request.POST.get('cet_rank')
        record.cet_or_cuet = request.POST.get('cet_or_cuet')
        record.cet_rollno = request.POST.get('cet_rollno')
        #special acheivements
        record.special_achievements = request.POST.get('special_achievements')
        record.save()
        # At this point, form is submitted successfully
        return redirect('bcom_preview')
    # GET request: render the filled details
    record = Bcom.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bcom/bcom-edit.html', context)








def bjmc1(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bjmc1.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        candidate_first_name = request.POST.get('candidate_first_name')
        candidate_middle_name = request.POST.get('candidate_middle_name')
        candidate_last_name = request.POST.get('candidate_last_name')
        email = request.POST.get('email')
        candidate_number = request.POST.get('candidate_number')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        category = request.POST.get('category')
        region = request.POST.get('region')
        # To track IP address and other info of user coming from request.META header
        ip_address = request.META.get('REMOTE_ADDR','-1')      # return -1 if no address found
        forwarded_address = request.META.get('HTTP_X_FORWARDED_FOR','-1')
        browser_info = request.META.get('HTTP_USER_AGENT','-1')
        created_at = str(datetime.datetime.now())[:19]        # only first 19 indexes so that it doesnt store microseconds
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BjmcTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.candidate_first_name = candidate_first_name   
            existing_record.candidate_middle_name = candidate_middle_name
            existing_record.candidate_last_name = candidate_last_name
            existing_record.email = email
            existing_record.candidate_number = candidate_number
            existing_record.gender = gender
            existing_record.dob = dob
            existing_record.category = category
            existing_record.region = region
            existing_record.ip_address = ip_address
            existing_record.forwarded_address = forwarded_address
            existing_record.browser_info = browser_info
            existing_record.created_at = created_at
            # saving the updated record
            existing_record.save()
            return redirect ('bjmc2')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BjmcTemp(application_id=application_id, ipu_registration=ipu_registration,
                            candidate_first_name=candidate_first_name,
                            candidate_middle_name=candidate_middle_name, candidate_last_name=candidate_last_name,
                            email=email, candidate_number=candidate_number, gender=gender, dob=dob, category=category, region=region,
                            ip_address=ip_address, forwarded_address=forwarded_address, browser_info=browser_info, created_at=created_at,)
            newform.save()
            return redirect ('bjmc2')
    # if the request method is not POST, then:
    # either user is coming from login page for the very first time
    # or user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bjmc form by clicking the step-form (progress bar)
    # in all three cases we can render bjmc1.html with context
    # to create context we will use the globally available variable application_id
    record = BjmcTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bjmc/bjmc1.html', context)

def bjmc2(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bjmc2.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        father_first_name = request.POST.get('father_first_name')
        father_middle_name = request.POST.get('father_middle_name')
        father_last_name = request.POST.get('father_last_name')
        mother_first_name = request.POST.get('mother_first_name')
        mother_middle_name = request.POST.get('mother_middle_name')
        mother_last_name = request.POST.get('mother_last_name')
        father_qualification = request.POST.get('father_qualification')
        mother_qualification = request.POST.get('mother_qualification')
        father_job = request.POST.get('father_job')
        mother_job = request.POST.get('mother_job')
        father_job_designation = request.POST.get('father_job_designation')
        mother_job_designation = request.POST.get('mother_job_designation')
        father_business_type = request.POST.get('father_business_type')
        mother_business_type = request.POST.get('mother_business_type')
        father_number = request.POST.get('father_number')
        mother_number = request.POST.get('mother_number')
        father_office_address = request.POST.get('father_office_address')
        mother_office_address = request.POST.get('mother_office_address')
        guardian_name = request.POST.get('guardian_name')
        complete_address = request.POST.get('complete_address')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BjmcTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.father_first_name = father_first_name   
            existing_record.father_middle_name = father_middle_name
            existing_record.father_last_name = father_last_name
            existing_record.mother_first_name = mother_first_name   
            existing_record.mother_middle_name = mother_middle_name
            existing_record.mother_last_name = mother_last_name
            existing_record.father_qualification = father_qualification
            existing_record.mother_qualification = mother_qualification
            existing_record.father_job = father_job
            existing_record.mother_job = mother_job
            existing_record.father_job_designation = father_job_designation
            existing_record.mother_job_designation = mother_job_designation
            existing_record.father_business_type = father_business_type   
            existing_record.mother_business_type = mother_business_type
            existing_record.father_office_address = father_office_address
            existing_record.mother_office_address = mother_office_address   
            existing_record.father_number = father_number
            existing_record.mother_number = mother_number
            existing_record.guardian_name = guardian_name   
            existing_record.complete_address = complete_address
            # saving the updated record
            existing_record.save()
            return redirect ('bjmc3')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BjmcTemp(application_id=application_id, ipu_registration=ipu_registration, 
                            father_first_name=father_first_name, father_middle_name=father_middle_name, father_last_name=father_last_name,
                            mother_first_name=mother_first_name, mother_middle_name=mother_middle_name, mother_last_name=mother_last_name,
                            father_qualification=father_qualification, mother_qualification=mother_qualification,
                            father_job=father_job, mother_job=mother_job,
                            father_job_designation=father_job_designation, mother_job_designation=mother_job_designation,
                            father_business_type=father_business_type, mother_business_type=mother_business_type,
                            father_number=father_number, mother_number=mother_number,
                            father_office_address=father_office_address, mother_office_address=mother_office_address,
                            complete_address=complete_address, guardian_name=guardian_name,)
            newform.save()
            return redirect ('bjmc3')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bjmc form by clicking the step-form (progress bar)
    # or user is coming from bjmc1.html after saving his record
    # in all three cases we can render bjmc2.html with context
    # to create context we will use the globally available variable application_id
    record = BjmcTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bjmc/bjmc2.html', context)

def bjmc3(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bjmc3.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        board_12th = request.POST.get('board_12th')
        year_of_12th = request.POST.get('year_of_12th')
        rollno_12th = request.POST.get('rollno_12th')
        school_12th = request.POST.get('school_12th')
        aggregate_12th = float(request.POST.get('aggregate_12th'))
        first_subject_12th = request.POST.get('first_subject_12th')
        second_subject_12th = request.POST.get('second_subject_12th')
        third_subject_12th = request.POST.get('third_subject_12th')
        fourth_subject_12th = request.POST.get('fourth_subject_12th')
        other_subject_12th = request.POST.get('other_subject_12th')
        other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        board_10th = request.POST.get('board_10th')
        year_of_10th = request.POST.get('year_of_10th')
        rollno_10th = request.POST.get('rollno_10th')
        school_10th = request.POST.get('school_10th')
        aggregate_10th = float(request.POST.get('aggregate_10th'))
        maths_10th = request.POST.get('maths_10th')
        science_10th = request.POST.get('science_10th')
        english_10th = request.POST.get('english_10th')
        sst_10th = request.POST.get('sst_10th')
        other_subject_10th = request.POST.get('other_subject_10th')
        other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BjmcTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.board_12th = board_12th   
            existing_record.year_of_12th = year_of_12th
            existing_record.rollno_12th = rollno_12th
            existing_record.school_12th = school_12th
            existing_record.aggregate_12th = aggregate_12th
            existing_record.first_subject_12th = first_subject_12th
            existing_record.second_subject_12th = second_subject_12th
            existing_record.third_subject_12th = third_subject_12th
            existing_record.fourth_subject_12th = fourth_subject_12th
            existing_record.other_subject_12th = other_subject_12th
            existing_record.other_subject_2_12th = other_subject_2_12th
            existing_record.board_10th = board_10th   
            existing_record.year_of_10th = year_of_10th
            existing_record.rollno_10th = rollno_10th
            existing_record.school_10th = school_10th
            existing_record.aggregate_10th = aggregate_10th
            existing_record.maths_10th = maths_10th
            existing_record.science_10th = science_10th
            existing_record.english_10th = english_10th
            existing_record.sst_10th = sst_10th
            existing_record.other_subject_10th = other_subject_10th
            existing_record.other_subject_2_10th = other_subject_2_10th
            # saving the updated record
            existing_record.save()
            return redirect ('bjmc4')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BjmcTemp(application_id=application_id, ipu_registration=ipu_registration,
                            board_12th=board_12th, year_of_12th=year_of_12th, rollno_12th=rollno_12th, school_12th=school_12th,
                            first_subject_12th=first_subject_12th, second_subject_12th=second_subject_12th, third_subject_12th=third_subject_12th, fourth_subject_12th=fourth_subject_12th,
                            other_subject_12th=other_subject_12th, other_subject_2_12th=other_subject_2_12th, aggregate_12th=aggregate_12th, 
                            board_10th=board_10th, year_of_10th=year_of_10th, rollno_10th=rollno_10th, school_10th=school_10th,
                            maths_10th=maths_10th, science_10th=science_10th, english_10th=english_10th, sst_10th=sst_10th,
                            other_subject_10th=other_subject_10th, other_subject_2_10th=other_subject_2_10th, aggregate_10th=aggregate_10th,)
            newform.save()
            return redirect ('bjmc4')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bjmc form by clicking the step-form (progress bar)
    # or user is coming from bjmc2.html after saving his record
    # in all three cases we can render bjmc3.html with context
    # to create context we will use the globally available variable application_id
    record = BjmcTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bjmc/bjmc3.html', context)

def bjmc4(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bjmc4.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        cet_or_cuet = request.POST.get('cet_or_cuet')
        cet_rank = request.POST.get('cet_rank')
        cet_rollno = request.POST.get('cet_rollno')
        special_achievements = request.POST.get('special_achievements')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BjmcTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.cet_or_cuet = cet_or_cuet   
            existing_record.cet_rank = cet_rank
            existing_record.cet_rollno = cet_rollno
            existing_record.special_achievements = special_achievements
            # saving the updated record
            existing_record.save()
            return redirect ('bjmc5')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BjmcTemp(application_id=application_id, ipu_registration=ipu_registration,
                            cet_rank=cet_rank, cet_rollno=cet_rollno, cet_or_cuet=cet_or_cuet,
                            special_achievements=special_achievements,)
            newform.save()
            return redirect ('bjmc5')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bjmc form by clicking the step-form (progress bar)
    # or user is coming from bjmc3.html after saving his record
    # in all three cases we can render bjmc4.html with context
    # to create context we will use the globally available variable application_id
    record = BjmcTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bjmc/bjmc4.html', context)

def bjmc5(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bjmc5.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        passport_photo = request.FILES['passport_photo']
        cet_result = request.FILES['cet_result']
        marksheet_10th = request.FILES['marksheet_10th']
        marksheet_12th = request.FILES['marksheet_12th']
        aadhaar = request.FILES['aadhaar']
        pancard = request.FILES['pancard']
        ipuregistrationproof = request.FILES['ipuregistrationproof']
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BjmcTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.passport_photo = passport_photo   
            existing_record.cet_result = cet_result
            existing_record.marksheet_10th = marksheet_10th
            existing_record.marksheet_12th = marksheet_12th
            existing_record.aadhaar = aadhaar
            existing_record.pancard = pancard
            existing_record.ipuregistrationproof = ipuregistrationproof
            # saving the updated record
            existing_record.save()
            # we will only redirect to payments on /bjmc6 if all previous steps are filled
            # so to check that, we will check whether some value on each step is filled or not
            if not existing_record.candidate_first_name:
                return redirect('bjmc1')
            if not existing_record.father_first_name:
                return redirect('bjmc2')
            if not existing_record.board_10th:
                return redirect('bjmc3')
            if not existing_record.cet_rollno:
                return redirect('bjmc4')
            # if all of these details are filled, then we can safely proceed to payment
            return redirect ('bjmc6')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BjmcTemp(application_id=application_id, ipu_registration=ipu_registration,
                            passport_photo=passport_photo, cet_result=cet_result, marksheet_10th=marksheet_10th, marksheet_12th=marksheet_12th,
                            aadhaar=aadhaar, pancard=pancard, ipuregistrationproof=ipuregistrationproof)
            newform.save()
            # if its a new record, then we shall not allow to proceed to payment, so we are redirecting to /bjmc1
            return redirect ('bjmc1')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bjmc form by clicking the step-form (progress bar)
    # or user is coming from bjmc4.html after saving his record
    # in all three cases we can render bjmc5.html with context
    # to create context we will use the globally available variable application_id
    record = BjmcTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bjmc/bjmc5.html', context)

def bjmc6(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bjmc6.html page
    # so we shall save the data 
    if request.method == "POST" :
        transaction_id = request.POST.get('transaction_id')
        transaction_proof = request.FILES['transaction_proof']
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # (this will never be the case because we are not allowing user to come to /bjmc6 if he hasn't already filled previous data , but still handling this case)
        # so, let's check if a record exists or not
        existing_record = BjmcTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.transaction_id = transaction_id   
            existing_record.transaction_proof = transaction_proof
            # saving the updated record
            existing_record.save()
            # all steps are completed, now redirecting to final preview where data will move from temp table to permanent table 
            return redirect ('bjmc')
        else:
            # saving all fields in a new object
            newform = BjmcTemp(application_id=application_id, ipu_registration=ipu_registration,
                            transaction_id=transaction_id, transaction_proof=transaction_proof)
            newform.save()
            return redirect ('bjmc')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bjmc form by clicking the step-form (progress bar)
    # or user is coming from bjmc5.html after saving his record
    # we shall allow the user only in the case when he has submitted all 5 steps
    record = BjmcTemp.objects.all().filter(application_id = application_id).first()
    # so to check that, we will check whether some value on each step is filled or not
    # before that we can check if record exists or not:
    if not record:
        messages.info(request, 'Please fill candidate details before payment')
        return redirect('bjmc1')
    if not record.candidate_first_name:
        messages.info(request, 'Please fill candidate details before payment')
        return redirect('bjmc1')
    if not record.father_first_name:
        messages.info(request, 'Please fill parent details before payment')
        return redirect('bjmc2')
    if not record.board_10th:
        messages.info(request, 'Please fill educational details before payment')
        return redirect('bjmc3')
    if not record.cet_rollno:
        messages.info(request, 'Please fill qualifying details before payment')
        return redirect('bjmc4')
    if not record.passport_photo:
        messages.info(request, 'Please upload documents before payment')
        return redirect("bjmc5")
    # if all of these details are filled, then we can safely render /bjmc6.html
    context = {'record': record}
    return render(request, 'bjmc/bjmc6.html', context)

# Bjmc
def bjmc(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Submit" on the /bjmc.html page
    # so we shall save the data in permanent table and delete from temporary table
    if request.method == 'POST':
        transaction_id = request.POST.get('transaction_id')
        # category and region
        category = request.POST.get('category')
        region = request.POST.get('region')
        candidate_first_name = request.POST.get('candidate_first_name')
        candidate_middle_name = request.POST.get('candidate_middle_name')
        candidate_last_name = request.POST.get('candidate_last_name')
        #father mother details
        father_first_name = request.POST.get('father_first_name')
        father_middle_name = request.POST.get('father_middle_name')
        father_last_name = request.POST.get('father_last_name')
        mother_first_name = request.POST.get('mother_first_name')
        mother_middle_name = request.POST.get('mother_middle_name')
        mother_last_name = request.POST.get('mother_last_name')
        father_qualification = request.POST.get('father_qualification')
        mother_qualification = request.POST.get('mother_qualification')
        father_job = request.POST.get('father_job')
        mother_job = request.POST.get('mother_job')
        father_job_designation = request.POST.get('father_job_designation')
        mother_job_designation = request.POST.get('mother_job_designation')
        father_business_type = request.POST.get('father_business_type')
        mother_business_type = request.POST.get('mother_business_type')
        father_number = request.POST.get('father_number')
        mother_number = request.POST.get('mother_number')
        father_office_address = request.POST.get('father_office_address')
        mother_office_address = request.POST.get('mother_office_address')
        #other candidate details
        complete_address = request.POST.get('complete_address')
        email = request.POST.get('email')
        candidate_number = request.POST.get('candidate_number')
        gender = request.POST.get('gender')
        #guardian details
        guardian_name = request.POST.get('guardian_name')
        #candidate dob
        dob = request.POST.get('dob')
        #12th class details
        board_12th = request.POST.get('board_12th')
        year_of_12th = request.POST.get('year_of_12th')
        rollno_12th = request.POST.get('rollno_12th')
        school_12th = request.POST.get('school_12th')
        aggregate_12th = float(request.POST.get('aggregate_12th'))
        first_subject_12th = request.POST.get('first_subject_12th')
        second_subject_12th = request.POST.get('second_subject_12th')
        third_subject_12th = request.POST.get('third_subject_12th')
        fourth_subject_12th = request.POST.get('fourth_subject_12th')
        other_subject_12th = request.POST.get('other_subject_12th')
        other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        #10th class details
        board_10th = request.POST.get('board_10th')
        year_of_10th = request.POST.get('year_of_10th')
        rollno_10th = request.POST.get('rollno_10th')
        school_10th = request.POST.get('school_10th')
        aggregate_10th = float(request.POST.get('aggregate_10th'))
        maths_10th = request.POST.get('maths_10th')
        science_10th = request.POST.get('science_10th')
        english_10th = request.POST.get('english_10th')
        sst_10th = request.POST.get('sst_10th')
        other_subject_10th = request.POST.get('other_subject_10th')
        other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        #CET details
        cet_or_cuet = request.POST.get('cet_or_cuet')
        cet_rank = request.POST.get('cet_rank')
        cet_rollno = request.POST.get('cet_rollno')
        #special acheivements
        special_achievements = request.POST.get('special_achievements')
        # To track IP address and other info of user coming from request.META header
        ip_address = request.META.get('REMOTE_ADDR','-1')      # return -1 if no address found
        forwarded_address = request.META.get('HTTP_X_FORWARDED_FOR','-1')
        browser_info = request.META.get('HTTP_USER_AGENT','-1')
        created_at = str(datetime.datetime.now())[:19]        # only first 19 indexes so that it doesnt store microseconds
        # saving all fields expect files in a new object
        newform = Bjmc(candidate_first_name=candidate_first_name, candidate_middle_name=candidate_middle_name, candidate_last_name=candidate_last_name,
                        father_first_name=father_first_name, father_middle_name=father_middle_name, father_last_name=father_last_name,
                        mother_first_name=mother_first_name, mother_middle_name=mother_middle_name, mother_last_name=mother_last_name,
                        father_qualification=father_qualification, mother_qualification=mother_qualification,
                        father_job=father_job, mother_job=mother_job,
                        father_job_designation=father_job_designation, mother_job_designation=mother_job_designation,
                        father_business_type=father_business_type, mother_business_type=mother_business_type,
                        father_number=father_number, mother_number=mother_number,
                        father_office_address=father_office_address, mother_office_address=mother_office_address,
                        complete_address=complete_address, candidate_number=candidate_number,
                        guardian_name=guardian_name, email=email, dob=dob, gender=gender,
                        board_12th=board_12th, year_of_12th=year_of_12th, rollno_12th=rollno_12th, school_12th=school_12th,
                        first_subject_12th=first_subject_12th, second_subject_12th=second_subject_12th, third_subject_12th=third_subject_12th, fourth_subject_12th=fourth_subject_12th,
                        other_subject_12th=other_subject_12th, other_subject_2_12th=other_subject_2_12th, aggregate_12th=aggregate_12th, 
                        board_10th=board_10th, year_of_10th=year_of_10th, rollno_10th=rollno_10th, school_10th=school_10th,
                        maths_10th=maths_10th, science_10th=science_10th, english_10th=english_10th, sst_10th=sst_10th,
                        other_subject_10th=other_subject_10th, other_subject_2_10th=other_subject_2_10th, aggregate_10th=aggregate_10th, 
                        cet_rank=cet_rank, cet_rollno=cet_rollno, cet_or_cuet=cet_or_cuet,
                        ipu_registration=ipu_registration, special_achievements=special_achievements,
                        application_id=application_id, transaction_id=transaction_id,
                        category=category, region=region,
                        ip_address=ip_address, forwarded_address=forwarded_address, browser_info=browser_info, created_at=created_at,)
        newform.save()
        # now saving files after instance is created
        temp_record = BjmcTemp.objects.get(application_id=application_id)
        newobj = Bjmc.objects.get(pk=newform.pk)
        newobj.passport_photo = temp_record.passport_photo
        newobj.cet_result = temp_record.cet_result
        newobj.marksheet_10th = temp_record.marksheet_10th
        newobj.marksheet_12th = temp_record.marksheet_12th
        newobj.aadhaar = temp_record.aadhaar
        newobj.pancard = temp_record.pancard
        newobj.ipuregistrationproof = temp_record.ipuregistrationproof
        newobj.transaction_proof = temp_record.transaction_proof
        newobj.save()
        temp_record.delete()   # deleting the temporary record
        # At this point, form is submitted successfully
        return redirect('bjmc_preview')
    record = BjmcTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bjmc/bjmc.html', context)
    
# Bjmc Preview
def bjmc_preview(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    record = Bjmc.objects.filter(application_id=application_id).first()
    context = {'record': record}
    return render(request, 'bjmc/bjmc-preview.html', context)

# Edit Bjmc (after final submission)
def bjmc_edit(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save" on the /bjmc-edit.html page
    # so we shall save the data in permanent table and delete from temporary table
    if request.method == 'POST':
        record = Bjmc.objects.all().filter(application_id = application_id).first()
        record.transaction_id = request.POST.get('transaction_id')
        # category and region
        record.category = request.POST.get('category')
        record.region = request.POST.get('region')
        record.candidate_first_name = request.POST.get('candidate_first_name')
        record.candidate_middle_name = request.POST.get('candidate_middle_name')
        record.candidate_last_name = request.POST.get('candidate_last_name')
        #father mother details
        record.father_first_name = request.POST.get('father_first_name')
        record.father_middle_name = request.POST.get('father_middle_name')
        record.father_last_name = request.POST.get('father_last_name')
        record.mother_first_name = request.POST.get('mother_first_name')
        record.mother_middle_name = request.POST.get('mother_middle_name')
        record.mother_last_name = request.POST.get('mother_last_name')
        record.father_qualification = request.POST.get('father_qualification')
        record.mother_qualification = request.POST.get('mother_qualification')
        record.father_job = request.POST.get('father_job')
        record.mother_job = request.POST.get('mother_job')
        record.father_job_designation = request.POST.get('father_job_designation')
        record.mother_job_designation = request.POST.get('mother_job_designation')
        record.father_business_type = request.POST.get('father_business_type')
        record.mother_business_type = request.POST.get('mother_business_type')
        record.father_number = request.POST.get('father_number')
        record.mother_number = request.POST.get('mother_number')
        record.father_office_address = request.POST.get('father_office_address')
        record.mother_office_address = request.POST.get('mother_office_address')
        #other candidate details
        record.complete_address = request.POST.get('complete_address')
        record.email = request.POST.get('email')
        record.candidate_number = request.POST.get('candidate_number')
        record.gender = request.POST.get('gender')
        #guardian details
        record.guardian_name = request.POST.get('guardian_name')
        #candidate dob
        record.dob = request.POST.get('dob')
        #12th class details
        record.board_12th = request.POST.get('board_12th')
        record.year_of_12th = request.POST.get('year_of_12th')
        record.rollno_12th = request.POST.get('rollno_12th')
        record.school_12th = request.POST.get('school_12th')
        record.aggregate_12th = float(request.POST.get('aggregate_12th'))
        record.first_subject_12th = request.POST.get('first_subject_12th')
        record.second_subject_12th = request.POST.get('second_subject_12th')
        record.third_subject_12th = request.POST.get('third_subject_12th')
        record.fourth_subject_12th = request.POST.get('fourth_subject_12th')
        record.other_subject_12th = request.POST.get('other_subject_12th')
        record.other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        #10th class details
        record.board_10th = request.POST.get('board_10th')
        record.year_of_10th = request.POST.get('year_of_10th')
        record.rollno_10th = request.POST.get('rollno_10th')
        record.school_10th = request.POST.get('school_10th')
        record.aggregate_10th = float(request.POST.get('aggregate_10th'))
        record.maths_10th = request.POST.get('maths_10th')
        record.science_10th = request.POST.get('science_10th')
        record.english_10th = request.POST.get('english_10th')
        record.sst_10th = request.POST.get('sst_10th')
        record.other_subject_10th = request.POST.get('other_subject_10th')
        record.other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        #JEE details
        record.cet_rank = request.POST.get('cet_rank')
        record.cet_or_cuet = request.POST.get('cet_or_cuet')
        record.cet_rollno = request.POST.get('cet_rollno')
        #special acheivements
        record.special_achievements = request.POST.get('special_achievements')
        record.save()
        # At this point, form is submitted successfully
        return redirect('bjmc_preview')
    # GET request: render the filled details
    record = Bjmc.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bjmc/bjmc-edit.html', context)









def ballb1(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /ballb1.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        candidate_first_name = request.POST.get('candidate_first_name')
        candidate_middle_name = request.POST.get('candidate_middle_name')
        candidate_last_name = request.POST.get('candidate_last_name')
        email = request.POST.get('email')
        candidate_number = request.POST.get('candidate_number')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        category = request.POST.get('category')
        region = request.POST.get('region')
        # To track IP address and other info of user coming from request.META header
        ip_address = request.META.get('REMOTE_ADDR','-1')      # return -1 if no address found
        forwarded_address = request.META.get('HTTP_X_FORWARDED_FOR','-1')
        browser_info = request.META.get('HTTP_USER_AGENT','-1')
        created_at = str(datetime.datetime.now())[:19]        # only first 19 indexes so that it doesnt store microseconds
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BallbTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.candidate_first_name = candidate_first_name   
            existing_record.candidate_middle_name = candidate_middle_name
            existing_record.candidate_last_name = candidate_last_name
            existing_record.email = email
            existing_record.candidate_number = candidate_number
            existing_record.gender = gender
            existing_record.dob = dob
            existing_record.category = category
            existing_record.region = region
            existing_record.ip_address = ip_address
            existing_record.forwarded_address = forwarded_address
            existing_record.browser_info = browser_info
            existing_record.created_at = created_at
            # saving the updated record
            existing_record.save()
            return redirect ('ballb2')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BallbTemp(application_id=application_id, ipu_registration=ipu_registration,
                            candidate_first_name=candidate_first_name,
                            candidate_middle_name=candidate_middle_name, candidate_last_name=candidate_last_name,
                            email=email, candidate_number=candidate_number, gender=gender, dob=dob, category=category, region=region,
                            ip_address=ip_address, forwarded_address=forwarded_address, browser_info=browser_info, created_at=created_at,)
            newform.save()
            return redirect ('ballb2')
    # if the request method is not POST, then:
    # either user is coming from login page for the very first time
    # or user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of ballb form by clicking the step-form (progress bar)
    # in all three cases we can render ballb1.html with context
    # to create context we will use the globally available variable application_id
    record = BallbTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'ballb/ballb1.html', context)

def ballb2(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /ballb2.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        father_first_name = request.POST.get('father_first_name')
        father_middle_name = request.POST.get('father_middle_name')
        father_last_name = request.POST.get('father_last_name')
        mother_first_name = request.POST.get('mother_first_name')
        mother_middle_name = request.POST.get('mother_middle_name')
        mother_last_name = request.POST.get('mother_last_name')
        father_qualification = request.POST.get('father_qualification')
        mother_qualification = request.POST.get('mother_qualification')
        father_job = request.POST.get('father_job')
        mother_job = request.POST.get('mother_job')
        father_job_designation = request.POST.get('father_job_designation')
        mother_job_designation = request.POST.get('mother_job_designation')
        father_business_type = request.POST.get('father_business_type')
        mother_business_type = request.POST.get('mother_business_type')
        father_number = request.POST.get('father_number')
        mother_number = request.POST.get('mother_number')
        father_office_address = request.POST.get('father_office_address')
        mother_office_address = request.POST.get('mother_office_address')
        guardian_name = request.POST.get('guardian_name')
        complete_address = request.POST.get('complete_address')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BallbTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.father_first_name = father_first_name   
            existing_record.father_middle_name = father_middle_name
            existing_record.father_last_name = father_last_name
            existing_record.mother_first_name = mother_first_name   
            existing_record.mother_middle_name = mother_middle_name
            existing_record.mother_last_name = mother_last_name
            existing_record.father_qualification = father_qualification
            existing_record.mother_qualification = mother_qualification
            existing_record.father_job = father_job
            existing_record.mother_job = mother_job
            existing_record.father_job_designation = father_job_designation
            existing_record.mother_job_designation = mother_job_designation
            existing_record.father_business_type = father_business_type   
            existing_record.mother_business_type = mother_business_type
            existing_record.father_office_address = father_office_address
            existing_record.mother_office_address = mother_office_address   
            existing_record.father_number = father_number
            existing_record.mother_number = mother_number
            existing_record.guardian_name = guardian_name   
            existing_record.complete_address = complete_address
            # saving the updated record
            existing_record.save()
            return redirect ('ballb3')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BallbTemp(application_id=application_id, ipu_registration=ipu_registration, 
                            father_first_name=father_first_name, father_middle_name=father_middle_name, father_last_name=father_last_name,
                            mother_first_name=mother_first_name, mother_middle_name=mother_middle_name, mother_last_name=mother_last_name,
                            father_qualification=father_qualification, mother_qualification=mother_qualification,
                            father_job=father_job, mother_job=mother_job,
                            father_job_designation=father_job_designation, mother_job_designation=mother_job_designation,
                            father_business_type=father_business_type, mother_business_type=mother_business_type,
                            father_number=father_number, mother_number=mother_number,
                            father_office_address=father_office_address, mother_office_address=mother_office_address,
                            complete_address=complete_address, guardian_name=guardian_name,)
            newform.save()
            return redirect ('ballb3')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of ballb form by clicking the step-form (progress bar)
    # or user is coming from ballb1.html after saving his record
    # in all three cases we can render ballb2.html with context
    # to create context we will use the globally available variable application_id
    record = BallbTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'ballb/ballb2.html', context)

def ballb3(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /ballb3.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        board_12th = request.POST.get('board_12th')
        year_of_12th = request.POST.get('year_of_12th')
        rollno_12th = request.POST.get('rollno_12th')
        school_12th = request.POST.get('school_12th')
        aggregate_12th = float(request.POST.get('aggregate_12th'))
        first_subject_12th = request.POST.get('first_subject_12th')
        second_subject_12th = request.POST.get('second_subject_12th')
        third_subject_12th = request.POST.get('third_subject_12th')
        fourth_subject_12th = request.POST.get('fourth_subject_12th')
        other_subject_12th = request.POST.get('other_subject_12th')
        other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        board_10th = request.POST.get('board_10th')
        year_of_10th = request.POST.get('year_of_10th')
        rollno_10th = request.POST.get('rollno_10th')
        school_10th = request.POST.get('school_10th')
        aggregate_10th = float(request.POST.get('aggregate_10th'))
        maths_10th = request.POST.get('maths_10th')
        science_10th = request.POST.get('science_10th')
        english_10th = request.POST.get('english_10th')
        sst_10th = request.POST.get('sst_10th')
        other_subject_10th = request.POST.get('other_subject_10th')
        other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BallbTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.board_12th = board_12th   
            existing_record.year_of_12th = year_of_12th
            existing_record.rollno_12th = rollno_12th
            existing_record.school_12th = school_12th
            existing_record.aggregate_12th = aggregate_12th
            existing_record.first_subject_12th = first_subject_12th
            existing_record.second_subject_12th = second_subject_12th
            existing_record.third_subject_12th = third_subject_12th
            existing_record.fourth_subject_12th = fourth_subject_12th
            existing_record.other_subject_12th = other_subject_12th
            existing_record.other_subject_2_12th = other_subject_2_12th
            existing_record.board_10th = board_10th   
            existing_record.year_of_10th = year_of_10th
            existing_record.rollno_10th = rollno_10th
            existing_record.school_10th = school_10th
            existing_record.aggregate_10th = aggregate_10th
            existing_record.maths_10th = maths_10th
            existing_record.science_10th = science_10th
            existing_record.english_10th = english_10th
            existing_record.sst_10th = sst_10th
            existing_record.other_subject_10th = other_subject_10th
            existing_record.other_subject_2_10th = other_subject_2_10th
            # saving the updated record
            existing_record.save()
            return redirect ('ballb4')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BallbTemp(application_id=application_id, ipu_registration=ipu_registration,
                            board_12th=board_12th, year_of_12th=year_of_12th, rollno_12th=rollno_12th, school_12th=school_12th,
                            first_subject_12th=first_subject_12th, second_subject_12th=second_subject_12th, third_subject_12th=third_subject_12th, fourth_subject_12th=fourth_subject_12th,
                            other_subject_12th=other_subject_12th, other_subject_2_12th=other_subject_2_12th, aggregate_12th=aggregate_12th, 
                            board_10th=board_10th, year_of_10th=year_of_10th, rollno_10th=rollno_10th, school_10th=school_10th,
                            maths_10th=maths_10th, science_10th=science_10th, english_10th=english_10th, sst_10th=sst_10th,
                            other_subject_10th=other_subject_10th, other_subject_2_10th=other_subject_2_10th, aggregate_10th=aggregate_10th,)
            newform.save()
            return redirect ('ballb4')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of ballb form by clicking the step-form (progress bar)
    # or user is coming from ballb2.html after saving his record
    # in all three cases we can render ballb3.html with context
    # to create context we will use the globally available variable application_id
    record = BallbTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'ballb/ballb3.html', context)

def ballb4(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /ballb4.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        cet_or_cuet = request.POST.get('cet_or_cuet')
        cet_rank = request.POST.get('cet_rank')
        cet_rollno = request.POST.get('cet_rollno')
        special_achievements = request.POST.get('special_achievements')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BallbTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.cet_or_cuet = cet_or_cuet   
            existing_record.cet_rank = cet_rank
            existing_record.cet_rollno = cet_rollno
            existing_record.special_achievements = special_achievements
            # saving the updated record
            existing_record.save()
            return redirect ('ballb5')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BallbTemp(application_id=application_id, ipu_registration=ipu_registration,
                            cet_rank=cet_rank, cet_rollno=cet_rollno, cet_or_cuet=cet_or_cuet,
                            special_achievements=special_achievements,)
            newform.save()
            return redirect ('ballb5')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of ballb form by clicking the step-form (progress bar)
    # or user is coming from ballb3.html after saving his record
    # in all three cases we can render ballb4.html with context
    # to create context we will use the globally available variable application_id
    record = BallbTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'ballb/ballb4.html', context)

def ballb5(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /ballb5.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        passport_photo = request.FILES['passport_photo']
        cet_result = request.FILES['cet_result']
        marksheet_10th = request.FILES['marksheet_10th']
        marksheet_12th = request.FILES['marksheet_12th']
        aadhaar = request.FILES['aadhaar']
        pancard = request.FILES['pancard']
        ipuregistrationproof = request.FILES['ipuregistrationproof']
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BallbTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.passport_photo = passport_photo   
            existing_record.cet_result = cet_result
            existing_record.marksheet_10th = marksheet_10th
            existing_record.marksheet_12th = marksheet_12th
            existing_record.aadhaar = aadhaar
            existing_record.pancard = pancard
            existing_record.ipuregistrationproof = ipuregistrationproof
            # saving the updated record
            existing_record.save()
            # we will only redirect to payments on /ballb6 if all previous steps are filled
            # so to check that, we will check whether some value on each step is filled or not
            if not existing_record.candidate_first_name:
                return redirect('ballb1')
            if not existing_record.father_first_name:
                return redirect('ballb2')
            if not existing_record.board_10th:
                return redirect('ballb3')
            if not existing_record.cet_rollno:
                return redirect('ballb4')
            # if all of these details are filled, then we can safely proceed to payment
            return redirect ('ballb6')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BallbTemp(application_id=application_id, ipu_registration=ipu_registration,
                            passport_photo=passport_photo, cet_result=cet_result, marksheet_10th=marksheet_10th, marksheet_12th=marksheet_12th,
                            aadhaar=aadhaar, pancard=pancard, ipuregistrationproof=ipuregistrationproof)
            newform.save()
            # if its a new record, then we shall not allow to proceed to payment, so we are redirecting to /ballb1
            return redirect ('ballb1')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of ballb form by clicking the step-form (progress bar)
    # or user is coming from ballb4.html after saving his record
    # in all three cases we can render ballb5.html with context
    # to create context we will use the globally available variable application_id
    record = BallbTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'ballb/ballb5.html', context)

def ballb6(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /ballb6.html page
    # so we shall save the data 
    if request.method == "POST" :
        transaction_id = request.POST.get('transaction_id')
        transaction_proof = request.FILES['transaction_proof']
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # (this will never be the case because we are not allowing user to come to /ballb6 if he hasn't already filled previous data , but still handling this case)
        # so, let's check if a record exists or not
        existing_record = BallbTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.transaction_id = transaction_id   
            existing_record.transaction_proof = transaction_proof
            # saving the updated record
            existing_record.save()
            # all steps are completed, now redirecting to final preview where data will move from temp table to permanent table 
            return redirect ('ballb')
        else:
            # saving all fields in a new object
            newform = BallbTemp(application_id=application_id, ipu_registration=ipu_registration,
                            transaction_id=transaction_id, transaction_proof=transaction_proof)
            newform.save()
            return redirect ('ballb')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of ballb form by clicking the step-form (progress bar)
    # or user is coming from ballb5.html after saving his record
    # we shall allow the user only in the case when he has submitted all 5 steps
    record = BallbTemp.objects.all().filter(application_id = application_id).first()
    # so to check that, we will check whether some value on each step is filled or not
    # before that we can check if record exists or not:
    if not record:
        messages.info(request, 'Please fill candidate details before payment')
        return redirect('ballb1')
    if not record.candidate_first_name:
        messages.info(request, 'Please fill candidate details before payment')
        return redirect('ballb1')
    if not record.father_first_name:
        messages.info(request, 'Please fill parent details before payment')
        return redirect('ballb2')
    if not record.board_10th:
        messages.info(request, 'Please fill educational details before payment')
        return redirect('ballb3')
    if not record.cet_rollno:
        messages.info(request, 'Please fill qualifying details before payment')
        return redirect('ballb4')
    if not record.passport_photo:
        messages.info(request, 'Please upload documents before payment')
        return redirect("ballb5")
    # if all of these details are filled, then we can safely render /ballb6.html
    context = {'record': record}
    return render(request, 'ballb/ballb6.html', context)

# ballb
def ballb(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Submit" on the /ballb.html page
    # so we shall save the data in permanent table and delete from temporary table
    if request.method == 'POST':
        transaction_id = request.POST.get('transaction_id')
        # category and region
        category = request.POST.get('category')
        region = request.POST.get('region')
        candidate_first_name = request.POST.get('candidate_first_name')
        candidate_middle_name = request.POST.get('candidate_middle_name')
        candidate_last_name = request.POST.get('candidate_last_name')
        #father mother details
        father_first_name = request.POST.get('father_first_name')
        father_middle_name = request.POST.get('father_middle_name')
        father_last_name = request.POST.get('father_last_name')
        mother_first_name = request.POST.get('mother_first_name')
        mother_middle_name = request.POST.get('mother_middle_name')
        mother_last_name = request.POST.get('mother_last_name')
        father_qualification = request.POST.get('father_qualification')
        mother_qualification = request.POST.get('mother_qualification')
        father_job = request.POST.get('father_job')
        mother_job = request.POST.get('mother_job')
        father_job_designation = request.POST.get('father_job_designation')
        mother_job_designation = request.POST.get('mother_job_designation')
        father_business_type = request.POST.get('father_business_type')
        mother_business_type = request.POST.get('mother_business_type')
        father_number = request.POST.get('father_number')
        mother_number = request.POST.get('mother_number')
        father_office_address = request.POST.get('father_office_address')
        mother_office_address = request.POST.get('mother_office_address')
        #other candidate details
        complete_address = request.POST.get('complete_address')
        email = request.POST.get('email')
        candidate_number = request.POST.get('candidate_number')
        gender = request.POST.get('gender')
        #guardian details
        guardian_name = request.POST.get('guardian_name')
        #candidate dob
        dob = request.POST.get('dob')
        #12th class details
        board_12th = request.POST.get('board_12th')
        year_of_12th = request.POST.get('year_of_12th')
        rollno_12th = request.POST.get('rollno_12th')
        school_12th = request.POST.get('school_12th')
        aggregate_12th = float(request.POST.get('aggregate_12th'))
        first_subject_12th = request.POST.get('first_subject_12th')
        second_subject_12th = request.POST.get('second_subject_12th')
        third_subject_12th = request.POST.get('third_subject_12th')
        fourth_subject_12th = request.POST.get('fourth_subject_12th')
        other_subject_12th = request.POST.get('other_subject_12th')
        other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        #10th class details
        board_10th = request.POST.get('board_10th')
        year_of_10th = request.POST.get('year_of_10th')
        rollno_10th = request.POST.get('rollno_10th')
        school_10th = request.POST.get('school_10th')
        aggregate_10th = float(request.POST.get('aggregate_10th'))
        maths_10th = request.POST.get('maths_10th')
        science_10th = request.POST.get('science_10th')
        english_10th = request.POST.get('english_10th')
        sst_10th = request.POST.get('sst_10th')
        other_subject_10th = request.POST.get('other_subject_10th')
        other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        #CET details
        cet_or_cuet = request.POST.get('cet_or_cuet')
        cet_rank = request.POST.get('cet_rank')
        cet_rollno = request.POST.get('cet_rollno')
        #special acheivements
        special_achievements = request.POST.get('special_achievements')
        # To track IP address and other info of user coming from request.META header
        ip_address = request.META.get('REMOTE_ADDR','-1')      # return -1 if no address found
        forwarded_address = request.META.get('HTTP_X_FORWARDED_FOR','-1')
        browser_info = request.META.get('HTTP_USER_AGENT','-1')
        created_at = str(datetime.datetime.now())[:19]        # only first 19 indexes so that it doesnt store microseconds
        # saving all fields expect files in a new object
        newform = Ballb(candidate_first_name=candidate_first_name, candidate_middle_name=candidate_middle_name, candidate_last_name=candidate_last_name,
                        father_first_name=father_first_name, father_middle_name=father_middle_name, father_last_name=father_last_name,
                        mother_first_name=mother_first_name, mother_middle_name=mother_middle_name, mother_last_name=mother_last_name,
                        father_qualification=father_qualification, mother_qualification=mother_qualification,
                        father_job=father_job, mother_job=mother_job,
                        father_job_designation=father_job_designation, mother_job_designation=mother_job_designation,
                        father_business_type=father_business_type, mother_business_type=mother_business_type,
                        father_number=father_number, mother_number=mother_number,
                        father_office_address=father_office_address, mother_office_address=mother_office_address,
                        complete_address=complete_address, candidate_number=candidate_number,
                        guardian_name=guardian_name, email=email, dob=dob, gender=gender,
                        board_12th=board_12th, year_of_12th=year_of_12th, rollno_12th=rollno_12th, school_12th=school_12th,
                        first_subject_12th=first_subject_12th, second_subject_12th=second_subject_12th, third_subject_12th=third_subject_12th, fourth_subject_12th=fourth_subject_12th,
                        other_subject_12th=other_subject_12th, other_subject_2_12th=other_subject_2_12th, aggregate_12th=aggregate_12th, 
                        board_10th=board_10th, year_of_10th=year_of_10th, rollno_10th=rollno_10th, school_10th=school_10th,
                        maths_10th=maths_10th, science_10th=science_10th, english_10th=english_10th, sst_10th=sst_10th,
                        other_subject_10th=other_subject_10th, other_subject_2_10th=other_subject_2_10th, aggregate_10th=aggregate_10th, 
                        cet_rank=cet_rank, cet_rollno=cet_rollno, cet_or_cuet=cet_or_cuet,
                        ipu_registration=ipu_registration, special_achievements=special_achievements,
                        application_id=application_id, transaction_id=transaction_id,
                        category=category, region=region,
                        ip_address=ip_address, forwarded_address=forwarded_address, browser_info=browser_info, created_at=created_at,)
        newform.save()
        # now saving files after instance is created
        temp_record = BallbTemp.objects.get(application_id=application_id)
        newobj = Ballb.objects.get(pk=newform.pk)
        newobj.passport_photo = temp_record.passport_photo
        newobj.cet_result = temp_record.cet_result
        newobj.marksheet_10th = temp_record.marksheet_10th
        newobj.marksheet_12th = temp_record.marksheet_12th
        newobj.aadhaar = temp_record.aadhaar
        newobj.pancard = temp_record.pancard
        newobj.ipuregistrationproof = temp_record.ipuregistrationproof
        newobj.transaction_proof = temp_record.transaction_proof
        newobj.save()
        temp_record.delete()   # deleting the temporary record
        # At this point, form is submitted successfully
        return redirect('ballb_preview')
    record = BallbTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'ballb/ballb.html', context)
    
# ballb Preview
def ballb_preview(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    record = Ballb.objects.filter(application_id=application_id).first()
    context = {'record': record}
    return render(request, 'ballb/ballb-preview.html', context)

# Edit ballb (after final submission)
def ballb_edit(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save" on the /ballb-edit.html page
    # so we shall save the data in permanent table and delete from temporary table
    if request.method == 'POST':
        record = Ballb.objects.all().filter(application_id = application_id).first()
        record.transaction_id = request.POST.get('transaction_id')
        # category and region
        record.category = request.POST.get('category')
        record.region = request.POST.get('region')
        record.candidate_first_name = request.POST.get('candidate_first_name')
        record.candidate_middle_name = request.POST.get('candidate_middle_name')
        record.candidate_last_name = request.POST.get('candidate_last_name')
        #father mother details
        record.father_first_name = request.POST.get('father_first_name')
        record.father_middle_name = request.POST.get('father_middle_name')
        record.father_last_name = request.POST.get('father_last_name')
        record.mother_first_name = request.POST.get('mother_first_name')
        record.mother_middle_name = request.POST.get('mother_middle_name')
        record.mother_last_name = request.POST.get('mother_last_name')
        record.father_qualification = request.POST.get('father_qualification')
        record.mother_qualification = request.POST.get('mother_qualification')
        record.father_job = request.POST.get('father_job')
        record.mother_job = request.POST.get('mother_job')
        record.father_job_designation = request.POST.get('father_job_designation')
        record.mother_job_designation = request.POST.get('mother_job_designation')
        record.father_business_type = request.POST.get('father_business_type')
        record.mother_business_type = request.POST.get('mother_business_type')
        record.father_number = request.POST.get('father_number')
        record.mother_number = request.POST.get('mother_number')
        record.father_office_address = request.POST.get('father_office_address')
        record.mother_office_address = request.POST.get('mother_office_address')
        #other candidate details
        record.complete_address = request.POST.get('complete_address')
        record.email = request.POST.get('email')
        record.candidate_number = request.POST.get('candidate_number')
        record.gender = request.POST.get('gender')
        #guardian details
        record.guardian_name = request.POST.get('guardian_name')
        #candidate dob
        record.dob = request.POST.get('dob')
        #12th class details
        record.board_12th = request.POST.get('board_12th')
        record.year_of_12th = request.POST.get('year_of_12th')
        record.rollno_12th = request.POST.get('rollno_12th')
        record.school_12th = request.POST.get('school_12th')
        record.aggregate_12th = float(request.POST.get('aggregate_12th'))
        record.first_subject_12th = request.POST.get('first_subject_12th')
        record.second_subject_12th = request.POST.get('second_subject_12th')
        record.third_subject_12th = request.POST.get('third_subject_12th')
        record.fourth_subject_12th = request.POST.get('fourth_subject_12th')
        record.other_subject_12th = request.POST.get('other_subject_12th')
        record.other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        #10th class details
        record.board_10th = request.POST.get('board_10th')
        record.year_of_10th = request.POST.get('year_of_10th')
        record.rollno_10th = request.POST.get('rollno_10th')
        record.school_10th = request.POST.get('school_10th')
        record.aggregate_10th = float(request.POST.get('aggregate_10th'))
        record.maths_10th = request.POST.get('maths_10th')
        record.science_10th = request.POST.get('science_10th')
        record.english_10th = request.POST.get('english_10th')
        record.sst_10th = request.POST.get('sst_10th')
        record.other_subject_10th = request.POST.get('other_subject_10th')
        record.other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        #JEE details
        record.cet_rank = request.POST.get('cet_rank')
        record.cet_or_cuet = request.POST.get('cet_or_cuet')
        record.cet_rollno = request.POST.get('cet_rollno')
        #special acheivements
        record.special_achievements = request.POST.get('special_achievements')
        record.save()
        # At this point, form is submitted successfully
        return redirect('ballb_preview')
    # GET request: render the filled details
    record = Ballb.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'ballb/ballb-edit.html', context)







def bballb1(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bballb1.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        candidate_first_name = request.POST.get('candidate_first_name')
        candidate_middle_name = request.POST.get('candidate_middle_name')
        candidate_last_name = request.POST.get('candidate_last_name')
        email = request.POST.get('email')
        candidate_number = request.POST.get('candidate_number')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        category = request.POST.get('category')
        region = request.POST.get('region')
        # To track IP address and other info of user coming from request.META header
        ip_address = request.META.get('REMOTE_ADDR','-1')      # return -1 if no address found
        forwarded_address = request.META.get('HTTP_X_FORWARDED_FOR','-1')
        browser_info = request.META.get('HTTP_USER_AGENT','-1')
        created_at = str(datetime.datetime.now())[:19]        # only first 19 indexes so that it doesnt store microseconds
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BballbTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.candidate_first_name = candidate_first_name   
            existing_record.candidate_middle_name = candidate_middle_name
            existing_record.candidate_last_name = candidate_last_name
            existing_record.email = email
            existing_record.candidate_number = candidate_number
            existing_record.gender = gender
            existing_record.dob = dob
            existing_record.category = category
            existing_record.region = region
            existing_record.ip_address = ip_address
            existing_record.forwarded_address = forwarded_address
            existing_record.browser_info = browser_info
            existing_record.created_at = created_at
            # saving the updated record
            existing_record.save()
            return redirect ('bballb2')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BballbTemp(application_id=application_id, ipu_registration=ipu_registration,
                            candidate_first_name=candidate_first_name,
                            candidate_middle_name=candidate_middle_name, candidate_last_name=candidate_last_name,
                            email=email, candidate_number=candidate_number, gender=gender, dob=dob, category=category, region=region,
                            ip_address=ip_address, forwarded_address=forwarded_address, browser_info=browser_info, created_at=created_at,)
            newform.save()
            return redirect ('bballb2')
    # if the request method is not POST, then:
    # either user is coming from login page for the very first time
    # or user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bballb form by clicking the step-form (progress bar)
    # in all three cases we can render bballb1.html with context
    # to create context we will use the globally available variable application_id
    record = BballbTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bballb/bballb1.html', context)

def bballb2(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bballb2.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        father_first_name = request.POST.get('father_first_name')
        father_middle_name = request.POST.get('father_middle_name')
        father_last_name = request.POST.get('father_last_name')
        mother_first_name = request.POST.get('mother_first_name')
        mother_middle_name = request.POST.get('mother_middle_name')
        mother_last_name = request.POST.get('mother_last_name')
        father_qualification = request.POST.get('father_qualification')
        mother_qualification = request.POST.get('mother_qualification')
        father_job = request.POST.get('father_job')
        mother_job = request.POST.get('mother_job')
        father_job_designation = request.POST.get('father_job_designation')
        mother_job_designation = request.POST.get('mother_job_designation')
        father_business_type = request.POST.get('father_business_type')
        mother_business_type = request.POST.get('mother_business_type')
        father_number = request.POST.get('father_number')
        mother_number = request.POST.get('mother_number')
        father_office_address = request.POST.get('father_office_address')
        mother_office_address = request.POST.get('mother_office_address')
        guardian_name = request.POST.get('guardian_name')
        complete_address = request.POST.get('complete_address')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BballbTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.father_first_name = father_first_name   
            existing_record.father_middle_name = father_middle_name
            existing_record.father_last_name = father_last_name
            existing_record.mother_first_name = mother_first_name   
            existing_record.mother_middle_name = mother_middle_name
            existing_record.mother_last_name = mother_last_name
            existing_record.father_qualification = father_qualification
            existing_record.mother_qualification = mother_qualification
            existing_record.father_job = father_job
            existing_record.mother_job = mother_job
            existing_record.father_job_designation = father_job_designation
            existing_record.mother_job_designation = mother_job_designation
            existing_record.father_business_type = father_business_type   
            existing_record.mother_business_type = mother_business_type
            existing_record.father_office_address = father_office_address
            existing_record.mother_office_address = mother_office_address   
            existing_record.father_number = father_number
            existing_record.mother_number = mother_number
            existing_record.guardian_name = guardian_name   
            existing_record.complete_address = complete_address
            # saving the updated record
            existing_record.save()
            return redirect ('bballb3')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BballbTemp(application_id=application_id, ipu_registration=ipu_registration, 
                            father_first_name=father_first_name, father_middle_name=father_middle_name, father_last_name=father_last_name,
                            mother_first_name=mother_first_name, mother_middle_name=mother_middle_name, mother_last_name=mother_last_name,
                            father_qualification=father_qualification, mother_qualification=mother_qualification,
                            father_job=father_job, mother_job=mother_job,
                            father_job_designation=father_job_designation, mother_job_designation=mother_job_designation,
                            father_business_type=father_business_type, mother_business_type=mother_business_type,
                            father_number=father_number, mother_number=mother_number,
                            father_office_address=father_office_address, mother_office_address=mother_office_address,
                            complete_address=complete_address, guardian_name=guardian_name,)
            newform.save()
            return redirect ('bballb3')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bballb form by clicking the step-form (progress bar)
    # or user is coming from bballb1.html after saving his record
    # in all three cases we can render bballb2.html with context
    # to create context we will use the globally available variable application_id
    record = BballbTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bballb/bballb2.html', context)

def bballb3(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bballb3.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        board_12th = request.POST.get('board_12th')
        year_of_12th = request.POST.get('year_of_12th')
        rollno_12th = request.POST.get('rollno_12th')
        school_12th = request.POST.get('school_12th')
        aggregate_12th = float(request.POST.get('aggregate_12th'))
        first_subject_12th = request.POST.get('first_subject_12th')
        second_subject_12th = request.POST.get('second_subject_12th')
        third_subject_12th = request.POST.get('third_subject_12th')
        fourth_subject_12th = request.POST.get('fourth_subject_12th')
        other_subject_12th = request.POST.get('other_subject_12th')
        other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        board_10th = request.POST.get('board_10th')
        year_of_10th = request.POST.get('year_of_10th')
        rollno_10th = request.POST.get('rollno_10th')
        school_10th = request.POST.get('school_10th')
        aggregate_10th = float(request.POST.get('aggregate_10th'))
        maths_10th = request.POST.get('maths_10th')
        science_10th = request.POST.get('science_10th')
        english_10th = request.POST.get('english_10th')
        sst_10th = request.POST.get('sst_10th')
        other_subject_10th = request.POST.get('other_subject_10th')
        other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BballbTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.board_12th = board_12th   
            existing_record.year_of_12th = year_of_12th
            existing_record.rollno_12th = rollno_12th
            existing_record.school_12th = school_12th
            existing_record.aggregate_12th = aggregate_12th
            existing_record.first_subject_12th = first_subject_12th
            existing_record.second_subject_12th = second_subject_12th
            existing_record.third_subject_12th = third_subject_12th
            existing_record.fourth_subject_12th = fourth_subject_12th
            existing_record.other_subject_12th = other_subject_12th
            existing_record.other_subject_2_12th = other_subject_2_12th
            existing_record.board_10th = board_10th   
            existing_record.year_of_10th = year_of_10th
            existing_record.rollno_10th = rollno_10th
            existing_record.school_10th = school_10th
            existing_record.aggregate_10th = aggregate_10th
            existing_record.maths_10th = maths_10th
            existing_record.science_10th = science_10th
            existing_record.english_10th = english_10th
            existing_record.sst_10th = sst_10th
            existing_record.other_subject_10th = other_subject_10th
            existing_record.other_subject_2_10th = other_subject_2_10th
            # saving the updated record
            existing_record.save()
            return redirect ('bballb4')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BballbTemp(application_id=application_id, ipu_registration=ipu_registration,
                            board_12th=board_12th, year_of_12th=year_of_12th, rollno_12th=rollno_12th, school_12th=school_12th,
                            first_subject_12th=first_subject_12th, second_subject_12th=second_subject_12th, third_subject_12th=third_subject_12th, fourth_subject_12th=fourth_subject_12th,
                            other_subject_12th=other_subject_12th, other_subject_2_12th=other_subject_2_12th, aggregate_12th=aggregate_12th, 
                            board_10th=board_10th, year_of_10th=year_of_10th, rollno_10th=rollno_10th, school_10th=school_10th,
                            maths_10th=maths_10th, science_10th=science_10th, english_10th=english_10th, sst_10th=sst_10th,
                            other_subject_10th=other_subject_10th, other_subject_2_10th=other_subject_2_10th, aggregate_10th=aggregate_10th,)
            newform.save()
            return redirect ('bballb4')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bballb form by clicking the step-form (progress bar)
    # or user is coming from bballb2.html after saving his record
    # in all three cases we can render bballb3.html with context
    # to create context we will use the globally available variable application_id
    record = BballbTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bballb/bballb3.html', context)

def bballb4(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bballb4.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        cet_or_cuet = request.POST.get('cet_or_cuet')
        cet_rank = request.POST.get('cet_rank')
        cet_rollno = request.POST.get('cet_rollno')
        special_achievements = request.POST.get('special_achievements')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BballbTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.cet_or_cuet = cet_or_cuet   
            existing_record.cet_rank = cet_rank
            existing_record.cet_rollno = cet_rollno
            existing_record.special_achievements = special_achievements
            # saving the updated record
            existing_record.save()
            return redirect ('bballb5')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BballbTemp(application_id=application_id, ipu_registration=ipu_registration,
                            cet_rank=cet_rank, cet_rollno=cet_rollno, cet_or_cuet=cet_or_cuet,
                            special_achievements=special_achievements,)
            newform.save()
            return redirect ('bballb5')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bballb form by clicking the step-form (progress bar)
    # or user is coming from bballb3.html after saving his record
    # in all three cases we can render bballb4.html with context
    # to create context we will use the globally available variable application_id
    record = BballbTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bballb/bballb4.html', context)

def bballb5(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bballb5.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        passport_photo = request.FILES['passport_photo']
        cet_result = request.FILES['cet_result']
        marksheet_10th = request.FILES['marksheet_10th']
        marksheet_12th = request.FILES['marksheet_12th']
        aadhaar = request.FILES['aadhaar']
        pancard = request.FILES['pancard']
        ipuregistrationproof = request.FILES['ipuregistrationproof']
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BballbTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.passport_photo = passport_photo   
            existing_record.cet_result = cet_result
            existing_record.marksheet_10th = marksheet_10th
            existing_record.marksheet_12th = marksheet_12th
            existing_record.aadhaar = aadhaar
            existing_record.pancard = pancard
            existing_record.ipuregistrationproof = ipuregistrationproof
            # saving the updated record
            existing_record.save()
            # we will only redirect to payments on /bballb6 if all previous steps are filled
            # so to check that, we will check whether some value on each step is filled or not
            if not existing_record.candidate_first_name:
                return redirect('bballb1')
            if not existing_record.father_first_name:
                return redirect('bballb2')
            if not existing_record.board_10th:
                return redirect('bballb3')
            if not existing_record.cet_rollno:
                return redirect('bballb4')
            # if all of these details are filled, then we can safely proceed to payment
            return redirect ('bballb6')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BballbTemp(application_id=application_id, ipu_registration=ipu_registration,
                            passport_photo=passport_photo, cet_result=cet_result, marksheet_10th=marksheet_10th, marksheet_12th=marksheet_12th,
                            aadhaar=aadhaar, pancard=pancard, ipuregistrationproof=ipuregistrationproof)
            newform.save()
            # if its a new record, then we shall not allow to proceed to payment, so we are redirecting to /bballb1
            return redirect ('bballb1')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bballb form by clicking the step-form (progress bar)
    # or user is coming from bballb4.html after saving his record
    # in all three cases we can render bballb5.html with context
    # to create context we will use the globally available variable application_id
    record = BballbTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bballb/bballb5.html', context)

def bballb6(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bballb6.html page
    # so we shall save the data 
    if request.method == "POST" :
        transaction_id = request.POST.get('transaction_id')
        transaction_proof = request.FILES['transaction_proof']
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # (this will never be the case because we are not allowing user to come to /bballb6 if he hasn't already filled previous data , but still handling this case)
        # so, let's check if a record exists or not
        existing_record = BballbTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.transaction_id = transaction_id   
            existing_record.transaction_proof = transaction_proof
            # saving the updated record
            existing_record.save()
            # all steps are completed, now redirecting to final preview where data will move from temp table to permanent table 
            return redirect ('bballb')
        else:
            # saving all fields in a new object
            newform = BballbTemp(application_id=application_id, ipu_registration=ipu_registration,
                            transaction_id=transaction_id, transaction_proof=transaction_proof)
            newform.save()
            return redirect ('bballb')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bballb form by clicking the step-form (progress bar)
    # or user is coming from bballb5.html after saving his record
    # we shall allow the user only in the case when he has submitted all 5 steps
    record = BballbTemp.objects.all().filter(application_id = application_id).first()
    # so to check that, we will check whether some value on each step is filled or not
    # before that we can check if record exists or not:
    if not record:
        messages.info(request, 'Please fill candidate details before payment')
        return redirect('bballb1')
    if not record.candidate_first_name:
        messages.info(request, 'Please fill candidate details before payment')
        return redirect('bballb1')
    if not record.father_first_name:
        messages.info(request, 'Please fill parent details before payment')
        return redirect('bballb2')
    if not record.board_10th:
        messages.info(request, 'Please fill educational details before payment')
        return redirect('bballb3')
    if not record.cet_rollno:
        messages.info(request, 'Please fill qualifying details before payment')
        return redirect('bballb4')
    if not record.passport_photo:
        messages.info(request, 'Please upload documents before payment')
        return redirect("bballb5")
    # if all of these details are filled, then we can safely render /bballb6.html
    context = {'record': record}
    return render(request, 'bballb/bballb6.html', context)

# Bballb
def bballb(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Submit" on the /bballb.html page
    # so we shall save the data in permanent table and delete from temporary table
    if request.method == 'POST':
        transaction_id = request.POST.get('transaction_id')
        # category and region
        category = request.POST.get('category')
        region = request.POST.get('region')
        candidate_first_name = request.POST.get('candidate_first_name')
        candidate_middle_name = request.POST.get('candidate_middle_name')
        candidate_last_name = request.POST.get('candidate_last_name')
        #father mother details
        father_first_name = request.POST.get('father_first_name')
        father_middle_name = request.POST.get('father_middle_name')
        father_last_name = request.POST.get('father_last_name')
        mother_first_name = request.POST.get('mother_first_name')
        mother_middle_name = request.POST.get('mother_middle_name')
        mother_last_name = request.POST.get('mother_last_name')
        father_qualification = request.POST.get('father_qualification')
        mother_qualification = request.POST.get('mother_qualification')
        father_job = request.POST.get('father_job')
        mother_job = request.POST.get('mother_job')
        father_job_designation = request.POST.get('father_job_designation')
        mother_job_designation = request.POST.get('mother_job_designation')
        father_business_type = request.POST.get('father_business_type')
        mother_business_type = request.POST.get('mother_business_type')
        father_number = request.POST.get('father_number')
        mother_number = request.POST.get('mother_number')
        father_office_address = request.POST.get('father_office_address')
        mother_office_address = request.POST.get('mother_office_address')
        #other candidate details
        complete_address = request.POST.get('complete_address')
        email = request.POST.get('email')
        candidate_number = request.POST.get('candidate_number')
        gender = request.POST.get('gender')
        #guardian details
        guardian_name = request.POST.get('guardian_name')
        #candidate dob
        dob = request.POST.get('dob')
        #12th class details
        board_12th = request.POST.get('board_12th')
        year_of_12th = request.POST.get('year_of_12th')
        rollno_12th = request.POST.get('rollno_12th')
        school_12th = request.POST.get('school_12th')
        aggregate_12th = float(request.POST.get('aggregate_12th'))
        first_subject_12th = request.POST.get('first_subject_12th')
        second_subject_12th = request.POST.get('second_subject_12th')
        third_subject_12th = request.POST.get('third_subject_12th')
        fourth_subject_12th = request.POST.get('fourth_subject_12th')
        other_subject_12th = request.POST.get('other_subject_12th')
        other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        #10th class details
        board_10th = request.POST.get('board_10th')
        year_of_10th = request.POST.get('year_of_10th')
        rollno_10th = request.POST.get('rollno_10th')
        school_10th = request.POST.get('school_10th')
        aggregate_10th = float(request.POST.get('aggregate_10th'))
        maths_10th = request.POST.get('maths_10th')
        science_10th = request.POST.get('science_10th')
        english_10th = request.POST.get('english_10th')
        sst_10th = request.POST.get('sst_10th')
        other_subject_10th = request.POST.get('other_subject_10th')
        other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        #CET details
        cet_or_cuet = request.POST.get('cet_or_cuet')
        cet_rank = request.POST.get('cet_rank')
        cet_rollno = request.POST.get('cet_rollno')
        #special acheivements
        special_achievements = request.POST.get('special_achievements')
        # To track IP address and other info of user coming from request.META header
        ip_address = request.META.get('REMOTE_ADDR','-1')      # return -1 if no address found
        forwarded_address = request.META.get('HTTP_X_FORWARDED_FOR','-1')
        browser_info = request.META.get('HTTP_USER_AGENT','-1')
        created_at = str(datetime.datetime.now())[:19]        # only first 19 indexes so that it doesnt store microseconds
        # saving all fields expect files in a new object
        newform = Bballb(candidate_first_name=candidate_first_name, candidate_middle_name=candidate_middle_name, candidate_last_name=candidate_last_name,
                        father_first_name=father_first_name, father_middle_name=father_middle_name, father_last_name=father_last_name,
                        mother_first_name=mother_first_name, mother_middle_name=mother_middle_name, mother_last_name=mother_last_name,
                        father_qualification=father_qualification, mother_qualification=mother_qualification,
                        father_job=father_job, mother_job=mother_job,
                        father_job_designation=father_job_designation, mother_job_designation=mother_job_designation,
                        father_business_type=father_business_type, mother_business_type=mother_business_type,
                        father_number=father_number, mother_number=mother_number,
                        father_office_address=father_office_address, mother_office_address=mother_office_address,
                        complete_address=complete_address, candidate_number=candidate_number,
                        guardian_name=guardian_name, email=email, dob=dob, gender=gender,
                        board_12th=board_12th, year_of_12th=year_of_12th, rollno_12th=rollno_12th, school_12th=school_12th,
                        first_subject_12th=first_subject_12th, second_subject_12th=second_subject_12th, third_subject_12th=third_subject_12th, fourth_subject_12th=fourth_subject_12th,
                        other_subject_12th=other_subject_12th, other_subject_2_12th=other_subject_2_12th, aggregate_12th=aggregate_12th, 
                        board_10th=board_10th, year_of_10th=year_of_10th, rollno_10th=rollno_10th, school_10th=school_10th,
                        maths_10th=maths_10th, science_10th=science_10th, english_10th=english_10th, sst_10th=sst_10th,
                        other_subject_10th=other_subject_10th, other_subject_2_10th=other_subject_2_10th, aggregate_10th=aggregate_10th, 
                        cet_rank=cet_rank, cet_rollno=cet_rollno, cet_or_cuet=cet_or_cuet,
                        ipu_registration=ipu_registration, special_achievements=special_achievements,
                        application_id=application_id, transaction_id=transaction_id,
                        category=category, region=region,
                        ip_address=ip_address, forwarded_address=forwarded_address, browser_info=browser_info, created_at=created_at,)
        newform.save()
        # now saving files after instance is created
        temp_record = BballbTemp.objects.get(application_id=application_id)
        newobj = Bballb.objects.get(pk=newform.pk)
        newobj.passport_photo = temp_record.passport_photo
        newobj.cet_result = temp_record.cet_result
        newobj.marksheet_10th = temp_record.marksheet_10th
        newobj.marksheet_12th = temp_record.marksheet_12th
        newobj.aadhaar = temp_record.aadhaar
        newobj.pancard = temp_record.pancard
        newobj.ipuregistrationproof = temp_record.ipuregistrationproof
        newobj.transaction_proof = temp_record.transaction_proof
        newobj.save()
        temp_record.delete()   # deleting the temporary record
        # At this point, form is submitted successfully
        return redirect('bballb_preview')
    record = BballbTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bballb/bballb.html', context)
    
# Bballb Preview
def bballb_preview(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    record = Bballb.objects.filter(application_id=application_id).first()
    context = {'record': record}
    return render(request, 'bballb/bballb-preview.html', context)

# Edit Bballb (after final submission)
def bballb_edit(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save" on the /bballb-edit.html page
    # so we shall save the data in permanent table and delete from temporary table
    if request.method == 'POST':
        record = Bballb.objects.all().filter(application_id = application_id).first()
        record.transaction_id = request.POST.get('transaction_id')
        # category and region
        record.category = request.POST.get('category')
        record.region = request.POST.get('region')
        record.candidate_first_name = request.POST.get('candidate_first_name')
        record.candidate_middle_name = request.POST.get('candidate_middle_name')
        record.candidate_last_name = request.POST.get('candidate_last_name')
        #father mother details
        record.father_first_name = request.POST.get('father_first_name')
        record.father_middle_name = request.POST.get('father_middle_name')
        record.father_last_name = request.POST.get('father_last_name')
        record.mother_first_name = request.POST.get('mother_first_name')
        record.mother_middle_name = request.POST.get('mother_middle_name')
        record.mother_last_name = request.POST.get('mother_last_name')
        record.father_qualification = request.POST.get('father_qualification')
        record.mother_qualification = request.POST.get('mother_qualification')
        record.father_job = request.POST.get('father_job')
        record.mother_job = request.POST.get('mother_job')
        record.father_job_designation = request.POST.get('father_job_designation')
        record.mother_job_designation = request.POST.get('mother_job_designation')
        record.father_business_type = request.POST.get('father_business_type')
        record.mother_business_type = request.POST.get('mother_business_type')
        record.father_number = request.POST.get('father_number')
        record.mother_number = request.POST.get('mother_number')
        record.father_office_address = request.POST.get('father_office_address')
        record.mother_office_address = request.POST.get('mother_office_address')
        #other candidate details
        record.complete_address = request.POST.get('complete_address')
        record.email = request.POST.get('email')
        record.candidate_number = request.POST.get('candidate_number')
        record.gender = request.POST.get('gender')
        #guardian details
        record.guardian_name = request.POST.get('guardian_name')
        #candidate dob
        record.dob = request.POST.get('dob')
        #12th class details
        record.board_12th = request.POST.get('board_12th')
        record.year_of_12th = request.POST.get('year_of_12th')
        record.rollno_12th = request.POST.get('rollno_12th')
        record.school_12th = request.POST.get('school_12th')
        record.aggregate_12th = float(request.POST.get('aggregate_12th'))
        record.first_subject_12th = request.POST.get('first_subject_12th')
        record.second_subject_12th = request.POST.get('second_subject_12th')
        record.third_subject_12th = request.POST.get('third_subject_12th')
        record.fourth_subject_12th = request.POST.get('fourth_subject_12th')
        record.other_subject_12th = request.POST.get('other_subject_12th')
        record.other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        #10th class details
        record.board_10th = request.POST.get('board_10th')
        record.year_of_10th = request.POST.get('year_of_10th')
        record.rollno_10th = request.POST.get('rollno_10th')
        record.school_10th = request.POST.get('school_10th')
        record.aggregate_10th = float(request.POST.get('aggregate_10th'))
        record.maths_10th = request.POST.get('maths_10th')
        record.science_10th = request.POST.get('science_10th')
        record.english_10th = request.POST.get('english_10th')
        record.sst_10th = request.POST.get('sst_10th')
        record.other_subject_10th = request.POST.get('other_subject_10th')
        record.other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        #JEE details
        record.cet_rank = request.POST.get('cet_rank')
        record.cet_or_cuet = request.POST.get('cet_or_cuet')
        record.cet_rollno = request.POST.get('cet_rollno')
        #special acheivements
        record.special_achievements = request.POST.get('special_achievements')
        record.save()
        # At this point, form is submitted successfully
        return redirect('bballb_preview')
    # GET request: render the filled details
    record = Bballb.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bballb/bballb-edit.html', context)








def eco1(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /eco1.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        candidate_first_name = request.POST.get('candidate_first_name')
        candidate_middle_name = request.POST.get('candidate_middle_name')
        candidate_last_name = request.POST.get('candidate_last_name')
        email = request.POST.get('email')
        candidate_number = request.POST.get('candidate_number')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        category = request.POST.get('category')
        region = request.POST.get('region')
        # To track IP address and other info of user coming from request.META header
        ip_address = request.META.get('REMOTE_ADDR','-1')      # return -1 if no address found
        forwarded_address = request.META.get('HTTP_X_FORWARDED_FOR','-1')
        browser_info = request.META.get('HTTP_USER_AGENT','-1')
        created_at = str(datetime.datetime.now())[:19]        # only first 19 indexes so that it doesnt store microseconds
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = EcoTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.candidate_first_name = candidate_first_name   
            existing_record.candidate_middle_name = candidate_middle_name
            existing_record.candidate_last_name = candidate_last_name
            existing_record.email = email
            existing_record.candidate_number = candidate_number
            existing_record.gender = gender
            existing_record.dob = dob
            existing_record.category = category
            existing_record.region = region
            existing_record.ip_address = ip_address
            existing_record.forwarded_address = forwarded_address
            existing_record.browser_info = browser_info
            existing_record.created_at = created_at
            # saving the updated record
            existing_record.save()
            return redirect ('eco2')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = EcoTemp(application_id=application_id, ipu_registration=ipu_registration,
                            candidate_first_name=candidate_first_name,
                            candidate_middle_name=candidate_middle_name, candidate_last_name=candidate_last_name,
                            email=email, candidate_number=candidate_number, gender=gender, dob=dob, category=category, region=region,
                            ip_address=ip_address, forwarded_address=forwarded_address, browser_info=browser_info, created_at=created_at,)
            newform.save()
            return redirect ('eco2')
    # if the request method is not POST, then:
    # either user is coming from login page for the very first time
    # or user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of eco form by clicking the step-form (progress bar)
    # in all three cases we can render eco1.html with context
    # to create context we will use the globally available variable application_id
    record = EcoTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'eco/eco1.html', context)

def eco2(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /eco2.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        father_first_name = request.POST.get('father_first_name')
        father_middle_name = request.POST.get('father_middle_name')
        father_last_name = request.POST.get('father_last_name')
        mother_first_name = request.POST.get('mother_first_name')
        mother_middle_name = request.POST.get('mother_middle_name')
        mother_last_name = request.POST.get('mother_last_name')
        father_qualification = request.POST.get('father_qualification')
        mother_qualification = request.POST.get('mother_qualification')
        father_job = request.POST.get('father_job')
        mother_job = request.POST.get('mother_job')
        father_job_designation = request.POST.get('father_job_designation')
        mother_job_designation = request.POST.get('mother_job_designation')
        father_business_type = request.POST.get('father_business_type')
        mother_business_type = request.POST.get('mother_business_type')
        father_number = request.POST.get('father_number')
        mother_number = request.POST.get('mother_number')
        father_office_address = request.POST.get('father_office_address')
        mother_office_address = request.POST.get('mother_office_address')
        guardian_name = request.POST.get('guardian_name')
        complete_address = request.POST.get('complete_address')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = EcoTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.father_first_name = father_first_name   
            existing_record.father_middle_name = father_middle_name
            existing_record.father_last_name = father_last_name
            existing_record.mother_first_name = mother_first_name   
            existing_record.mother_middle_name = mother_middle_name
            existing_record.mother_last_name = mother_last_name
            existing_record.father_qualification = father_qualification
            existing_record.mother_qualification = mother_qualification
            existing_record.father_job = father_job
            existing_record.mother_job = mother_job
            existing_record.father_job_designation = father_job_designation
            existing_record.mother_job_designation = mother_job_designation
            existing_record.father_business_type = father_business_type   
            existing_record.mother_business_type = mother_business_type
            existing_record.father_office_address = father_office_address
            existing_record.mother_office_address = mother_office_address   
            existing_record.father_number = father_number
            existing_record.mother_number = mother_number
            existing_record.guardian_name = guardian_name   
            existing_record.complete_address = complete_address
            # saving the updated record
            existing_record.save()
            return redirect ('eco3')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = EcoTemp(application_id=application_id, ipu_registration=ipu_registration, 
                            father_first_name=father_first_name, father_middle_name=father_middle_name, father_last_name=father_last_name,
                            mother_first_name=mother_first_name, mother_middle_name=mother_middle_name, mother_last_name=mother_last_name,
                            father_qualification=father_qualification, mother_qualification=mother_qualification,
                            father_job=father_job, mother_job=mother_job,
                            father_job_designation=father_job_designation, mother_job_designation=mother_job_designation,
                            father_business_type=father_business_type, mother_business_type=mother_business_type,
                            father_number=father_number, mother_number=mother_number,
                            father_office_address=father_office_address, mother_office_address=mother_office_address,
                            complete_address=complete_address, guardian_name=guardian_name,)
            newform.save()
            return redirect ('eco3')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of eco form by clicking the step-form (progress bar)
    # or user is coming from eco1.html after saving his record
    # in all three cases we can render eco2.html with context
    # to create context we will use the globally available variable application_id
    record = EcoTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'eco/eco2.html', context)

def eco3(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /eco3.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        board_12th = request.POST.get('board_12th')
        year_of_12th = request.POST.get('year_of_12th')
        rollno_12th = request.POST.get('rollno_12th')
        school_12th = request.POST.get('school_12th')
        aggregate_12th = float(request.POST.get('aggregate_12th'))
        first_subject_12th = request.POST.get('first_subject_12th')
        second_subject_12th = request.POST.get('second_subject_12th')
        third_subject_12th = request.POST.get('third_subject_12th')
        fourth_subject_12th = request.POST.get('fourth_subject_12th')
        other_subject_12th = request.POST.get('other_subject_12th')
        other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        board_10th = request.POST.get('board_10th')
        year_of_10th = request.POST.get('year_of_10th')
        rollno_10th = request.POST.get('rollno_10th')
        school_10th = request.POST.get('school_10th')
        aggregate_10th = float(request.POST.get('aggregate_10th'))
        maths_10th = request.POST.get('maths_10th')
        science_10th = request.POST.get('science_10th')
        english_10th = request.POST.get('english_10th')
        sst_10th = request.POST.get('sst_10th')
        other_subject_10th = request.POST.get('other_subject_10th')
        other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = EcoTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.board_12th = board_12th   
            existing_record.year_of_12th = year_of_12th
            existing_record.rollno_12th = rollno_12th
            existing_record.school_12th = school_12th
            existing_record.aggregate_12th = aggregate_12th
            existing_record.first_subject_12th = first_subject_12th
            existing_record.second_subject_12th = second_subject_12th
            existing_record.third_subject_12th = third_subject_12th
            existing_record.fourth_subject_12th = fourth_subject_12th
            existing_record.other_subject_12th = other_subject_12th
            existing_record.other_subject_2_12th = other_subject_2_12th
            existing_record.board_10th = board_10th   
            existing_record.year_of_10th = year_of_10th
            existing_record.rollno_10th = rollno_10th
            existing_record.school_10th = school_10th
            existing_record.aggregate_10th = aggregate_10th
            existing_record.maths_10th = maths_10th
            existing_record.science_10th = science_10th
            existing_record.english_10th = english_10th
            existing_record.sst_10th = sst_10th
            existing_record.other_subject_10th = other_subject_10th
            existing_record.other_subject_2_10th = other_subject_2_10th
            # saving the updated record
            existing_record.save()
            return redirect ('eco4')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = EcoTemp(application_id=application_id, ipu_registration=ipu_registration,
                            board_12th=board_12th, year_of_12th=year_of_12th, rollno_12th=rollno_12th, school_12th=school_12th,
                            first_subject_12th=first_subject_12th, second_subject_12th=second_subject_12th, third_subject_12th=third_subject_12th, fourth_subject_12th=fourth_subject_12th,
                            other_subject_12th=other_subject_12th, other_subject_2_12th=other_subject_2_12th, aggregate_12th=aggregate_12th, 
                            board_10th=board_10th, year_of_10th=year_of_10th, rollno_10th=rollno_10th, school_10th=school_10th,
                            maths_10th=maths_10th, science_10th=science_10th, english_10th=english_10th, sst_10th=sst_10th,
                            other_subject_10th=other_subject_10th, other_subject_2_10th=other_subject_2_10th, aggregate_10th=aggregate_10th,)
            newform.save()
            return redirect ('eco4')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of eco form by clicking the step-form (progress bar)
    # or user is coming from eco2.html after saving his record
    # in all three cases we can render eco3.html with context
    # to create context we will use the globally available variable application_id
    record = EcoTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'eco/eco3.html', context)

def eco4(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /eco4.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        cet_or_cuet = request.POST.get('cet_or_cuet')
        cet_rank = request.POST.get('cet_rank')
        cet_rollno = request.POST.get('cet_rollno')
        special_achievements = request.POST.get('special_achievements')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = EcoTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.cet_or_cuet = cet_or_cuet   
            existing_record.cet_rank = cet_rank
            existing_record.cet_rollno = cet_rollno
            existing_record.special_achievements = special_achievements
            # saving the updated record
            existing_record.save()
            return redirect ('eco5')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = EcoTemp(application_id=application_id, ipu_registration=ipu_registration,
                            cet_rank=cet_rank, cet_rollno=cet_rollno, cet_or_cuet=cet_or_cuet,
                            special_achievements=special_achievements,)
            newform.save()
            return redirect ('eco5')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of eco form by clicking the step-form (progress bar)
    # or user is coming from eco3.html after saving his record
    # in all three cases we can render eco4.html with context
    # to create context we will use the globally available variable application_id
    record = EcoTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'eco/eco4.html', context)

def eco5(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /eco5.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        passport_photo = request.FILES['passport_photo']
        cet_result = request.FILES['cet_result']
        marksheet_10th = request.FILES['marksheet_10th']
        marksheet_12th = request.FILES['marksheet_12th']
        aadhaar = request.FILES['aadhaar']
        pancard = request.FILES['pancard']
        ipuregistrationproof = request.FILES['ipuregistrationproof']
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = EcoTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.passport_photo = passport_photo   
            existing_record.cet_result = cet_result
            existing_record.marksheet_10th = marksheet_10th
            existing_record.marksheet_12th = marksheet_12th
            existing_record.aadhaar = aadhaar
            existing_record.pancard = pancard
            existing_record.ipuregistrationproof = ipuregistrationproof
            # saving the updated record
            existing_record.save()
            # we will only redirect to payments on /eco6 if all previous steps are filled
            # so to check that, we will check whether some value on each step is filled or not
            if not existing_record.candidate_first_name:
                return redirect('eco1')
            if not existing_record.father_first_name:
                return redirect('eco2')
            if not existing_record.board_10th:
                return redirect('eco3')
            if not existing_record.cet_rollno:
                return redirect('eco4')
            # if all of these details are filled, then we can safely proceed to payment
            return redirect ('eco6')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = EcoTemp(application_id=application_id, ipu_registration=ipu_registration,
                            passport_photo=passport_photo, cet_result=cet_result, marksheet_10th=marksheet_10th, marksheet_12th=marksheet_12th,
                            aadhaar=aadhaar, pancard=pancard, ipuregistrationproof=ipuregistrationproof)
            newform.save()
            # if its a new record, then we shall not allow to proceed to payment, so we are redirecting to /eco1
            return redirect ('eco1')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of eco form by clicking the step-form (progress bar)
    # or user is coming from eco4.html after saving his record
    # in all three cases we can render eco5.html with context
    # to create context we will use the globally available variable application_id
    record = EcoTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'eco/eco5.html', context)

def eco6(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /eco6.html page
    # so we shall save the data 
    if request.method == "POST" :
        transaction_id = request.POST.get('transaction_id')
        transaction_proof = request.FILES['transaction_proof']
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # (this will never be the case because we are not allowing user to come to /eco6 if he hasn't already filled previous data , but still handling this case)
        # so, let's check if a record exists or not
        existing_record = EcoTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.transaction_id = transaction_id   
            existing_record.transaction_proof = transaction_proof
            # saving the updated record
            existing_record.save()
            # all steps are completed, now redirecting to final preview where data will move from temp table to permanent table 
            return redirect ('eco')
        else:
            # saving all fields in a new object
            newform = EcoTemp(application_id=application_id, ipu_registration=ipu_registration,
                            transaction_id=transaction_id, transaction_proof=transaction_proof)
            newform.save()
            return redirect ('eco')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of eco form by clicking the step-form (progress bar)
    # or user is coming from eco5.html after saving his record
    # we shall allow the user only in the case when he has submitted all 5 steps
    record = EcoTemp.objects.all().filter(application_id = application_id).first()
    # so to check that, we will check whether some value on each step is filled or not
    # before that we can check if record exists or not:
    if not record:
        messages.info(request, 'Please fill candidate details before payment')
        return redirect('eco1')
    if not record.candidate_first_name:
        messages.info(request, 'Please fill candidate details before payment')
        return redirect('eco1')
    if not record.father_first_name:
        messages.info(request, 'Please fill parent details before payment')
        return redirect('eco2')
    if not record.board_10th:
        messages.info(request, 'Please fill educational details before payment')
        return redirect('eco3')
    if not record.cet_rollno:
        messages.info(request, 'Please fill qualifying details before payment')
        return redirect('eco4')
    if not record.passport_photo:
        messages.info(request, 'Please upload documents before payment')
        return redirect("eco5")
    # if all of these details are filled, then we can safely render /eco6.html
    context = {'record': record}
    return render(request, 'eco/eco6.html', context)

# Eco
def eco(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Submit" on the /eco.html page
    # so we shall save the data in permanent table and delete from temporary table
    if request.method == 'POST':
        transaction_id = request.POST.get('transaction_id')
        # category and region
        category = request.POST.get('category')
        region = request.POST.get('region')
        candidate_first_name = request.POST.get('candidate_first_name')
        candidate_middle_name = request.POST.get('candidate_middle_name')
        candidate_last_name = request.POST.get('candidate_last_name')
        #father mother details
        father_first_name = request.POST.get('father_first_name')
        father_middle_name = request.POST.get('father_middle_name')
        father_last_name = request.POST.get('father_last_name')
        mother_first_name = request.POST.get('mother_first_name')
        mother_middle_name = request.POST.get('mother_middle_name')
        mother_last_name = request.POST.get('mother_last_name')
        father_qualification = request.POST.get('father_qualification')
        mother_qualification = request.POST.get('mother_qualification')
        father_job = request.POST.get('father_job')
        mother_job = request.POST.get('mother_job')
        father_job_designation = request.POST.get('father_job_designation')
        mother_job_designation = request.POST.get('mother_job_designation')
        father_business_type = request.POST.get('father_business_type')
        mother_business_type = request.POST.get('mother_business_type')
        father_number = request.POST.get('father_number')
        mother_number = request.POST.get('mother_number')
        father_office_address = request.POST.get('father_office_address')
        mother_office_address = request.POST.get('mother_office_address')
        #other candidate details
        complete_address = request.POST.get('complete_address')
        email = request.POST.get('email')
        candidate_number = request.POST.get('candidate_number')
        gender = request.POST.get('gender')
        #guardian details
        guardian_name = request.POST.get('guardian_name')
        #candidate dob
        dob = request.POST.get('dob')
        #12th class details
        board_12th = request.POST.get('board_12th')
        year_of_12th = request.POST.get('year_of_12th')
        rollno_12th = request.POST.get('rollno_12th')
        school_12th = request.POST.get('school_12th')
        aggregate_12th = float(request.POST.get('aggregate_12th'))
        first_subject_12th = request.POST.get('first_subject_12th')
        second_subject_12th = request.POST.get('second_subject_12th')
        third_subject_12th = request.POST.get('third_subject_12th')
        fourth_subject_12th = request.POST.get('fourth_subject_12th')
        other_subject_12th = request.POST.get('other_subject_12th')
        other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        #10th class details
        board_10th = request.POST.get('board_10th')
        year_of_10th = request.POST.get('year_of_10th')
        rollno_10th = request.POST.get('rollno_10th')
        school_10th = request.POST.get('school_10th')
        aggregate_10th = float(request.POST.get('aggregate_10th'))
        maths_10th = request.POST.get('maths_10th')
        science_10th = request.POST.get('science_10th')
        english_10th = request.POST.get('english_10th')
        sst_10th = request.POST.get('sst_10th')
        other_subject_10th = request.POST.get('other_subject_10th')
        other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        #CET details
        cet_or_cuet = request.POST.get('cet_or_cuet')
        cet_rank = request.POST.get('cet_rank')
        cet_rollno = request.POST.get('cet_rollno')
        #special acheivements
        special_achievements = request.POST.get('special_achievements')
        # To track IP address and other info of user coming from request.META header
        ip_address = request.META.get('REMOTE_ADDR','-1')      # return -1 if no address found
        forwarded_address = request.META.get('HTTP_X_FORWARDED_FOR','-1')
        browser_info = request.META.get('HTTP_USER_AGENT','-1')
        created_at = str(datetime.datetime.now())[:19]        # only first 19 indexes so that it doesnt store microseconds
        # saving all fields expect files in a new object
        newform = Eco(candidate_first_name=candidate_first_name, candidate_middle_name=candidate_middle_name, candidate_last_name=candidate_last_name,
                        father_first_name=father_first_name, father_middle_name=father_middle_name, father_last_name=father_last_name,
                        mother_first_name=mother_first_name, mother_middle_name=mother_middle_name, mother_last_name=mother_last_name,
                        father_qualification=father_qualification, mother_qualification=mother_qualification,
                        father_job=father_job, mother_job=mother_job,
                        father_job_designation=father_job_designation, mother_job_designation=mother_job_designation,
                        father_business_type=father_business_type, mother_business_type=mother_business_type,
                        father_number=father_number, mother_number=mother_number,
                        father_office_address=father_office_address, mother_office_address=mother_office_address,
                        complete_address=complete_address, candidate_number=candidate_number,
                        guardian_name=guardian_name, email=email, dob=dob, gender=gender,
                        board_12th=board_12th, year_of_12th=year_of_12th, rollno_12th=rollno_12th, school_12th=school_12th,
                        first_subject_12th=first_subject_12th, second_subject_12th=second_subject_12th, third_subject_12th=third_subject_12th, fourth_subject_12th=fourth_subject_12th,
                        other_subject_12th=other_subject_12th, other_subject_2_12th=other_subject_2_12th, aggregate_12th=aggregate_12th, 
                        board_10th=board_10th, year_of_10th=year_of_10th, rollno_10th=rollno_10th, school_10th=school_10th,
                        maths_10th=maths_10th, science_10th=science_10th, english_10th=english_10th, sst_10th=sst_10th,
                        other_subject_10th=other_subject_10th, other_subject_2_10th=other_subject_2_10th, aggregate_10th=aggregate_10th, 
                        cet_rank=cet_rank, cet_rollno=cet_rollno, cet_or_cuet=cet_or_cuet,
                        ipu_registration=ipu_registration, special_achievements=special_achievements,
                        application_id=application_id, transaction_id=transaction_id,
                        category=category, region=region,
                        ip_address=ip_address, forwarded_address=forwarded_address, browser_info=browser_info, created_at=created_at,)
        newform.save()
        # now saving files after instance is created
        temp_record = EcoTemp.objects.get(application_id=application_id)
        newobj = Eco.objects.get(pk=newform.pk)
        newobj.passport_photo = temp_record.passport_photo
        newobj.cet_result = temp_record.cet_result
        newobj.marksheet_10th = temp_record.marksheet_10th
        newobj.marksheet_12th = temp_record.marksheet_12th
        newobj.aadhaar = temp_record.aadhaar
        newobj.pancard = temp_record.pancard
        newobj.ipuregistrationproof = temp_record.ipuregistrationproof
        newobj.transaction_proof = temp_record.transaction_proof
        newobj.save()
        temp_record.delete()   # deleting the temporary record
        # At this point, form is submitted successfully
        return redirect('eco_preview')
    record = EcoTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'eco/eco.html', context)
    
# Eco Preview
def eco_preview(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    record = Eco.objects.filter(application_id=application_id).first()
    context = {'record': record}
    return render(request, 'eco/eco-preview.html', context)

# Edit Eco (after final submission)
def eco_edit(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save" on the /eco-edit.html page
    # so we shall save the data in permanent table and delete from temporary table
    if request.method == 'POST':
        record = Eco.objects.all().filter(application_id = application_id).first()
        record.transaction_id = request.POST.get('transaction_id')
        # category and region
        record.category = request.POST.get('category')
        record.region = request.POST.get('region')
        record.candidate_first_name = request.POST.get('candidate_first_name')
        record.candidate_middle_name = request.POST.get('candidate_middle_name')
        record.candidate_last_name = request.POST.get('candidate_last_name')
        #father mother details
        record.father_first_name = request.POST.get('father_first_name')
        record.father_middle_name = request.POST.get('father_middle_name')
        record.father_last_name = request.POST.get('father_last_name')
        record.mother_first_name = request.POST.get('mother_first_name')
        record.mother_middle_name = request.POST.get('mother_middle_name')
        record.mother_last_name = request.POST.get('mother_last_name')
        record.father_qualification = request.POST.get('father_qualification')
        record.mother_qualification = request.POST.get('mother_qualification')
        record.father_job = request.POST.get('father_job')
        record.mother_job = request.POST.get('mother_job')
        record.father_job_designation = request.POST.get('father_job_designation')
        record.mother_job_designation = request.POST.get('mother_job_designation')
        record.father_business_type = request.POST.get('father_business_type')
        record.mother_business_type = request.POST.get('mother_business_type')
        record.father_number = request.POST.get('father_number')
        record.mother_number = request.POST.get('mother_number')
        record.father_office_address = request.POST.get('father_office_address')
        record.mother_office_address = request.POST.get('mother_office_address')
        #other candidate details
        record.complete_address = request.POST.get('complete_address')
        record.email = request.POST.get('email')
        record.candidate_number = request.POST.get('candidate_number')
        record.gender = request.POST.get('gender')
        #guardian details
        record.guardian_name = request.POST.get('guardian_name')
        #candidate dob
        record.dob = request.POST.get('dob')
        #12th class details
        record.board_12th = request.POST.get('board_12th')
        record.year_of_12th = request.POST.get('year_of_12th')
        record.rollno_12th = request.POST.get('rollno_12th')
        record.school_12th = request.POST.get('school_12th')
        record.aggregate_12th = float(request.POST.get('aggregate_12th'))
        record.first_subject_12th = request.POST.get('first_subject_12th')
        record.second_subject_12th = request.POST.get('second_subject_12th')
        record.third_subject_12th = request.POST.get('third_subject_12th')
        record.fourth_subject_12th = request.POST.get('fourth_subject_12th')
        record.other_subject_12th = request.POST.get('other_subject_12th')
        record.other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        #10th class details
        record.board_10th = request.POST.get('board_10th')
        record.year_of_10th = request.POST.get('year_of_10th')
        record.rollno_10th = request.POST.get('rollno_10th')
        record.school_10th = request.POST.get('school_10th')
        record.aggregate_10th = float(request.POST.get('aggregate_10th'))
        record.maths_10th = request.POST.get('maths_10th')
        record.science_10th = request.POST.get('science_10th')
        record.english_10th = request.POST.get('english_10th')
        record.sst_10th = request.POST.get('sst_10th')
        record.other_subject_10th = request.POST.get('other_subject_10th')
        record.other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        #JEE details
        record.cet_rank = request.POST.get('cet_rank')
        record.cet_or_cuet = request.POST.get('cet_or_cuet')
        record.cet_rollno = request.POST.get('cet_rollno')
        #special acheivements
        record.special_achievements = request.POST.get('special_achievements')
        record.save()
        # At this point, form is submitted successfully
        return redirect('eco_preview')
    # GET request: render the filled details
    record = Eco.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'eco/eco-edit.html', context)








def llm1(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /llm1.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        candidate_first_name = request.POST.get('candidate_first_name')
        candidate_middle_name = request.POST.get('candidate_middle_name')
        candidate_last_name = request.POST.get('candidate_last_name')
        email = request.POST.get('email')
        candidate_number = request.POST.get('candidate_number')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        category = request.POST.get('category')
        region = request.POST.get('region')
        # To track IP address and other info of user coming from request.META header
        ip_address = request.META.get('REMOTE_ADDR','-1')      # return -1 if no address found
        forwarded_address = request.META.get('HTTP_X_FORWARDED_FOR','-1')
        browser_info = request.META.get('HTTP_USER_AGENT','-1')
        created_at = str(datetime.datetime.now())[:19]        # only first 19 indexes so that it doesnt store microseconds
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = LlmTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.candidate_first_name = candidate_first_name   
            existing_record.candidate_middle_name = candidate_middle_name
            existing_record.candidate_last_name = candidate_last_name
            existing_record.email = email
            existing_record.candidate_number = candidate_number
            existing_record.gender = gender
            existing_record.dob = dob
            existing_record.category = category
            existing_record.region = region
            existing_record.ip_address = ip_address
            existing_record.forwarded_address = forwarded_address
            existing_record.browser_info = browser_info
            existing_record.created_at = created_at
            # saving the updated record
            existing_record.save()
            return redirect ('llm2')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = LlmTemp(application_id=application_id, ipu_registration=ipu_registration,
                            candidate_first_name=candidate_first_name,
                            candidate_middle_name=candidate_middle_name, candidate_last_name=candidate_last_name,
                            email=email, candidate_number=candidate_number, gender=gender, dob=dob, category=category, region=region,
                            ip_address=ip_address, forwarded_address=forwarded_address, browser_info=browser_info, created_at=created_at,)
            newform.save()
            return redirect ('llm2')
    # if the request method is not POST, then:
    # either user is coming from login page for the very first time
    # or user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of llm form by clicking the step-form (progress bar)
    # in all three cases we can render llm1.html with context
    # to create context we will use the globally available variable application_id
    record = LlmTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'llm/llm1.html', context)

def llm2(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /llm2.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        father_first_name = request.POST.get('father_first_name')
        father_middle_name = request.POST.get('father_middle_name')
        father_last_name = request.POST.get('father_last_name')
        mother_first_name = request.POST.get('mother_first_name')
        mother_middle_name = request.POST.get('mother_middle_name')
        mother_last_name = request.POST.get('mother_last_name')
        father_qualification = request.POST.get('father_qualification')
        mother_qualification = request.POST.get('mother_qualification')
        father_job = request.POST.get('father_job')
        mother_job = request.POST.get('mother_job')
        father_job_designation = request.POST.get('father_job_designation')
        mother_job_designation = request.POST.get('mother_job_designation')
        father_business_type = request.POST.get('father_business_type')
        mother_business_type = request.POST.get('mother_business_type')
        father_number = request.POST.get('father_number')
        mother_number = request.POST.get('mother_number')
        father_office_address = request.POST.get('father_office_address')
        mother_office_address = request.POST.get('mother_office_address')
        guardian_name = request.POST.get('guardian_name')
        complete_address = request.POST.get('complete_address')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = LlmTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.father_first_name = father_first_name   
            existing_record.father_middle_name = father_middle_name
            existing_record.father_last_name = father_last_name
            existing_record.mother_first_name = mother_first_name   
            existing_record.mother_middle_name = mother_middle_name
            existing_record.mother_last_name = mother_last_name
            existing_record.father_qualification = father_qualification
            existing_record.mother_qualification = mother_qualification
            existing_record.father_job = father_job
            existing_record.mother_job = mother_job
            existing_record.father_job_designation = father_job_designation
            existing_record.mother_job_designation = mother_job_designation
            existing_record.father_business_type = father_business_type   
            existing_record.mother_business_type = mother_business_type
            existing_record.father_office_address = father_office_address
            existing_record.mother_office_address = mother_office_address   
            existing_record.father_number = father_number
            existing_record.mother_number = mother_number
            existing_record.guardian_name = guardian_name   
            existing_record.complete_address = complete_address
            # saving the updated record
            existing_record.save()
            return redirect ('llm3')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = LlmTemp(application_id=application_id, ipu_registration=ipu_registration, 
                            father_first_name=father_first_name, father_middle_name=father_middle_name, father_last_name=father_last_name,
                            mother_first_name=mother_first_name, mother_middle_name=mother_middle_name, mother_last_name=mother_last_name,
                            father_qualification=father_qualification, mother_qualification=mother_qualification,
                            father_job=father_job, mother_job=mother_job,
                            father_job_designation=father_job_designation, mother_job_designation=mother_job_designation,
                            father_business_type=father_business_type, mother_business_type=mother_business_type,
                            father_number=father_number, mother_number=mother_number,
                            father_office_address=father_office_address, mother_office_address=mother_office_address,
                            complete_address=complete_address, guardian_name=guardian_name,)
            newform.save()
            return redirect ('llm3')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of llm form by clicking the step-form (progress bar)
    # or user is coming from llm1.html after saving his record
    # in all three cases we can render llm2.html with context
    # to create context we will use the globally available variable application_id
    record = LlmTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'llm/llm2.html', context)

def llm3(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /llm3.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        board_12th = request.POST.get('board_12th')
        year_of_12th = request.POST.get('year_of_12th')
        rollno_12th = request.POST.get('rollno_12th')
        school_12th = request.POST.get('school_12th')
        aggregate_12th = float(request.POST.get('aggregate_12th'))
        first_subject_12th = request.POST.get('first_subject_12th')
        second_subject_12th = request.POST.get('second_subject_12th')
        third_subject_12th = request.POST.get('third_subject_12th')
        fourth_subject_12th = request.POST.get('fourth_subject_12th')
        other_subject_12th = request.POST.get('other_subject_12th')
        other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        board_10th = request.POST.get('board_10th')
        year_of_10th = request.POST.get('year_of_10th')
        rollno_10th = request.POST.get('rollno_10th')
        school_10th = request.POST.get('school_10th')
        aggregate_10th = float(request.POST.get('aggregate_10th'))
        maths_10th = request.POST.get('maths_10th')
        science_10th = request.POST.get('science_10th')
        english_10th = request.POST.get('english_10th')
        sst_10th = request.POST.get('sst_10th')
        other_subject_10th = request.POST.get('other_subject_10th')
        other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        ug_type = request.POST.get("ug_type")
        board_ug = request.POST.get("board_ug")
        year_of_ug = request.POST.get("year_of_ug")
        rollno_ug = request.POST.get("rollno_ug")
        school_ug = request.POST.get("school_ug")
        agg_ug = request.POST.get("agg_ug")
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = LlmTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.board_12th = board_12th   
            existing_record.year_of_12th = year_of_12th
            existing_record.rollno_12th = rollno_12th
            existing_record.school_12th = school_12th
            existing_record.aggregate_12th = aggregate_12th
            existing_record.first_subject_12th = first_subject_12th
            existing_record.second_subject_12th = second_subject_12th
            existing_record.third_subject_12th = third_subject_12th
            existing_record.fourth_subject_12th = fourth_subject_12th
            existing_record.other_subject_12th = other_subject_12th
            existing_record.other_subject_2_12th = other_subject_2_12th
            existing_record.board_10th = board_10th   
            existing_record.year_of_10th = year_of_10th
            existing_record.rollno_10th = rollno_10th
            existing_record.school_10th = school_10th
            existing_record.aggregate_10th = aggregate_10th
            existing_record.maths_10th = maths_10th
            existing_record.science_10th = science_10th
            existing_record.english_10th = english_10th
            existing_record.sst_10th = sst_10th
            existing_record.other_subject_10th = other_subject_10th
            existing_record.other_subject_2_10th = other_subject_2_10th
            existing_record.ug_type = ug_type
            existing_record.board_ug = board_ug
            existing_record.year_of_ug = year_of_ug
            existing_record.rollno_ug = rollno_ug
            existing_record.school_ug = school_ug
            existing_record.aggregate_ug = agg_ug
            # saving the updated record
            existing_record.save()
            return redirect ('llm4')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = LlmTemp(application_id=application_id, ipu_registration=ipu_registration,
                            board_12th=board_12th, year_of_12th=year_of_12th, rollno_12th=rollno_12th, school_12th=school_12th,
                            first_subject_12th=first_subject_12th, second_subject_12th=second_subject_12th, third_subject_12th=third_subject_12th, fourth_subject_12th=fourth_subject_12th,
                            other_subject_12th=other_subject_12th, other_subject_2_12th=other_subject_2_12th, aggregate_12th=aggregate_12th, 
                            board_10th=board_10th, year_of_10th=year_of_10th, rollno_10th=rollno_10th, school_10th=school_10th,
                            maths_10th=maths_10th, science_10th=science_10th, english_10th=english_10th, sst_10th=sst_10th,
                            other_subject_10th=other_subject_10th, other_subject_2_10th=other_subject_2_10th, aggregate_10th=aggregate_10th,
                            ug_type=ug_type, board_ug=board_ug, year_of_ug=year_of_ug, rollno_ug=rollno_ug, school_ug=school_ug, aggregate_ug=agg_ug,)
            newform.save()
            return redirect ('llm4')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of llm form by clicking the step-form (progress bar)
    # or user is coming from llm2.html after saving his record
    # in all three cases we can render llm3.html with context
    # to create context we will use the globally available variable application_id
    record = LlmTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'llm/llm3.html', context)

def llm4(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /llm4.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        cet_rank = request.POST.get('cet_rank')
        cet_rollno = request.POST.get('cet_rollno')
        special_achievements = request.POST.get('special_achievements')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = LlmTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields  
            existing_record.cet_rank = cet_rank
            existing_record.cet_rollno = cet_rollno
            existing_record.special_achievements = special_achievements
            # saving the updated record
            existing_record.save()
            return redirect ('llm5')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = LlmTemp(application_id=application_id, ipu_registration=ipu_registration,
                            cet_rank=cet_rank, cet_rollno=cet_rollno,
                            special_achievements=special_achievements,)
            newform.save()
            return redirect ('llm5')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of llm form by clicking the step-form (progress bar)
    # or user is coming from llm3.html after saving his record
    # in all three cases we can render llm4.html with context
    # to create context we will use the globally available variable application_id
    record = LlmTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'llm/llm4.html', context)

def llm5(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /llm5.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        passport_photo = request.FILES['passport_photo']
        cet_result = request.FILES['cet_result']
        marksheet_10th = request.FILES['marksheet_10th']
        marksheet_12th = request.FILES['marksheet_12th']
        aadhaar = request.FILES['aadhaar']
        pancard = request.FILES['pancard']
        ipuregistrationproof = request.FILES['ipuregistrationproof']
        ug_degree = request.FILES['ug_degree']
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = LlmTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.passport_photo = passport_photo   
            existing_record.cet_result = cet_result
            existing_record.marksheet_10th = marksheet_10th
            existing_record.marksheet_12th = marksheet_12th
            existing_record.aadhaar = aadhaar
            existing_record.pancard = pancard
            existing_record.ipuregistrationproof = ipuregistrationproof
            existing_record.ug_degree = ug_degree
            # saving the updated record
            existing_record.save()
            # we will only redirect to payments on /llm6 if all previous steps are filled
            # so to check that, we will check whether some value on each step is filled or not
            if not existing_record.candidate_first_name:
                return redirect('llm1')
            if not existing_record.father_first_name:
                return redirect('llm2')
            if not existing_record.board_10th:
                return redirect('llm3')
            if not existing_record.cet_rollno:
                return redirect('llm4')
            # if all of these details are filled, then we can safely proceed to payment
            return redirect ('llm6')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = LlmTemp(application_id=application_id, ipu_registration=ipu_registration,
                            passport_photo=passport_photo, cet_result=cet_result, marksheet_10th=marksheet_10th, marksheet_12th=marksheet_12th,
                            aadhaar=aadhaar, pancard=pancard, ipuregistrationproof=ipuregistrationproof, ug_degree=ug_degree,)
            newform.save()
            # if its a new record, then we shall not allow to proceed to payment, so we are redirecting to /llm1
            return redirect ('llm1')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of llm form by clicking the step-form (progress bar)
    # or user is coming from llm4.html after saving his record
    # in all three cases we can render llm5.html with context
    # to create context we will use the globally available variable application_id
    record = LlmTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'llm/llm5.html', context)

def llm6(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /llm6.html page
    # so we shall save the data 
    if request.method == "POST" :
        transaction_id = request.POST.get('transaction_id')
        transaction_proof = request.FILES['transaction_proof']
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # (this will never be the case because we are not allowing user to come to /llm6 if he hasn't already filled previous data , but still handling this case)
        # so, let's check if a record exists or not
        existing_record = LlmTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.transaction_id = transaction_id   
            existing_record.transaction_proof = transaction_proof
            # saving the updated record
            existing_record.save()
            # all steps are completed, now redirecting to final preview where data will move from temp table to permanent table 
            return redirect ('llm')
        else:
            # saving all fields in a new object
            newform = LlmTemp(application_id=application_id, ipu_registration=ipu_registration,
                            transaction_id=transaction_id, transaction_proof=transaction_proof)
            newform.save()
            return redirect ('llm')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of llm form by clicking the step-form (progress bar)
    # or user is coming from llm5.html after saving his record
    # we shall allow the user only in the case when he has submitted all 5 steps
    record = LlmTemp.objects.all().filter(application_id = application_id).first()
    # so to check that, we will check whether some value on each step is filled or not
    # before that we can check if record exists or not:
    if not record:
        messages.info(request, 'Please fill candidate details before payment')
        return redirect('llm1')
    if not record.candidate_first_name:
        messages.info(request, 'Please fill candidate details before payment')
        return redirect('llm1')
    if not record.father_first_name:
        messages.info(request, 'Please fill parent details before payment')
        return redirect('llm2')
    if not record.board_10th:
        messages.info(request, 'Please fill educational details before payment')
        return redirect('llm3')
    if not record.cet_rollno:
        messages.info(request, 'Please fill qualifying details before payment')
        return redirect('llm4')
    if not record.passport_photo:
        messages.info(request, 'Please upload documents before payment')
        return redirect("llm5")
    # if all of these details are filled, then we can safely render /llm6.html
    context = {'record': record}
    return render(request, 'llm/llm6.html', context)

# Llm
def llm(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Submit" on the /llm.html page
    # so we shall save the data in permanent table and delete from temporary table
    if request.method == 'POST':
        transaction_id = request.POST.get('transaction_id')
        # category and region
        category = request.POST.get('category')
        region = request.POST.get('region')
        candidate_first_name = request.POST.get('candidate_first_name')
        candidate_middle_name = request.POST.get('candidate_middle_name')
        candidate_last_name = request.POST.get('candidate_last_name')
        #father mother details
        father_first_name = request.POST.get('father_first_name')
        father_middle_name = request.POST.get('father_middle_name')
        father_last_name = request.POST.get('father_last_name')
        mother_first_name = request.POST.get('mother_first_name')
        mother_middle_name = request.POST.get('mother_middle_name')
        mother_last_name = request.POST.get('mother_last_name')
        father_qualification = request.POST.get('father_qualification')
        mother_qualification = request.POST.get('mother_qualification')
        father_job = request.POST.get('father_job')
        mother_job = request.POST.get('mother_job')
        father_job_designation = request.POST.get('father_job_designation')
        mother_job_designation = request.POST.get('mother_job_designation')
        father_business_type = request.POST.get('father_business_type')
        mother_business_type = request.POST.get('mother_business_type')
        father_number = request.POST.get('father_number')
        mother_number = request.POST.get('mother_number')
        father_office_address = request.POST.get('father_office_address')
        mother_office_address = request.POST.get('mother_office_address')
        #other candidate details
        complete_address = request.POST.get('complete_address')
        email = request.POST.get('email')
        candidate_number = request.POST.get('candidate_number')
        gender = request.POST.get('gender')
        #guardian details
        guardian_name = request.POST.get('guardian_name')
        #candidate dob
        dob = request.POST.get('dob')
        #12th class details
        board_12th = request.POST.get('board_12th')
        year_of_12th = request.POST.get('year_of_12th')
        rollno_12th = request.POST.get('rollno_12th')
        school_12th = request.POST.get('school_12th')
        aggregate_12th = float(request.POST.get('aggregate_12th'))
        first_subject_12th = request.POST.get('first_subject_12th')
        second_subject_12th = request.POST.get('second_subject_12th')
        third_subject_12th = request.POST.get('third_subject_12th')
        fourth_subject_12th = request.POST.get('fourth_subject_12th')
        other_subject_12th = request.POST.get('other_subject_12th')
        other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        #10th class details
        board_10th = request.POST.get('board_10th')
        year_of_10th = request.POST.get('year_of_10th')
        rollno_10th = request.POST.get('rollno_10th')
        school_10th = request.POST.get('school_10th')
        aggregate_10th = float(request.POST.get('aggregate_10th'))
        maths_10th = request.POST.get('maths_10th')
        science_10th = request.POST.get('science_10th')
        english_10th = request.POST.get('english_10th')
        sst_10th = request.POST.get('sst_10th')
        other_subject_10th = request.POST.get('other_subject_10th')
        other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        #ug details
        ug_type = request.POST.get("ug_type")
        board_ug = request.POST.get("board_ug")
        year_of_ug = request.POST.get("year_of_ug")
        rollno_ug = request.POST.get("rollno_ug")
        school_ug = request.POST.get("school_ug")
        agg_ug = request.POST.get("agg_ug")
        #CET details
        cet_rank = request.POST.get('cet_rank')
        cet_rollno = request.POST.get('cet_rollno')
        #special acheivements
        special_achievements = request.POST.get('special_achievements')
        # To track IP address and other info of user coming from request.META header
        ip_address = request.META.get('REMOTE_ADDR','-1')      # return -1 if no address found
        forwarded_address = request.META.get('HTTP_X_FORWARDED_FOR','-1')
        browser_info = request.META.get('HTTP_USER_AGENT','-1')
        created_at = str(datetime.datetime.now())[:19]        # only first 19 indexes so that it doesnt store microseconds
        # saving all fields expect files in a new object
        newform = Llm(candidate_first_name=candidate_first_name, candidate_middle_name=candidate_middle_name, candidate_last_name=candidate_last_name,
                        father_first_name=father_first_name, father_middle_name=father_middle_name, father_last_name=father_last_name,
                        mother_first_name=mother_first_name, mother_middle_name=mother_middle_name, mother_last_name=mother_last_name,
                        father_qualification=father_qualification, mother_qualification=mother_qualification,
                        father_job=father_job, mother_job=mother_job,
                        father_job_designation=father_job_designation, mother_job_designation=mother_job_designation,
                        father_business_type=father_business_type, mother_business_type=mother_business_type,
                        father_number=father_number, mother_number=mother_number,
                        father_office_address=father_office_address, mother_office_address=mother_office_address,
                        complete_address=complete_address, candidate_number=candidate_number,
                        guardian_name=guardian_name, email=email, dob=dob, gender=gender,
                        board_12th=board_12th, year_of_12th=year_of_12th, rollno_12th=rollno_12th, school_12th=school_12th,
                        first_subject_12th=first_subject_12th, second_subject_12th=second_subject_12th, third_subject_12th=third_subject_12th, fourth_subject_12th=fourth_subject_12th,
                        other_subject_12th=other_subject_12th, other_subject_2_12th=other_subject_2_12th, aggregate_12th=aggregate_12th, 
                        board_10th=board_10th, year_of_10th=year_of_10th, rollno_10th=rollno_10th, school_10th=school_10th,
                        maths_10th=maths_10th, science_10th=science_10th, english_10th=english_10th, sst_10th=sst_10th,
                        other_subject_10th=other_subject_10th, other_subject_2_10th=other_subject_2_10th, aggregate_10th=aggregate_10th, 
                        cet_rank=cet_rank, cet_rollno=cet_rollno, 
                        ug_type=ug_type, board_ug=board_ug, year_of_ug=year_of_ug, rollno_ug=rollno_ug, school_ug=school_ug, aggregate_ug=agg_ug,
                        ipu_registration=ipu_registration, special_achievements=special_achievements,
                        application_id=application_id, transaction_id=transaction_id,
                        category=category, region=region,
                        ip_address=ip_address, forwarded_address=forwarded_address, browser_info=browser_info, created_at=created_at,)
        newform.save()
        # now saving files after instance is created
        temp_record = LlmTemp.objects.get(application_id=application_id)
        newobj = Llm.objects.get(pk=newform.pk)
        newobj.passport_photo = temp_record.passport_photo
        newobj.cet_result = temp_record.cet_result
        newobj.marksheet_10th = temp_record.marksheet_10th
        newobj.marksheet_12th = temp_record.marksheet_12th
        newobj.aadhaar = temp_record.aadhaar
        newobj.pancard = temp_record.pancard
        newobj.ipuregistrationproof = temp_record.ipuregistrationproof
        newobj.transaction_proof = temp_record.transaction_proof
        newobj.ug_degree = temp_record.ug_degree
        newobj.save()
        temp_record.delete()   # deleting the temporary record
        # At this point, form is submitted successfully
        return redirect('llm_preview')
    record = LlmTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'llm/llm.html', context)
    
# Llm Preview
def llm_preview(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    record = Llm.objects.filter(application_id=application_id).first()
    context = {'record': record}
    return render(request, 'llm/llm-preview.html', context)

# Edit Llm (after final submission)
def llm_edit(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save" on the /llm-edit.html page
    # so we shall save the data in permanent table and delete from temporary table
    if request.method == 'POST':
        record = Llm.objects.all().filter(application_id = application_id).first()
        record.transaction_id = request.POST.get('transaction_id')
        # category and region
        record.category = request.POST.get('category')
        record.region = request.POST.get('region')
        record.candidate_first_name = request.POST.get('candidate_first_name')
        record.candidate_middle_name = request.POST.get('candidate_middle_name')
        record.candidate_last_name = request.POST.get('candidate_last_name')
        #father mother details
        record.father_first_name = request.POST.get('father_first_name')
        record.father_middle_name = request.POST.get('father_middle_name')
        record.father_last_name = request.POST.get('father_last_name')
        record.mother_first_name = request.POST.get('mother_first_name')
        record.mother_middle_name = request.POST.get('mother_middle_name')
        record.mother_last_name = request.POST.get('mother_last_name')
        record.father_qualification = request.POST.get('father_qualification')
        record.mother_qualification = request.POST.get('mother_qualification')
        record.father_job = request.POST.get('father_job')
        record.mother_job = request.POST.get('mother_job')
        record.father_job_designation = request.POST.get('father_job_designation')
        record.mother_job_designation = request.POST.get('mother_job_designation')
        record.father_business_type = request.POST.get('father_business_type')
        record.mother_business_type = request.POST.get('mother_business_type')
        record.father_number = request.POST.get('father_number')
        record.mother_number = request.POST.get('mother_number')
        record.father_office_address = request.POST.get('father_office_address')
        record.mother_office_address = request.POST.get('mother_office_address')
        #other candidate details
        record.complete_address = request.POST.get('complete_address')
        record.email = request.POST.get('email')
        record.candidate_number = request.POST.get('candidate_number')
        record.gender = request.POST.get('gender')
        #guardian details
        record.guardian_name = request.POST.get('guardian_name')
        #candidate dob
        record.dob = request.POST.get('dob')
        #12th class details
        record.board_12th = request.POST.get('board_12th')
        record.year_of_12th = request.POST.get('year_of_12th')
        record.rollno_12th = request.POST.get('rollno_12th')
        record.school_12th = request.POST.get('school_12th')
        record.aggregate_12th = float(request.POST.get('aggregate_12th'))
        record.first_subject_12th = request.POST.get('first_subject_12th')
        record.second_subject_12th = request.POST.get('second_subject_12th')
        record.third_subject_12th = request.POST.get('third_subject_12th')
        record.fourth_subject_12th = request.POST.get('fourth_subject_12th')
        record.other_subject_12th = request.POST.get('other_subject_12th')
        record.other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        #10th class details
        record.board_10th = request.POST.get('board_10th')
        record.year_of_10th = request.POST.get('year_of_10th')
        record.rollno_10th = request.POST.get('rollno_10th')
        record.school_10th = request.POST.get('school_10th')
        record.aggregate_10th = float(request.POST.get('aggregate_10th'))
        record.maths_10th = request.POST.get('maths_10th')
        record.science_10th = request.POST.get('science_10th')
        record.english_10th = request.POST.get('english_10th')
        record.sst_10th = request.POST.get('sst_10th')
        record.other_subject_10th = request.POST.get('other_subject_10th')
        record.other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        record.ug_type = request.POST.get("ug_type")
        record.board_ug = request.POST.get("board_ug")
        record.year_of_ug = request.POST.get("year_of_ug")
        record.rollno_ug = request.POST.get("rollno_ug")
        record.school_ug = request.POST.get("school_ug")
        record.aggregate_ug = request.POST.get("agg_ug")
        #CET details
        record.cet_rank = request.POST.get('cet_rank')
        record.cet_rollno = request.POST.get('cet_rollno')
        #special acheivements
        record.special_achievements = request.POST.get('special_achievements')
        record.save()
        # At this point, form is submitted successfully
        return redirect('llm_preview')
    # GET request: render the filled details
    record = Llm.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'llm/llm-edit.html', context)



