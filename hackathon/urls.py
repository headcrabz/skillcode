"""hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from superimpo import views
from django.conf.urls.static import static
from superimpo.views import home
from django.conf import settings
from mit import urls
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # dont touch index it is showing the superimpo

    url(r'^', include('mit.urls')),
    # url(r'^', include('audible.urls')),
    # url(r'^index/$', views.home, name='home'),
    # url(r'^flight/$', flight, name='flight'),
    # url(r'^tosee/$', placestosee, name='placestosee'),
    
    # ##############################################
    # url(r'^picture/$', picture, name='picture'),
    # url(r'^keyword/$', keyword, name='keyword'),
    # url(r'^location/$', location_home, name='location_home'),
    # url(r'^ade/$', ade, name='ade'),
    # url(r'^ademessage/$', ade, name='ademessage'),    
    # url(r'^location_results/$', location, name='location'),
    # url(r'^Mood Based/$', mood, name='mood'),
    # url(r'^logined/$', logined, name='logined'),
    # url(r'^details/(?P<asin>([a-zA-Z0-9]+))/$', analysereviews, name='analysereviews'),
    # url(r'^$', save_embed, name='save_embed'),
    # url(r'^cloudant/$', cloudant, name='cloudant'),
    # url(r'^accounts/', include('allauth.urls')),
    # url(r'^checksms/',  check_sms, name='check_sms'),
    # url(r'^response_sms/',  response_sms, name='response_sms'),
    # url(r'^inventorytaker/',  inventory_tracker, name='inventory_tracker'),
    # url(r'^graphql', GraphQLView.as_view(graphiql=True, schema=schema)),
    # url(r'^', include('django_alexa.urls')),
    # url(r'^bank', bank, name='bank'),
    
    # url(r'^index$', views.home, name='home'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)