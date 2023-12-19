from django.contrib import admin

# Register your models here.
from brands.models import brandModel
class brandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('brand_name',)}
    list_display = ['brand_name','slug']

admin.site.register(brandModel,brandAdmin)