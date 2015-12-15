

# coding=utf-8
from django.template.loader import get_template
from django.http import Http404, HttpResponse
from django.template import Template, Context
import re
import os
import pdb
from django.conf import settings

def counterA(request,text):
    dirofTemplate = settings.TEMPLATES[0]['DIRS'][0]
    file = os.path.join(dirofTemplate,text)
    wordict = {}
    for i in open(file).read().split():
        if i not in wordict:
            wordict[i] = 1
        else:
            wordict[i] += 1
    cd = get_template('htmlText.html')
    cd2 = cd.render(Context({'words':wordict}))
    return HttpResponse(cd2)


