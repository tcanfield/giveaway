from django.conf.urls import url
from django.conf import settings
from django.contrib.staticfiles.urls import static
from . import views

urlpatterns = [
    url(r'^$', views.category_list, name='category_list'),
    url(r'^giveaway_list/(?P<pk>\d+)/$', views.giveaway_list, name='giveaway_list'),
    url(r'^giveaway/(?P<pk>\d+)/$', views.giveaway, name='giveaway'),
    url(r'^enter_giveaway/(?P<giveaway_id>\d+)/$', views.enter_giveaway, name='enter_giveaway')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
