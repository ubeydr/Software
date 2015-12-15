from django.template.loader import get_template
from django.http import Http404, HttpResponse
from django.template import Template, Context
import re
import os

def counterA(request,text):
    path = os.getcwd()
    path = os.path.join(path,'templates/')
    text = os.path.join(path,text)
    file = (text,'r')
    wordlist = {}
    for line in file:
        split = re.compile('\\W*')
        line = [word.lower() for word in split.split(text) if word != '']
        for word in line:
            wordlist.setdefault(word,0)
            wordlist[word] = wordlist[word] + 1

    cd = get_template('htmlText.html')
    cd2 = cd.render(Context({'words':wordlist}))
    return HttpResponse(cd2)