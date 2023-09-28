from django.contrib import admin
from form.models import AllowedIP, Login, Bba, BbaTemp, Bcom, BcomTemp, Bjmc, BjmcTemp, Ballb, BallbTemp, Bballb, BballbTemp, Eco, EcoTemp, Llm, LlmTemp, BankDetails, CoursesLogin
from import_export.admin import ExportActionMixin
from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.contrib import messages



# For Temporary Bba
class BbaTempAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ['cet_or_cuet', 'cet_rank']         #for adding filter option
    search_fields = ['cet_rank', 'candidate_first_name']         # for adding search option
    readonly_fields = ['photograph_preview']       # non editable field
    list_display = ('id', 'candidate_first_name', 'cet_rank', 'application_id','ip_address','created_at')    # telling which fields to display
    ordering = ['cet_rank']   # allowing to sort by cet rank


# For Bba
class BbaAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ['allow_for_counselling', 'allow_editing', 'cet_or_cuet', 'cet_rank']         #for adding filter option
    search_fields = ['cet_rank', 'candidate_first_name']         # for adding search option
    readonly_fields = ['photograph_preview']       # non editable field
    list_display = ('id','ipu_registration', 'candidate_first_name', 'allow_for_counselling', 'allow_editing', 'cet_rank', 'application_id','ip_address','created_at')    # telling which fields to display
    list_editable = ('allow_for_counselling', 'allow_editing' )   # to allow editing without opening the record
    ordering = ['cet_rank']   # allowing to sort by cet rank

    #for PDF generation
    #We are just rendering the pdfs.html page and passing desired records as context
    #The 'queryset' parameter defines which records are selected by user before pressing the action button
    @admin.action(description='Generate PDF file')
    def generatePDF(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Bba.objects.filter(pk__in = all_ids) #pk is primary key
        context = {'all_records' : all_records}
        return render(request,'bba/pdfs-bba.html', context)
    
    @admin.action(description='Allow for Counselling')
    def allowCounselling(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Bba.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_for_counselling = True
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were allowed for counselling."
        modeladmin.message_user(request, message, messages.SUCCESS)
    
    @admin.action(description='Do NOT Allow for Counselling')
    def disallowCounselling(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Bba.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_for_counselling = False
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were not allowed for counselling."
        modeladmin.message_user(request, message, messages.SUCCESS)

    @admin.action(description='Allow Editing')
    def allowEditing(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Bba.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_editing = True
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were given editing access."
        modeladmin.message_user(request, message, messages.SUCCESS)
    
    @admin.action(description='Do NOT Allow Editing')
    def disallowEditing(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Bba.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_editing = False
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were denied editing access."
        modeladmin.message_user(request, message, messages.SUCCESS)

    actions = [generatePDF, allowCounselling, disallowCounselling, allowEditing, disallowEditing]  # a list of action buttons in admin panel


# For Temporary Bcom
class BcomTempAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ['cet_or_cuet', 'cet_rank']         #for adding filter option
    search_fields = ['cet_rank', 'candidate_first_name']         # for adding search option
    readonly_fields = ['photograph_preview']       # non editable field
    list_display = ('id', 'candidate_first_name', 'cet_rank', 'application_id','ip_address','created_at')    # telling which fields to display
    ordering = ['cet_rank']   # allowing to sort by cet rank


# For Bcom
class BcomAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ['allow_for_counselling', 'allow_editing', 'cet_or_cuet', 'cet_rank']         #for adding filter option
    search_fields = ['cet_rank', 'candidate_first_name']         # for adding search option
    readonly_fields = ['photograph_preview']       # non editable field
    list_display = ('id','ipu_registration', 'candidate_first_name', 'allow_for_counselling', 'allow_editing', 'cet_rank', 'application_id','ip_address','created_at')    # telling which fields to display
    list_editable = ('allow_for_counselling', 'allow_editing' )   # to allow editing without opening the record
    ordering = ['cet_rank']   # allowing to sort by cet rank

    #for PDF generation
    #We are just rendering the pdfs.html page and passing desired records as context
    #The 'queryset' parameter defines which records are selected by user before pressing the action button
    @admin.action(description='Generate PDF file')
    def generatePDF(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Bcom.objects.filter(pk__in = all_ids) #pk is primary key
        context = {'all_records' : all_records}
        return render(request,'bcom/pdfs-bcom.html', context)
    
    @admin.action(description='Allow for Counselling')
    def allowCounselling(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Bcom.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_for_counselling = True
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were allowed for counselling."
        modeladmin.message_user(request, message, messages.SUCCESS)
    
    @admin.action(description='Do NOT Allow for Counselling')
    def disallowCounselling(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Bcom.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_for_counselling = False
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were not allowed for counselling."
        modeladmin.message_user(request, message, messages.SUCCESS)

    @admin.action(description='Allow Editing')
    def allowEditing(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Bcom.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_editing = True
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were given editing access."
        modeladmin.message_user(request, message, messages.SUCCESS)
    
    @admin.action(description='Do NOT Allow Editing')
    def disallowEditing(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Bcom.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_editing = False
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were denied editing access."
        modeladmin.message_user(request, message, messages.SUCCESS)

    actions = [generatePDF, allowCounselling, disallowCounselling, allowEditing, disallowEditing]  # a list of action buttons in admin panel


# For Temporary Bjmc
class BjmcTempAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ['cet_or_cuet', 'cet_rank']         #for adding filter option
    search_fields = ['cet_rank', 'candidate_first_name']         # for adding search option
    readonly_fields = ['photograph_preview']       # non editable field
    list_display = ('id', 'candidate_first_name', 'cet_rank', 'application_id','ip_address','created_at')    # telling which fields to display
    ordering = ['cet_rank']   # allowing to sort by cet rank


# For Bjmc
class BjmcAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ['allow_for_counselling', 'allow_editing', 'cet_or_cuet', 'cet_rank']         #for adding filter option
    search_fields = ['cet_rank', 'candidate_first_name']         # for adding search option
    readonly_fields = ['photograph_preview']       # non editable field
    list_display = ('id','ipu_registration', 'candidate_first_name', 'allow_for_counselling', 'allow_editing', 'cet_rank', 'application_id','ip_address','created_at')    # telling which fields to display
    list_editable = ('allow_for_counselling', 'allow_editing' )   # to allow editing without opening the record
    ordering = ['cet_rank']   # allowing to sort by cet rank

    #for PDF generation
    #We are just rendering the pdfs.html page and passing desired records as context
    #The 'queryset' parameter defines which records are selected by user before pressing the action button
    @admin.action(description='Generate PDF file')
    def generatePDF(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Bjmc.objects.filter(pk__in = all_ids) #pk is primary key
        context = {'all_records' : all_records}
        return render(request,'bjmc/pdfs-bjmc.html', context)
    
    @admin.action(description='Allow for Counselling')
    def allowCounselling(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Bjmc.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_for_counselling = True
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were allowed for counselling."
        modeladmin.message_user(request, message, messages.SUCCESS)
    
    @admin.action(description='Do NOT Allow for Counselling')
    def disallowCounselling(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Bjmc.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_for_counselling = False
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were not allowed for counselling."
        modeladmin.message_user(request, message, messages.SUCCESS)

    @admin.action(description='Allow Editing')
    def allowEditing(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Bjmc.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_editing = True
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were given editing access."
        modeladmin.message_user(request, message, messages.SUCCESS)
    
    @admin.action(description='Do NOT Allow Editing')
    def disallowEditing(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Bjmc.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_editing = False
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were denied editing access."
        modeladmin.message_user(request, message, messages.SUCCESS)

    actions = [generatePDF, allowCounselling, disallowCounselling, allowEditing, disallowEditing]  # a list of action buttons in admin panel


# For Temporary Ballb
class BallbTempAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ['cet_or_cuet', 'cet_rank']         #for adding filter option
    search_fields = ['cet_rank', 'candidate_first_name']         # for adding search option
    readonly_fields = ['photograph_preview']       # non editable field
    list_display = ('id', 'candidate_first_name', 'cet_rank', 'application_id','ip_address','created_at')    # telling which fields to display
    ordering = ['cet_rank']   # allowing to sort by cet rank


# For Ballb
class BallbAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ['allow_for_counselling', 'allow_editing', 'cet_or_cuet', 'cet_rank']         #for adding filter option
    search_fields = ['cet_rank', 'candidate_first_name']         # for adding search option
    readonly_fields = ['photograph_preview']       # non editable field
    list_display = ('id','ipu_registration', 'candidate_first_name', 'allow_for_counselling', 'allow_editing', 'cet_rank', 'application_id','ip_address','created_at')    # telling which fields to display
    list_editable = ('allow_for_counselling', 'allow_editing' )   # to allow editing without opening the record
    ordering = ['cet_rank']   # allowing to sort by cet rank

    #for PDF generation
    #We are just rendering the pdfs.html page and passing desired records as context
    #The 'queryset' parameter defines which records are selected by user before pressing the action button
    @admin.action(description='Generate PDF file')
    def generatePDF(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Ballb.objects.filter(pk__in = all_ids) #pk is primary key
        context = {'all_records' : all_records}
        return render(request,'ballb/pdfs-ballb.html', context)
    
    @admin.action(description='Allow for Counselling')
    def allowCounselling(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Ballb.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_for_counselling = True
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were allowed for counselling."
        modeladmin.message_user(request, message, messages.SUCCESS)
    
    @admin.action(description='Do NOT Allow for Counselling')
    def disallowCounselling(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Ballb.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_for_counselling = False
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were not allowed for counselling."
        modeladmin.message_user(request, message, messages.SUCCESS)

    @admin.action(description='Allow Editing')
    def allowEditing(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Ballb.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_editing = True
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were given editing access."
        modeladmin.message_user(request, message, messages.SUCCESS)
    
    @admin.action(description='Do NOT Allow Editing')
    def disallowEditing(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Ballb.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_editing = False
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were denied editing access."
        modeladmin.message_user(request, message, messages.SUCCESS)

    actions = [generatePDF, allowCounselling, disallowCounselling, allowEditing, disallowEditing]  # a list of action buttons in admin panel


# For Temporary Bballb
class BballbTempAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ['cet_or_cuet', 'cet_rank']         #for adding filter option
    search_fields = ['cet_rank', 'candidate_first_name']         # for adding search option
    readonly_fields = ['photograph_preview']       # non editable field
    list_display = ('id', 'candidate_first_name', 'cet_rank', 'application_id','ip_address','created_at')    # telling which fields to display
    ordering = ['cet_rank']   # allowing to sort by cet rank


# For Bballb
class BballbAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ['allow_for_counselling', 'allow_editing', 'cet_or_cuet', 'cet_rank']         #for adding filter option
    search_fields = ['cet_rank', 'candidate_first_name']         # for adding search option
    readonly_fields = ['photograph_preview']       # non editable field
    list_display = ('id','ipu_registration', 'candidate_first_name', 'allow_for_counselling', 'allow_editing', 'cet_rank', 'application_id','ip_address','created_at')    # telling which fields to display
    list_editable = ('allow_for_counselling', 'allow_editing' )   # to allow editing without opening the record
    ordering = ['cet_rank']   # allowing to sort by cet rank

    #for PDF generation
    #We are just rendering the pdfs.html page and passing desired records as context
    #The 'queryset' parameter defines which records are selected by user before pressing the action button
    @admin.action(description='Generate PDF file')
    def generatePDF(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Bballb.objects.filter(pk__in = all_ids) #pk is primary key
        context = {'all_records' : all_records}
        return render(request,'bballb/pdfs-bballb.html', context)
    
    @admin.action(description='Allow for Counselling')
    def allowCounselling(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Bballb.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_for_counselling = True
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were allowed for counselling."
        modeladmin.message_user(request, message, messages.SUCCESS)
    
    @admin.action(description='Do NOT Allow for Counselling')
    def disallowCounselling(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Bballb.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_for_counselling = False
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were not allowed for counselling."
        modeladmin.message_user(request, message, messages.SUCCESS)

    @admin.action(description='Allow Editing')
    def allowEditing(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Bballb.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_editing = True
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were given editing access."
        modeladmin.message_user(request, message, messages.SUCCESS)
    
    @admin.action(description='Do NOT Allow Editing')
    def disallowEditing(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Bballb.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_editing = False
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were denied editing access."
        modeladmin.message_user(request, message, messages.SUCCESS)

    actions = [generatePDF, allowCounselling, disallowCounselling, allowEditing, disallowEditing]  # a list of action buttons in admin panel


# For Temporary Eco
class EcoTempAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ['cet_or_cuet', 'cet_rank']         #for adding filter option
    search_fields = ['cet_rank', 'candidate_first_name']         # for adding search option
    readonly_fields = ['photograph_preview']       # non editable field
    list_display = ('id', 'candidate_first_name', 'cet_rank', 'application_id','ip_address','created_at')    # telling which fields to display
    ordering = ['cet_rank']   # allowing to sort by cet rank


# For Eco
class EcoAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ['allow_for_counselling', 'allow_editing', 'cet_or_cuet', 'cet_rank']         #for adding filter option
    search_fields = ['cet_rank', 'candidate_first_name']         # for adding search option
    readonly_fields = ['photograph_preview']       # non editable field
    list_display = ('id','ipu_registration', 'candidate_first_name', 'allow_for_counselling', 'allow_editing', 'cet_rank', 'application_id','ip_address','created_at')    # telling which fields to display
    list_editable = ('allow_for_counselling', 'allow_editing' )   # to allow editing without opening the record
    ordering = ['cet_rank']   # allowing to sort by cet rank

    #for PDF generation
    #We are just rendering the pdfs.html page and passing desired records as context
    #The 'queryset' parameter defines which records are selected by user before pressing the action button
    @admin.action(description='Generate PDF file')
    def generatePDF(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Eco.objects.filter(pk__in = all_ids) #pk is primary key
        context = {'all_records' : all_records}
        return render(request,'eco/pdfs-eco.html', context)
    
    @admin.action(description='Allow for Counselling')
    def allowCounselling(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Eco.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_for_counselling = True
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were allowed for counselling."
        modeladmin.message_user(request, message, messages.SUCCESS)
    
    @admin.action(description='Do NOT Allow for Counselling')
    def disallowCounselling(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Eco.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_for_counselling = False
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were not allowed for counselling."
        modeladmin.message_user(request, message, messages.SUCCESS)

    @admin.action(description='Allow Editing')
    def allowEditing(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Eco.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_editing = True
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were given editing access."
        modeladmin.message_user(request, message, messages.SUCCESS)
    
    @admin.action(description='Do NOT Allow Editing')
    def disallowEditing(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Eco.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_editing = False
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were denied editing access."
        modeladmin.message_user(request, message, messages.SUCCESS)

    actions = [generatePDF, allowCounselling, disallowCounselling, allowEditing, disallowEditing]  # a list of action buttons in admin panel



# For Temporary Llm
class LlmTempAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ['cet_rank']         #for adding filter option
    search_fields = ['cet_rank', 'candidate_first_name']         # for adding search option
    readonly_fields = ['photograph_preview']       # non editable field
    list_display = ('id', 'candidate_first_name', 'cet_rank', 'application_id','ip_address','created_at')    # telling which fields to display
    ordering = ['cet_rank']   # allowing to sort by cet rank


# For Llm
class LlmAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ['cet_rank', 'allow_for_counselling']         #for adding filter option
    search_fields = ['cet_rank', 'candidate_first_name']         # for adding search option
    readonly_fields = ['photograph_preview']       # non editable field
    list_display = ('id','ipu_registration', 'candidate_first_name', 'allow_for_counselling', 'allow_editing', 'cet_rank', 'application_id','ip_address','created_at')    # telling which fields to display
    list_editable = ('allow_for_counselling', 'allow_editing' )   # to allow editing without opening the record
    ordering = ['cet_rank']   # allowing to sort by cet rank

    #for PDF generation
    #We are just rendering the pdfs.html page and passing desired records as context
    #The 'queryset' parameter defines which records are selected by user before pressing the action button
    @admin.action(description='Generate PDF file')
    def generatePDF(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Llm.objects.filter(pk__in = all_ids) #pk is primary key
        context = {'all_records' : all_records}
        return render(request,'llm/pdfs-llm.html', context)
    
    @admin.action(description='Allow for Counselling')
    def allowCounselling(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Llm.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_for_counselling = True
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were allowed for counselling."
        modeladmin.message_user(request, message, messages.SUCCESS)
    
    @admin.action(description='Do NOT Allow for Counselling')
    def disallowCounselling(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Llm.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_for_counselling = False
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were not allowed for counselling."
        modeladmin.message_user(request, message, messages.SUCCESS)

    @admin.action(description='Allow Editing')
    def allowEditing(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Llm.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_editing = True
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were given editing access."
        modeladmin.message_user(request, message, messages.SUCCESS)
    
    @admin.action(description='Do NOT Allow Editing')
    def disallowEditing(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Llm.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_editing = False
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were denied editing access."
        modeladmin.message_user(request, message, messages.SUCCESS)

    actions = [generatePDF, allowCounselling, disallowCounselling, allowEditing, disallowEditing]  # a list of action buttons in admin panel




# For Login
class LoginAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('candidate_name','ipu_registration','password', 'candidate_email', 'ip_address','created_at')
    search_fields = ['ipu_registration',]



# For bank details
class BankDetailsAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('ipu_registration','course', 'account_number','account_holder_name')
    list_filter = ['course']         #for adding filter option



# For bank details
class CoursesLoginAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('ipu_registration','course', )
    list_filter = ['course']         #for adding filter option



# register method takes at most 2 arguements at a time

admin.site.register(BbaTemp, BbaTempAdmin)
admin.site.register(Bba, BbaAdmin)

admin.site.register(BcomTemp, BcomTempAdmin)
admin.site.register(Bcom, BcomAdmin)

admin.site.register(BjmcTemp, BjmcTempAdmin)
admin.site.register(Bjmc, BjmcAdmin)

admin.site.register(BallbTemp, BallbTempAdmin)
admin.site.register(Ballb, BallbAdmin)

admin.site.register(BballbTemp, BballbTempAdmin)
admin.site.register(Bballb, BballbAdmin)

admin.site.register(EcoTemp, EcoTempAdmin)
admin.site.register(Eco, EcoAdmin)

admin.site.register(LlmTemp, LlmTempAdmin)
admin.site.register(Llm, LlmAdmin)


admin.site.register(Login, LoginAdmin)
admin.site.register(CoursesLogin, CoursesLoginAdmin)
admin.site.register(BankDetails, BankDetailsAdmin)

admin.site.register(AllowedIP)
admin.site.register(Session)

admin.site.site_header = "MAIMS Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "MAIMS"