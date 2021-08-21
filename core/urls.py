
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from main.views import profile, settings_profile
from django.conf.urls.static import static

app_names= 'core'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("main.urls")),
    path('accounts/', include('allauth.urls'), name = "accounts"),
    path('accounts/profile/<int:user_id>', profile , name ='profile'),
    path('accounts/profle/settings/', settings_profile, name = "setting")
]
