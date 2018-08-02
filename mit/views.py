from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.conf import settings
import requests
import pycurl
import urllib
import json
import StringIO
import certifi
from os.path import join, dirname
from os import environ
from django.conf import settings
import urllib
from . import recosimi
import operator
import os
# import line to: from C:/Users/anshulmi/Anaconda2/Lib/site-packages/watson_developer_cloud import VisualRecognitionV3 as VisualRecognitionV3



def home(request):
    profile = request.GET.get("profile")

    return render(request, 'mit/index.html' , {"profile" : profile})

def mainpage(request):
    profile = request.GET.get("profile")
    if not profile :
        profile = "ApplicationDeveloper"
    return render(request, 'mit/mainpage.html' , {"profile" : profile})

def jobsGeog(request, profile):
    if not profile :
        profile = "ApplicationDeveloper"

    return render(request, 'mit/jobs_geog.html' , {"profile" : profile})

def skillsgeog(request, profile):
    if not profile :
        profile = "ApplicationDeveloper"
    skills = request.session["list"]
    print "skillsss" , skills
    return render(request, 'mit/skillsgeog.html' , {"profile" : profile, "skills": skills})

def skillscore(request, profile):
  
    if not profile :
        profile = "ApplicationDeveloper"
    return render(request, 'mit/skillscore.html' , {"profile" : profile})


def askquestions(request, profile):
  
    if not profile :
        profile = "ApplicationDeveloper"
    return render(request, 'mit/askquestions.html' , {"profile" : profile})




def results(request, profile, score):
    
    if not profile or profile is None or profile == "None":
        profile = "ApplicationDeveloper"
    p = recosimi.getsimilarprofiles()
    print "profile is "  + profile
    simkeys = p.getrecommendedState(profile, float(score))


    simkeys1 = dict(simkeys[1])
    print simkeys1
    simkeys1= sorted(simkeys1.iteritems(), key=operator.itemgetter(1), reverse=True)
    
    simcolors=[]
    simk = []
    for i,k in simkeys1:
        if float(k) > 0.96:
            simk.append(i)
            simcolors.append("green") 
        elif float(k) > 0.90:
            simk.append(i)
            simcolors.append("orange") 
        elif float(k) > 0.85:
            simk.append(i)
            simcolors.append("red") 
        else :
            simk.append(i)
            simcolors.append("black")
            
    similist = zip(simk, simcolors)  


    return render(request, 'mit/results.html' , {"profile" : profile , "similarprofiles": similist, "similarprofiles_2": simkeys[0]})



def runalgo(request, profile):
    
    if not profile :
        profile = "ApplicationDeveloper"
    p = recosimi.getsimilarprofiles()
    s = profile
    simkeys = dict(p.getprofiles(s, 0.8))
    print simkeys
    simkeys= sorted(simkeys.iteritems(), key=operator.itemgetter(1), reverse=True)
    
    simcolors=[]
    simk = []
    for i,k in simkeys:
        if float(k) > 0.96:
            simk.append(i)
            simcolors.append("green") 
        elif float(k) > 0.90:
            simk.append(i)
            simcolors.append("orange") 
        elif float(k) > 0.85:
            simk.append(i)
            simcolors.append("red") 
        else :
            simk.append(i)
            simcolors.append("black")
            
    similist = zip(simk, simcolors)  
    request.session["list"] =  similist
    print "checking", request.session["list"] 
    return render(request, 'mit/runalgo.html' , {"profile" : profile , "similarprofiles": similist})

def tuno(request, profile):
    
    if not profile :
        profile = "ApplicationDeveloper"
    return render(request, 'mit/tuno.html' , {"profile" : profile})

def loclog(request, profile):
    profile = request.GET.get("profile")
    if not profile :
        profile = "ApplicationDeveloper"
    return render(request, 'mit/loclog.html' , {"profile" : profile})


def finetune(request, profile):
    profile = request.GET.get("profile")
    if not profile :
        profile = "ApplicationDeveloper"
    return render(request, 'mit/finetune.html' , {"profile" : profile})



