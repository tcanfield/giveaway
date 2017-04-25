from django.conf.urls import url
from django.conf import settings
from django.contrib.staticfiles.urls import static
from . import views

urlpatterns = [
    url(r'^$', views.category_list, name='category_list'),
    url(r'^/giveaway_list/(?P<pk>\d+)/$', views.giveaway_list, name='giveaway_list')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
