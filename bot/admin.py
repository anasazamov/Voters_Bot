from django.contrib import admin
from .models import Voters, Candidates
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.action(description="First start")
def first_start_func(modeladmin, request, queryset):
    queryset.update(first_start=True)

@admin.action(description="Reply election")
def reply_election(modeladmin, request, queryset):
    queryset.update(yes=0,no=0)


class MyModelAdmin(ImportExportModelAdmin):
    pass

class VotersAdmin(admin.ModelAdmin):
    list_display = ("id","first_start","first_name","last_name","username","position","department","chat_id","nomzod")
    ordering = ("id","first_start","first_name","last_name","username","position","department","chat_id")
    list_filter = ("id","first_start","position","department")
    search_fields = ("id","first_start","first_name","last_name","username","position","department","chat_id","nomzod")
    actions = [first_start_func]
    
    
    
    def nomzod(self,obj):
      
        return f'{obj.first_name} {obj.last_name}'
    
    
    
class CandidatesAdmin(admin.ModelAdmin):
    ordering = ("id","first_name","last_name","position","department","yes","no")
    list_display = ("id","first_name","last_name","position","department","yes","no")
    list_filter = ("id","position","department") 
    search_fields = ("id","first_name","last_name","position","department","yes","no")
    actions = [reply_election]
    
class MyModelAdmin(ImportExportModelAdmin):
    pass

class Multieadmin(CandidatesAdmin, MyModelAdmin):
    pass

class Multipeadmin(VotersAdmin, MyModelAdmin):
    pass

admin.site.register(Voters, Multipeadmin)
# admin.site.register(Voters, VotersAdmin)
admin.site.register(Candidates, Multieadmin)
# admin.site.register(Candidates, CandidatesAdmin)
    
    

