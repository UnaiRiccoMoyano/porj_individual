from django.contrib import admin
from django.urls import include, path
from league import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('league/', include('league.urls')),
]