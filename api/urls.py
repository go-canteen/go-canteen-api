"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework import permissions, routers
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from ping import views as ping_views
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
import main.views as main_views
import main.urls

schema_view = get_schema_view(
    openapi.Info(
        title="Gocanteen API",
        default_version="v1",
    ),
    public=False,
    permission_classes=[permissions.AllowAny],
)
from main.urls import router as main_router

router = routers.DefaultRouter()
router.registry.extend(main_router.registry)
router.register(r"users", main_views.UserViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("main/", include(main.urls))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
