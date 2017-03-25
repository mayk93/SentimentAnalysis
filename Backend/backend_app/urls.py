from django.conf.urls import url
from backend_app import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^test_view/$', views.test_view),
    url(r'^test_classification/$', views.classify),
]

urlpatterns = format_suffix_patterns(urlpatterns)

