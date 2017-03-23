def get_urls_content():
    content = '''
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('backend_app.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    '''.strip()
    return content + "\n\n"


def get_app_urls_content():
    content = '''
from django.conf.urls import url
from backend_app import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^test_view/$', views.test_view),
]

urlpatterns = format_suffix_patterns(urlpatterns)
    '''.strip()

    return content + "\n\n"


with open("urls.py", "w+") as destination:
    urls_content = get_urls_content()
    destination.write(urls_content)

with open("app_urls.py", "w+") as destination:
    urls_content = get_app_urls_content()
    destination.write(urls_content)