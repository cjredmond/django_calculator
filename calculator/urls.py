
from django.conf.urls import url, include
from django.contrib import admin
from app.views import index_view, UserCreateView, ProfileView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_view, name="index_view"),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^accounts/profile/$', ProfileView.as_view(), name="profile_view"),
]
