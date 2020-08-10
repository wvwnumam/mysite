from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('', views.index),
    path('blog/', include('blog.urls'))
]