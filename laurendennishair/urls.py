from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


js_info_dict = {
    'packages': ('django.conf',),
}

urlpatterns = patterns('',
    # Examples:
    url(r'^inplaceeditform/', include('inplaceeditform.urls')),
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog', js_info_dict),
    url(r'^$',  include('ldh.urls')),

    # url(r'^blog/', include('blog.urls')),
    url(r'^example/$', 'ldh.views.example', name='example'),

    url(r'^admin/', include(admin.site.urls)),
)

if 'laurendennishair.example_extra_fields' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^extra_fields/', include('laurendennishair.example_extra_fields.urls'))
    )
    if 'ajax_select' in settings.INSTALLED_APPS:
        from ajax_select import urls as ajax_select_urls
        urlpatterns += patterns('',
            url(r'^ajax_select/', include(ajax_select_urls))
        )


urlpatterns += patterns('',
    (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:],
     'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT,
      'show_indexes': True}),
)
