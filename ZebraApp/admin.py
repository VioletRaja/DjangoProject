from django.contrib import admin
from ZebraApp import models
from .models import *

admin.site.register(services_pics)
# admin.site.register(ContactUs)
admin.site.register(Home_source)
admin.site.register(home_url)
admin.site.register(Service_page)
admin.site.register(projects_model)
admin.site.register(Project_catagory)
admin.site.register(Project_site_pics)
admin.site.register(about_us)
admin.site.register(client_logo)
admin.site.register(rating)
admin.site.register(Review)


class MemberAdmin(admin.ModelAdmin):
    list_display = ("username", "phone","message",)

admin.site.register(ContactUs, MemberAdmin)