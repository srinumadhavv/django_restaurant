from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

from .models import Meals,Category


class MealsAdmin(SummernoteModelAdmin,admin.ModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['name', 'preperation_time' ,'price']
    search_fields=['name','price']
    list_filter=('category','people',)


admin.site.register(Meals,MealsAdmin)
admin.site.register(Category)