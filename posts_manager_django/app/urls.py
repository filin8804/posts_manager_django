from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views
from . import ajax

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add-post/$', views.add_post, name='add_post'),
    url(r'^post/add$', ajax.post_add, name='post_add'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)