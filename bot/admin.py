from django.contrib import admin
from .models import Voters, Candidates
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class MyModelAdmin(ImportExportModelAdmin):
    pass

class VotersAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","username","position","department","chat_id","nomzod")
    
    def nomzod(self,obj):
      
        return f'{obj.first_name} {obj.last_name}'
    
class CandidatesAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","position","department","yes","no")
    
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
    
    

