from django.conf.urls import patterns, include, url
from django.contrib   import admin
admin.autodiscover()
from django.conf.urls.static import static
import settings

urlpatterns = patterns('',
	url(r'^admin/'                  , include(admin.site.urls)),
	url(r'^Cultura/$'              , 'cms_put.views.principal'),
	url(r'^Cultura/login$'         , 'cms_put.views.login_view'),
	url(r'^Cultura/logout$'        , 'cms_put.views.logout_view'),
	url(r'^Cultura/cambio$'        , 'cms_put.views.cambio'),
	url(r'^Cultura/todas$'         , 'cms_put.views.todas'),
	url(r'^Cultura/(.+)/RSS$'      , 'cms_put.views.canalRSS'),
	url(r'^Cultura/actividad/(\d+)'   , 'cms_put.views.actividad'),
	url(r'^Cultura/ayuda'   , 'cms_put.views.ayuda'),
    url(r'^images/(?P<path>.*)$'  , 'django.views.static.serve', {'document_root': settings.STATIC_URL,}),
    url(r'^Cultura/(.+)'          , 'cms_put.views.usuario'),
)
