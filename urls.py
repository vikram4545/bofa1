from django.conf.urls import url
from . import views
from .models import Number
from django.contrib.auth.decorators import login_required


app_name = 'boapp'
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^home/$',views.home1,name='home'),
    url(r'^update/$',views.hbalance,name='hbalance'),
    url(r'^transactions/(?P<id>\d+)/$',views.transactions,name='transactions'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(views.Delete1.as_view()), name='detail'),
    url(r'^delete1/(?P<pk>\d+)/$', login_required(views.Delete2.as_view()), name='detail1'),
    url(r'^delete2/(?P<pk>\d+)/$', login_required(views.Updatev.as_view(model=Number, success_url= "/bofa/home/")), name='detail2'),
    url(r'^delete3/$', login_required(views.CustomerDetails.as_view())),
    ]
