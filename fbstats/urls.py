"""fbstats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from mainapp.views import DataPreview, GetPagePostsAPI
from django.views.decorators.cache import cache_page
from action.api import UserDataDetail, UserDataList

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(
        r'^api-auth/', include(
            'rest_framework.urls', namespace='rest_framework')),
    url(
        r'^$',
        TemplateView.as_view(template_name='landing.html'),
        name='home'
    ),
    url(
        r'^preview/$',
        cache_page(60 * 60)(DataPreview.as_view()),
        name='data-preview'
    ),
    url(
        regex=r'^api/stats/$',
        view=GetPagePostsAPI.as_view(),
        name='api'
    ),
    url(
        r'^api/user-data/(?P<pk>[-\d]+)/$',
        UserDataDetail.as_view(),
        name='userdata_detail'
    ),
    url(
        r'^api/user-data/$',
        UserDataList.as_view(),
        name='userdata_list'
    ),
    url(
        r'^user-data/create/$',
        TemplateView.as_view(template_name="create.html")
    ),
    url(
        r'^user-data/update/$',
        TemplateView.as_view(template_name="update.html")
    ),
]
