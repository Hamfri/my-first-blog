from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # Django will now redirect everything that comes into 'http://127.0.0.1:8000/'
    url(r'', include('blog.urls')),
]
