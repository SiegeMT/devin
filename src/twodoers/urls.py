from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('', include('landing.urls')),
    path('plume/', include('plume.urls')),
    path('admin/', admin.site.urls),
] 
urlpatterns += staticfiles_urlpatterns()