"""futbolkas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, patterns, include
from django.contrib import admin
from django.views.i18n import set_language
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static

from main.views import PaysCreateView

urlpatterns = patterns('',
                       url(r'^admin/', admin.site.urls),
                       url(r'^$', 'main.views.home'),
                       url(r'^i18n/', csrf_exempt(set_language), name="my_set_language"),
                       url(r'^souvenir4you/', 'main.views.home'),
                       url(r'^pays/', PaysCreateView.as_view(), name="pays"),
                       url(r'^ru/', include('mainru.urls')),
                       url(r'^item/(?P<alias>[^/]+)', 'main.views.item'),
                       url(r'^order/', 'main.views.order'),
                       url(r'^(?P<alias>[^/]+)', 'main.views.get_category'),
                       )
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
