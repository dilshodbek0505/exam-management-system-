from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect
from django.conf.urls.i18n import i18n_patterns


from .schema import swagger_urlpatterns

urlpatterns = [
    path("", lambda _request: redirect('swagger/')),
    path("api/v1/common/", include("apps.common.urls", namespace="common")),
    path("api/v1/notifications/", include("apps.notification.urls", namespace="notifications")),
    path("api/v1/user/", include("apps.user.urls", namespace="user")),
]

urlpatterns += i18n_patterns(
    path("api/v1/", include("apps.exam.urls", namespace="exam")),
    path("admin/", admin.site.urls),

    prefix_default_language = False
)

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
