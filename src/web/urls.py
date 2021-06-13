from django.contrib import admin
from django.urls import path, reverse_lazy
from django.urls.conf import include
from django.views.generic.base import RedirectView

from web.courier_api.views import FileUploadView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", RedirectView.as_view(url='/api/')),
    path('api/', include('web.courier_api.urls', namespace='courier')),
    path('upload/', FileUploadView.as_view(), name="file_upload"),
    path('api-auth/', include('rest_framework.urls')),
]
