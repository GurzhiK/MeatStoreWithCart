from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    # path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),
    path('acc/', include('accounts.urls')),
]

urlpatterns += doc_urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^.*',
                        TemplateView.as_view(template_name='index.html'))]
