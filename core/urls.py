"""
URL configuration for core project.

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

from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
    openapi.Info(
        title="GNOME Nepal Api",
        default_version="v1",
        description="GNOME Nepal API",
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
)
urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path("summernote/", include("django_summernote.urls")),
    path(
        "healthcheck/",
        include("healthcheck.urls"),
    ),
    path(
        "api/v1/",
        include(
            [
                #
                # v1 urls
                path("newsletter/", include("newsletter.urls")),
                path("faqs/", include("faq.urls")),
                path("events/", include("event.urls")),
            ]
        ),
    ),
]

# we will be using this in production as well,
# we have NFS we don't need to worry about this
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
