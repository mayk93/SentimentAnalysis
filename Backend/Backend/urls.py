from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('backend_app.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

