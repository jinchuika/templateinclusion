from django.conf.urls import url
from django.contrib import admin
from app.views import PostView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<pk>\d+)/$', PostView.as_view(), name='post_detail'),
]
