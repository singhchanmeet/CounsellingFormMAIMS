# This file contains utility functions
# (rename functions for file upload)
# we are renaming everything by ipu_registration because that is unique for every candidate
import os


#BBA rename functions
def bba_photo_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bba/photographs')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bba/photographs', new_name))
        return os.path.join('bba/photographs', new_name)
    else:
        return filename
    
def bba_cetresult_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bba/cetresult')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bba/cetresult', new_name))
        return os.path.join('bba/cetresult', new_name)
    else:
        return filename
    
def bba_10thmarksheet_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bba/marksheet10th')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bba/marksheet10th', new_name))
        return os.path.join('bba/marksheet10th', new_name)
    else:
        return filename    
    
def bba_12thmarksheet_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file
        for each_file in os.listdir(os.path.join('media/bba/marksheet12th')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bba/marksheet12th', new_name))
        return os.path.join('bba/marksheet12th', new_name)
    else:
        return filename
    
def bba_aadhar_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file
        for each_file in os.listdir(os.path.join('media/bba/aadhar')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bba/aadhar', new_name))
        return os.path.join('bba/aadhar', new_name)
    else:
        return filename

def bba_pancard_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bba/pancard')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bba/pancard', new_name))
        return os.path.join('bba/pancard', new_name)
    else:
        return filename
    
def bba_ipuregistration_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bba/ipuregistration')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bba/ipuregistration', new_name))
        return os.path.join('bba/ipuregistration', new_name)
    else:
        return filename

def bba_transaction_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bba/transactions')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bba/transactions', new_name))
        return os.path.join('bba/transactions', new_name)
    else:
        return filename
    
def bba_counselling_transaction_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bba/counselling_transactions')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bba/counselling_transactions', new_name))
        return os.path.join('bba/counselling_transactions', new_name)
    else:
        return filename
    






#Bcom rename functions
def bcom_photo_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bcom/photographs')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bcom/photographs', new_name))
        return os.path.join('bcom/photographs', new_name)
    else:
        return filename
    
def bcom_cetresult_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bcom/cetresult')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bcom/cetresult', new_name))
        return os.path.join('bcom/cetresult', new_name)
    else:
        return filename
    
def bcom_10thmarksheet_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bcom/marksheet10th')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bcom/marksheet10th', new_name))
        return os.path.join('bcom/marksheet10th', new_name)
    else:
        return filename    
    
def bcom_12thmarksheet_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file
        for each_file in os.listdir(os.path.join('media/bcom/marksheet12th')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bcom/marksheet12th', new_name))
        return os.path.join('bcom/marksheet12th', new_name)
    else:
        return filename
    
def bcom_aadhar_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file
        for each_file in os.listdir(os.path.join('media/bcom/aadhar')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bcom/aadhar', new_name))
        return os.path.join('bcom/aadhar', new_name)
    else:
        return filename

def bcom_pancard_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bcom/pancard')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bcom/pancard', new_name))
        return os.path.join('bcom/pancard', new_name)
    else:
        return filename
    
def bcom_ipuregistration_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bcom/ipuregistration')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bcom/ipuregistration', new_name))
        return os.path.join('bcom/ipuregistration', new_name)
    else:
        return filename

def bcom_transaction_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bcom/transactions')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bcom/transactions', new_name))
        return os.path.join('bcom/transactions', new_name)
    else:
        return filename
    
def bcom_counselling_transaction_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bcom/counselling_transactions')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bcom/counselling_transactions', new_name))
        return os.path.join('bcom/counselling_transactions', new_name)
    else:
        return filename
    





#bjmc rename functions
def bjmc_photo_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bjmc/photographs')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bjmc/photographs', new_name))
        return os.path.join('bjmc/photographs', new_name)
    else:
        return filename
    
def bjmc_cetresult_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bjmc/cetresult')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bjmc/cetresult', new_name))
        return os.path.join('bjmc/cetresult', new_name)
    else:
        return filename
    
def bjmc_10thmarksheet_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bjmc/marksheet10th')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bjmc/marksheet10th', new_name))
        return os.path.join('bjmc/marksheet10th', new_name)
    else:
        return filename    
    
def bjmc_12thmarksheet_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file
        for each_file in os.listdir(os.path.join('media/bjmc/marksheet12th')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bjmc/marksheet12th', new_name))
        return os.path.join('bjmc/marksheet12th', new_name)
    else:
        return filename
    
def bjmc_aadhar_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file
        for each_file in os.listdir(os.path.join('media/bjmc/aadhar')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bjmc/aadhar', new_name))
        return os.path.join('bjmc/aadhar', new_name)
    else:
        return filename

def bjmc_pancard_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bjmc/pancard')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bjmc/pancard', new_name))
        return os.path.join('bjmc/pancard', new_name)
    else:
        return filename
    
def bjmc_ipuregistration_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bjmc/ipuregistration')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bjmc/ipuregistration', new_name))
        return os.path.join('bjmc/ipuregistration', new_name)
    else:
        return filename

def bjmc_transaction_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bjmc/transactions')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bjmc/transactions', new_name))
        return os.path.join('bjmc/transactions', new_name)
    else:
        return filename
    
def bjmc_counselling_transaction_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bjmc/counselling_transactions')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bjmc/counselling_transactions', new_name))
        return os.path.join('bjmc/counselling_transactions', new_name)
    else:
        return filename
    





#ballb rename functions
def ballb_photo_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/ballb/photographs')):
            if (each_file == new_name):
                os.remove(os.path.join('media/ballb/photographs', new_name))
        return os.path.join('ballb/photographs', new_name)
    else:
        return filename
    
def ballb_cetresult_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/ballb/cetresult')):
            if (each_file == new_name):
                os.remove(os.path.join('media/ballb/cetresult', new_name))
        return os.path.join('ballb/cetresult', new_name)
    else:
        return filename
    
def ballb_10thmarksheet_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/ballb/marksheet10th')):
            if (each_file == new_name):
                os.remove(os.path.join('media/ballb/marksheet10th', new_name))
        return os.path.join('ballb/marksheet10th', new_name)
    else:
        return filename    
    
def ballb_12thmarksheet_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file
        for each_file in os.listdir(os.path.join('media/ballb/marksheet12th')):
            if (each_file == new_name):
                os.remove(os.path.join('media/ballb/marksheet12th', new_name))
        return os.path.join('ballb/marksheet12th', new_name)
    else:
        return filename
    
def ballb_aadhar_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file
        for each_file in os.listdir(os.path.join('media/ballb/aadhar')):
            if (each_file == new_name):
                os.remove(os.path.join('media/ballb/aadhar', new_name))
        return os.path.join('ballb/aadhar', new_name)
    else:
        return filename

def ballb_pancard_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/ballb/pancard')):
            if (each_file == new_name):
                os.remove(os.path.join('media/ballb/pancard', new_name))
        return os.path.join('ballb/pancard', new_name)
    else:
        return filename
    
def ballb_ipuregistration_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/ballb/ipuregistration')):
            if (each_file == new_name):
                os.remove(os.path.join('media/ballb/ipuregistration', new_name))
        return os.path.join('ballb/ipuregistration', new_name)
    else:
        return filename

def ballb_transaction_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/ballb/transactions')):
            if (each_file == new_name):
                os.remove(os.path.join('media/ballb/transactions', new_name))
        return os.path.join('ballb/transactions', new_name)
    else:
        return filename
    
def ballb_counselling_transaction_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/ballb/counselling_transactions')):
            if (each_file == new_name):
                os.remove(os.path.join('media/ballb/counselling_transactions', new_name))
        return os.path.join('ballb/counselling_transactions', new_name)
    else:
        return filename
    





#bballb rename functions
def bballb_photo_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bballb/photographs')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bballb/photographs', new_name))
        return os.path.join('bballb/photographs', new_name)
    else:
        return filename
    
def bballb_cetresult_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bballb/cetresult')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bballb/cetresult', new_name))
        return os.path.join('bballb/cetresult', new_name)
    else:
        return filename
    
def bballb_10thmarksheet_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bballb/marksheet10th')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bballb/marksheet10th', new_name))
        return os.path.join('bballb/marksheet10th', new_name)
    else:
        return filename    
    
def bballb_12thmarksheet_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file
        for each_file in os.listdir(os.path.join('media/bballb/marksheet12th')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bballb/marksheet12th', new_name))
        return os.path.join('bballb/marksheet12th', new_name)
    else:
        return filename
    
def bballb_aadhar_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file
        for each_file in os.listdir(os.path.join('media/bballb/aadhar')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bballb/aadhar', new_name))
        return os.path.join('bballb/aadhar', new_name)
    else:
        return filename

def bballb_pancard_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bballb/pancard')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bballb/pancard', new_name))
        return os.path.join('bballb/pancard', new_name)
    else:
        return filename
    
def bballb_ipuregistration_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bballb/ipuregistration')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bballb/ipuregistration', new_name))
        return os.path.join('bballb/ipuregistration', new_name)
    else:
        return filename

def bballb_transaction_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bballb/transactions')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bballb/transactions', new_name))
        return os.path.join('bballb/transactions', new_name)
    else:
        return filename
    
def bballb_counselling_transaction_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bballb/counselling_transactions')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bballb/counselling_transactions', new_name))
        return os.path.join('bballb/counselling_transactions', new_name)
    else:
        return filename
    





#eco rename functions
def eco_photo_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/eco/photographs')):
            if (each_file == new_name):
                os.remove(os.path.join('media/eco/photographs', new_name))
        return os.path.join('eco/photographs', new_name)
    else:
        return filename
    
def eco_cetresult_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/eco/cetresult')):
            if (each_file == new_name):
                os.remove(os.path.join('media/eco/cetresult', new_name))
        return os.path.join('eco/cetresult', new_name)
    else:
        return filename
    
def eco_10thmarksheet_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/eco/marksheet10th')):
            if (each_file == new_name):
                os.remove(os.path.join('media/eco/marksheet10th', new_name))
        return os.path.join('eco/marksheet10th', new_name)
    else:
        return filename    
    
def eco_12thmarksheet_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file
        for each_file in os.listdir(os.path.join('media/eco/marksheet12th')):
            if (each_file == new_name):
                os.remove(os.path.join('media/eco/marksheet12th', new_name))
        return os.path.join('eco/marksheet12th', new_name)
    else:
        return filename
    
def eco_aadhar_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file
        for each_file in os.listdir(os.path.join('media/eco/aadhar')):
            if (each_file == new_name):
                os.remove(os.path.join('media/eco/aadhar', new_name))
        return os.path.join('eco/aadhar', new_name)
    else:
        return filename

def eco_pancard_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/eco/pancard')):
            if (each_file == new_name):
                os.remove(os.path.join('media/eco/pancard', new_name))
        return os.path.join('eco/pancard', new_name)
    else:
        return filename
    
def eco_ipuregistration_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/eco/ipuregistration')):
            if (each_file == new_name):
                os.remove(os.path.join('media/eco/ipuregistration', new_name))
        return os.path.join('eco/ipuregistration', new_name)
    else:
        return filename

def eco_transaction_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/eco/transactions')):
            if (each_file == new_name):
                os.remove(os.path.join('media/eco/transactions', new_name))
        return os.path.join('eco/transactions', new_name)
    else:
        return filename
    
def eco_counselling_transaction_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/eco/counselling_transactions')):
            if (each_file == new_name):
                os.remove(os.path.join('media/eco/counselling_transactions', new_name))
        return os.path.join('eco/counselling_transactions', new_name)
    else:
        return filename
    





#llm rename functions
def llm_photo_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/llm/photographs')):
            if (each_file == new_name):
                os.remove(os.path.join('media/llm/photographs', new_name))
        return os.path.join('llm/photographs', new_name)
    else:
        return filename
    
def llm_cetresult_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/llm/cetresult')):
            if (each_file == new_name):
                os.remove(os.path.join('media/llm/cetresult', new_name))
        return os.path.join('llm/cetresult', new_name)
    else:
        return filename
    
def llm_10thmarksheet_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/llm/marksheet10th')):
            if (each_file == new_name):
                os.remove(os.path.join('media/llm/marksheet10th', new_name))
        return os.path.join('llm/marksheet10th', new_name)
    else:
        return filename    
    
def llm_12thmarksheet_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file
        for each_file in os.listdir(os.path.join('media/llm/marksheet12th')):
            if (each_file == new_name):
                os.remove(os.path.join('media/llm/marksheet12th', new_name))
        return os.path.join('llm/marksheet12th', new_name)
    else:
        return filename
    
def llm_aadhar_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file
        for each_file in os.listdir(os.path.join('media/llm/aadhar')):
            if (each_file == new_name):
                os.remove(os.path.join('media/llm/aadhar', new_name))
        return os.path.join('llm/aadhar', new_name)
    else:
        return filename

def llm_pancard_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/llm/pancard')):
            if (each_file == new_name):
                os.remove(os.path.join('media/llm/pancard', new_name))
        return os.path.join('llm/pancard', new_name)
    else:
        return filename
    
def llm_ipuregistration_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/llm/ipuregistration')):
            if (each_file == new_name):
                os.remove(os.path.join('media/llm/ipuregistration', new_name))
        return os.path.join('llm/ipuregistration', new_name)
    else:
        return filename

def llm_transaction_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/llm/transactions')):
            if (each_file == new_name):
                os.remove(os.path.join('media/llm/transactions', new_name))
        return os.path.join('llm/transactions', new_name)
    else:
        return filename
    
def llm_counselling_transaction_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/llm/counselling_transactions')):
            if (each_file == new_name):
                os.remove(os.path.join('media/llm/counselling_transactions', new_name))
        return os.path.join('llm/counselling_transactions', new_name)
    else:
        return filename
    
def llm_ug_degree_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/llm/ug-degree')):
            if (each_file == new_name):
                os.remove(os.path.join('media/llm/ug-degree', new_name))
        return os.path.join('llm/ug-degree', new_name)
    else:
        return filename

def llm_graduationresult_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/llm/graduationresult')):
            if (each_file == new_name):
                os.remove(os.path.join('media/llm/graduationresult', new_name))
        return os.path.join('llm/graduationresult', new_name)
    else:
        return filename
    

# Cheque Copy Rename Function (renaming by account number)
def cheque_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.account_number, ext)
        return os.path.join('cheque_copies/', new_name)
    else:
        return filename 