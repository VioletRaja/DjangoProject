from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from ZebraApp import urls
from ZebraApp import views

admin.site.site_header='ZEBRA ADMIN'
admin.site.site_title='ZEBRA ADMIN PORTAL'
admin.site.index_title='WELCOME TO ZEBRA ADMIN PORTAL'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('ZebraApp.urls')),
    path('',views.index,name='index'),
] 

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


# urlpatterns = [
#     # Other URL patterns
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
