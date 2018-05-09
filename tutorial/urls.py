from django.contrib import admin
from django.urls import path, re_path, include
from tutorial import views

urlpatterns = [
    re_path(r'^$', views.login_redirect, name='login_redirect'),
    path('admin/', admin.site.urls),
    re_path(r'^accounts/', include('accounts.urls', namespace='accounts')),

]
