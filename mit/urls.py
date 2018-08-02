from django.conf.urls import url,include
from django.contrib import admin
from . import views


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # dont touch index it is showing the superimpo
    url(r'^$', views.home, name='home'),
    url(r'^profile-search/$', views.mainpage, name='profile'),
    url(r'^jobs-Geography/(?P<profile>([a-zA-Z0-9, %//\s&\'()-/.\\]+))/$', views.jobsGeog, name='jobsGeog'),
    url(r'^profiles-skills-score/(?P<profile>([a-zA-Z0-9, %//\s&\'()-/.\\]+))/$', views.skillscore, name='closematch'),
    url(r'^tune-the-search/(?P<profile>([a-zA-Z0-9, %//\s&\'()-/.\\]+))/$', views.tuno, name='tuno'),
    url(r'^location-logistics/(?P<profile>([a-zA-Z0-9, %//\s&\'()-/.\\]+))/$', views.loclog, name='loclog'),
    url(r'^finetune-search/(?P<profile>([a-zA-Z0-9, %//\s&\'()-/.\\]+))/$', views.finetune, name='finetune'),
    url(r'^skills-geography/(?P<profile>([a-zA-Z0-9, %//\s&\'()-/.\\]+))/$', views.skillsgeog, name='skillsgeog'),
    url(r'^find-matches/(?P<profile>([a-zA-Z0-9, %//\s&\'()-/.\\%]+))/$', views.runalgo, name='runalgo'),
    url(r'^flamingo-asks/(?P<profile>([a-zA-Z0-9, %//\s&\'()-/.\\%]+))/$', views.askquestions, name='askquestions'),
    url(r'^final-results/(?P<profile>([a-zA-Z0-9, %//\s&\'()-/.\\%]+))/criteria/(?P<score>([a-zA-Z0-9, %//\s&\'()-/.\\%]+))$', views.results, name='results'),

    ]