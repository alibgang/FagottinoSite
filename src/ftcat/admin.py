from django.contrib import admin

from .models import FT_Catalogue, Misc_Catalogue, RepertoireList

# Register your models here.
admin.site.register(FT_Catalogue)
admin.site.register(Misc_Catalogue)
admin.site.register(RepertoireList)
