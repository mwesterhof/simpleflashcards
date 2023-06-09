from django.contrib import admin
from django.urls import include, path

from main import urls as main_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cards/', include(main_urls)),
]
