from django.contrib import admin

from .models import Skills, Element, Aboutme, Examples, Contact


class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


class ElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'description_element', 'logotypes')


class AboutmeAdmin(admin.ModelAdmin):
    list_display = ('id', 'info', 'icons')


class ExamplesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'hr']


admin.site.register(Skills, SkillsAdmin)
admin.site.register(Element, ElementAdmin)
admin.site.register(Aboutme, AboutmeAdmin)
admin.site.register(Examples, ExamplesAdmin)
admin.site.register(Contact, ContactAdmin)