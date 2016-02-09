from django.conf.urls import patterns, url
from app import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        #url(r'^reclama_datos/', views.reclama_datos, name='reclama_datos'),
        #url(r'^voto_tapa/$', views.voto_tapa, name='voto_tapa'),
        url(r'^bar/(?P<bar_name_slug>[\w\-]+)/$', views.bar, name='bar'),
        url(r'^bar/(?P<bar_name_slug>[\w\-]+)/(?P<tapa_name_slug>[\w\-]+)/$', views.tapa, name='tapa'),
        url(r'^add_bar/$', views.add_bar, name='add_bar'),
        url(r'^add_tapa/$', views.add_tapa, name='add_tapa'),
        url(r'^registro/$', views.registrar_usuario, name='registro'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^restricted/', views.restricted, name='restricted'),
        url(r'^reclama_datos/', views.reclama_datos, name='reclama_datos'),
        url(r'^voto_tapa/$', views.voto_tapa, name='voto_tapa'),

        )
