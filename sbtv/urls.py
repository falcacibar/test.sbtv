from django.conf.urls import include, url
# from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'sbtv.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^futbol/', 'sbtv.football.views.matches')
    , url(r'^$', 'sbtv.dictgen.views.dictgen')
    
]
