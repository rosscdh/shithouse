"""
URL configuration for shithouse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from shithouse.apps.default.urls import urlpatterns as default_urls
from shithouse.apps.agency.urls import urlpatterns as agency_urls
from shithouse.apps.house.urls import urlpatterns as house_urls

urlpatterns = default_urls + [
    path("admin/", admin.site.urls),
    path('comment/', include('comment.urls')),
    path('api/', include('comment.api.urls')),  # only required for API Framework
    path("__debug__/", include("debug_toolbar.urls")),
] + agency_urls + house_urls + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)