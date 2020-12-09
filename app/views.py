# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
from .form import AnalyseForm



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
import speech_recognition as sr
import json


def Speech_to_text(file):
    data = {}

    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Reading Audio file as source
    # listening the audio file and store in audio_text variable

    with sr.AudioFile(file) as source:

        audio_text = r.listen(source)

        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:

            # using google speech recognition
            text = r.recognize_google(audio_text)
            y = json.dumps(text)
            #print('Converting audio transcripts into text ...')
            return y

        except:
            return 'Sorry.. run again...'


@login_required(login_url="/login/")
def index(request):
    try:
        if request.method == "POST":
            form = AnalyseForm(request.POST, request.FILES)
            if form.is_valid():
                audio = request.FILES['Fichier_AUDIO']
                text = Speech_to_text(audio)
                return render(request, "index.html",
                              context={'text': text})

        else:
            form = AnalyseForm()
        return render(request, 'index.html', {'form': form})
    except:
        context = {}

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))




@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))















