from django.conf.urls import url
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', views.post_list, name= 'post_list'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
]

