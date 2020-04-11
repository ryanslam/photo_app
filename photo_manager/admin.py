from django.contrib import admin
from photo_manager.models import *


class HomePagePhotoAdmin(admin.ModelAdmin):
	list_display = ('name', 'date', 'thumb')
	list_filter = ['date']
	search_fields = ['name']


class PhotographyPhotoAdmin(admin.ModelAdmin):
	list_display = ('name', 'category', 'thumb', 'cover')
	list_filter = ['category']
	search_fields = ['name']


class AboutInfoAdmin(admin.ModelAdmin):
	list_display = ('title', 'body')


class PortfolioEntryAdmin(admin.ModelAdmin):
	list_display = ('name', 'category', 'position', 'year_start', 'year_end', 'description')
	list_filter = ['year_start']
	search_fields = ['name']


admin.site.register(HomePagePhoto, HomePagePhotoAdmin)
admin.site.register(PhotographyPhoto, PhotographyPhotoAdmin)
admin.site.register(AboutInfo, AboutInfoAdmin)
admin.site.register(PortfolioEntry, PortfolioEntryAdmin)
